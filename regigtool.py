
from msilib.sequence import tables
from PyQt5 import QtCore, QtGui, QtWidgets
import time
class Ui_RegIG(object):
    def setupUi(self, RegIG):
        RegIG.setObjectName("RegIG")
        RegIG.resize(630, 429)
        self.centralwidget = QtWidgets.QWidget(RegIG)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 100, 601, 301))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 21))
        self.label.setObjectName("label")
        self.threadcount = QtWidgets.QSpinBox(self.centralwidget)
        self.threadcount.setGeometry(QtCore.QRect(90, 10, 31, 22))
        self.threadcount.setProperty("value", 1)
        self.threadcount.setObjectName("threadcount")
        self.startreg = QtWidgets.QPushButton(self.centralwidget)
        self.startreg.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.startreg.setObjectName("startreg")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 10, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        RegIG.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegIG)
        self.statusbar.setObjectName("statusbar")
        RegIG.setStatusBar(self.statusbar)

        self.retranslateUi(RegIG)
        QtCore.QMetaObject.connectSlotsByName(RegIG)

    def retranslateUi(self, RegIG):
        _translate = QtCore.QCoreApplication.translate
        RegIG.setWindowTitle(_translate("RegIG", "RegIG"))
        self.label.setText(_translate("RegIG", "ThreadCount"))
        self.startreg.setText(_translate("RegIG", "StartReg"))
        self.comboBox.setItemText(0, _translate("RegIG", "Mail.tm"))
        self.comboBox.setItemText(1, _translate("RegIG", "TempMail"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mail"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ip"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Trạng Thái"))
        self.tableWidget.setColumnWidth(0,100) #cái này là set độ dài của column nhé
        self.tableWidget.setColumnWidth(1,100)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,170)
        self.tableWidget.setColumnWidth(4,151)
        self.startreg.clicked.connect(self.StartReg)
    def hienthi(self, row, column, text):
        print(row)
        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(text)) #bài trước có rồi nha
    def delay(self, countdelay):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(int(countdelay*1000), loop.quit) #cái này nó tính cứ 1000 là 1 giây nên mình sẽ để nhân nó như vậy 
        loop.exec()
    # do ip nha
    def StartReg(self):#ip bẩn quá rồi
        # đợi 10 giây thì giao diện mới hết not re
        #time.sleep(10) #test cho xem queen
        self.startreg.setEnabled(False)# tạo sự kiện bấm chuột vào button thì sẽ tắt nút đó đi
        import regtestig # lấy file bên kia sang
        # cho nó lặp vô hạn 
        while True:
            #đó đồng đều rồi
            # self.threadcount.value() lấy theo số luồng của spinBox
            for i in range(self.threadcount.value()): #giờ thì tạo vòng lặp for để reg liên tục các luồng vd:5 thì 5 luồng sẽ được tạo ra và reg liên tục
                # giờ tạo cái thêm row cho table
                self.tableWidget.insertRow(self.tableWidget.rowCount())
                row = self.tableWidget.rowCount() - 1  #lỗi 
                # không để kiểu này để gọi sang kia à hình như được :))
                self.reg = regtestig.Reg(self, row) #truyền self của bên này sang bên kia tý còn gọi
                # truyền vào để cho giá trị của row nó không thay đổi 
                # vd gọi self.row thì luông đầu tiên vẫn được nhưng lần sau gọi lại self.row sẽ thay đổi nên sẽ bị nhầm
                self.reg.hienthi.connect(self.hienthi) # connect def hiển thị
                self.reg.start() #QThread: Destroyed while thread is still running vì vòng lặp while quá nhanh nên luồng tạo nhiều quá sẽ bị hủy
                self.delay(0.01)
            self.delay(120)
            
            # để cho nó dừng lại 120s khi 5 luồng đó đang thực hêin
            # mình sẽ lấy code sẵn delay trong pyqt của mình nhá
             #không dược để như này vì hàm time sẽ làm dừng giao diện trong khoảng thơif gian đó
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegIG = QtWidgets.QMainWindow()
    ui = Ui_RegIG()
    ui.setupUi(RegIG)
    RegIG.show()
    sys.exit(app.exec_())
