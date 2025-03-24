from queue import Full
import sys
from PyQt5 import QtWidgets
from bai9 import Ui_MainWindow
from from_9.them_sua import Ui_Form

class Mode(QtWidgets.QDialog):
    def __init__(self, parent = ..., flags = ...):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.item = False
        self.ui.pushButton.clicked.connect(self.output)
        self.ui.pushButton_2.clicked.connect(self.close)
    def output(self):
        self.ten = self.ui.lineEdit.text()
        self.sdt = self.ui.lineEdit_2.text()
        self.close()
        self.item = True
        return self.ten, self.sdt
    def check(self):
        return self.item   
class Bai9(QtWidgets.QMainWindow):
    def __init__(self):
        super(Bai9, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.them)
        self.ui.pushButton_4.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.sua)
        self.ui.tableWidget.cellClicked.connect(self.hien_thong_tin)
        self.ui.pushButton_3.clicked.connect(self.xoa)
    def them(self):
        mode = Mode(self)
        mode.exec_()
        ten, sdt = mode.output()
        if  mode.check():  
            them_song = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(them_song)
            self.ui.tableWidget.setItem(them_song, 0, QtWidgets.QTableWidgetItem(ten))
            self.ui.tableWidget.setItem(them_song, 1, QtWidgets.QTableWidgetItem(sdt))
        else:
            QtWidgets.QMessageBox.information(self, "Thông báo!", "Tên và số điện thoại không được để trống!")
        self.close
    def hien_thong_tin(self, dong):
        mode = Mode(self)
        self.dong_duoc_chon = dong
        ten_item = self.ui.tableWidget.item(self.dong_duoc_chon, 0)
        sdt_item = self.ui.tableWidget.item(self.dong_duoc_chon, 1)
        self.ten = ten_item.text()
        self.sdt = sdt_item.text()
    def sua(self):
        try:
            mode = Mode(self)
            mode.ui.lineEdit.setText(self.ten)
            mode.ui.lineEdit_2.setText(self.sdt)
            mode.exec_()
            mode.ui.label.setText("Nhập tên muốn sữa: ")
            if mode.check():
                ten, sdt = mode.output()
                self.ui.tableWidget.setItem(self.dong_duoc_chon, 0, QtWidgets.QTableWidgetItem(ten))
                self.ui.tableWidget.setItem(self.dong_duoc_chon,1, QtWidgets.QTableWidgetItem(sdt))
            else:
                 QtWidgets.QMessageBox.information(self, "Thông báo!", "Huỷ thành công!")
        except:
            QtWidgets.QMessageBox.information(self, "Thông báo!", "Chưa chọn dòng cần sữa!")
    def xoa(self):
        dong = self.ui.tableWidget.currentRow()
        if dong != -1:
            self.ui.tableWidget.removeRow(dong)
        else:
            QtWidgets.QMessageBox.information(self, "Thông báo!", "Chưa chọn dòng để xoá!")
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Bai9()
    win.show()
    sys.exit(app.exec_())