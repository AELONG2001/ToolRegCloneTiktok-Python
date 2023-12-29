import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin


gl = GoLogin({
 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTg3ZWM5ZjVkODcxMDE0NDY5NDc1MjQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTg3ZWRhNTVkODcxMDE0NDY5NGY1YTQifQ.iUHo5CDRIds7uGGQ4eip4WkbtCEOXTLlTnwCkzcy6jA',
})

profile_id = gl.create({
    "name": '1',
    "os": 'win',
    "navigator": {
        "language": 'vi',
        "userAgent": 'random',
        "resolution": 'random',
        "platform": 'win',
    },
    'proxyEnabled': True,
    'proxy': {
        'mode': 'http',
        'host': '117.5.56.126',
        'port': '5014',
        'username': '',
        'password': '',
    },
    "webRTC": {
        "mode": "alerted",
        "enabled": True,
    },
})

gl = GoLogin({
 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTg3ZWM5ZjVkODcxMDE0NDY5NDc1MjQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTg3ZWRhNTVkODcxMDE0NDY5NGY1YTQifQ.iUHo5CDRIds7uGGQ4eip4WkbtCEOXTLlTnwCkzcy6jA',
 'profile_id': profile_id
})

print('profile id=', profile_id)

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.tiktok.com/signup/phone-or-email/email")
time.sleep(20)
driver.close()
gl.stop()
gl.delete(profile_id)
print("complete")