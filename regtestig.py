import threading, time, requests, random, re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PyQt5 import QtCore #lấy Qthread ở bên kia nữa
class Reg(QtCore.QThread): #viết luôn bên này nhá tý import sang cũng được
    hienthi = QtCore.pyqtSignal(int, int, str)
    def __init__(self, all, row):
        super().__init__()
        self.all = all
        self.row = row
    def getDriver(self):
        self.hienthi.emit(self.row, 4, "Đang mở chrome")
        options = webdriver.ChromeOptions()
        options.add_argument("--app=https://httpbin.org/ip") #nó sẽ hiển thị chrome đó như một cái app
        options.add_argument("--window-size=270,425") #set size của chrome
        s = Service("chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=options) #quên
        return driver
    def getName(self):
        self.hienthi.emit(self.row, 4, "Đang Get Name")
        gender = random.choice(["male", "female"])
        self.nameig = requests.get("https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/").json()["data"][gender] #sợ trùng với name của threading nên để vậy
    def randomBirthday(self):
        self.d = str(random.randint(1,30)) #random ngày nha
        self.m = str(random.randint(1,12)) #random tháng nha
        self.y = str(random.randint(1999,2000)) #random năm nha
        #chuyển nó về string
    def GetTMmail(self):
        self.hienthi.emit(self.row, 4, "Đang Get Mail")
        user = ["a","b","c","d","e","f","g","h","u","i","o","y","m","n","l","h","q","x","s","k","p","t","w","v","j","z"]
        self.mail = ""
        for i in range(4):
            num = str(random.randint(1,100))
            self.mail += random.choice(user)
            self.mail += num
        domain = requests.get("https://api.mail.tm/domains?page=1", headers={"content-type":"application/json"}).json()["hydra:member"][0]["domain"]
        self.mail += "@"+domain
        data = '{"address":"'+self.mail+'","password":"29112004"}'
        acc = requests.post("https://api.mail.tm/accounts", data, headers={"content-type":"application/json"}).json()
        self.token = requests.post("https://api.mail.tm/token", data, headers={"content-type":"application/json"}).json()["token"]
    def GetCodeTMmail(self):
        self.hienthi.emit(self.row, 4, "Đang GetCode")
        messages = requests.get("https://api.mail.tm/messages",headers={"authorization":"Bearer "+self.token}).text
        c = re.findall(r'subject":".*?code',messages)
        if c == []:
            return ""
        return re.findall(r"\d{6}",c[0])[0]
    def run(self):
        self.hienthi.emit(self.row, 4, "Bắt đầu Reg")
        if self.all.comboBox.currentText() == "Mail.tm":
            print("ok nè đm")
            # để test nhá xem được khôpng
            self.GetTMmail()
        self.hienthi.emit(self.row, 2, self.mail)
        # cái proxy mình không có nên các bạn tự tìm hiểu nha làm 
        self.getName()
        driver = self.getDriver()
        driver.get("https://www.instagram.com/accounts/emailsignup/")
        driver.implicitly_wait(5) #chờ 5s đến khi element hiện
        if "Please wait a few minutes before you try again." in driver.page_source:
            driver.refresh() # load lại trang nha
        driver.implicitly_wait(5) #chờ 5s đến khi element hiện
        driver.find_element(By.NAME, "emailOrPhone").send_keys(self.mail) #3thichs thì ghi từng cái nhá chứ mình không thích thế miễn reg là được rồi :))
        driver.find_element(By.NAME, "fullName").send_keys(self.nameig)
        for i in range(1):
            driver.find_element(By.XPATH, '//span[text()="Refresh suggestion"]').click() #lỗi :))
            time.sleep(1)#chưa thử class bao giờ tý lỗi không biết nha làm vậy cho nhanh :)) cho nó bấm 2 lần để cho username về giống tên cho đẹp
        username = driver.find_element(By.NAME, 'username').get_attribute("value") #nó là value không phải text nha
        print(username)
        self.hienthi.emit(self.row, 0, username)
        self.hienthi.emit(self.row, 1, "29112004")
        #click cho load username khỏi phải nhập 
        driver.find_element(By.NAME, "password").send_keys("29112004")
        # /html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button
        driver.find_element(By.XPATH, '//button[text()="Sign up"]').click() #lên gg search xpath tương đối nha không thì như này cho nhanh
        self.randomBirthday()
        driver.implicitly_wait(10)
        birthday = driver.find_elements(By.CLASS_NAME, "h144Z  ")
        Select(birthday[0]).select_by_value(self.m)
        Select(birthday[1]).select_by_value(self.d)
        Select(birthday[2]).select_by_value(self.y)
        driver.find_element(By.XPATH, '//button[text()="Next"]').click()
        self.hienthi.emit(self.row, 4, "Đang chờ code")
        time.sleep(20)
        code = self.GetCodeTMmail()
        driver.find_element(By.NAME, "email_confirmation_code").send_keys(code)
        driver.find_element(By.XPATH, '//button[text()="Next"]').click()
        time.sleep(10)
        if "The IP address you are using has been flagged as an open proxy." in driver.page_source:
            self.hienthi.emit(self.all.row, 4, "Reg thất bại Proxy bị gắn lá cờ")
            driver.close()

# để mình lấy code get mail get code của mình luôn nha làm lại tốn time lắm
#để reg nhiếu luồng
# for o in range(1):
#     f = Reg()
#     f.start()
#các bạn tìm hiểu thêm nha chứ mình không dạy làm hoàn thiện
# change proxy thì search gg là có hết
#ok
# nay làm giao diện tool regig nhé
# để set cho nhỏ cái chrome đã