import sys
from PySide import QtCore, QtGui
from passenger_home import *
from passenger_checkin import *
from train_schedule import *

class passengerTrainSchedWidget(QtGui.QWidget):
    goBack = QtCore.Signal()
    
    def __init__(self, current_user_id):
        super(passengerTrainSchedWidget, self).__init__()
        self.current_user_id = current_user_id
        self.initUI()
    
    def initUI(self):
        self.widget_type = 'passengerTrainSchedWidget'
        
        self.ts = train_schedules()
        self.ts.query_train_schedules()
        
        self.createLabels()
    
    def createLabels(self):
        self.setObjectName(("Form"))
        self.resize(500, 300)
        
        self.TrainSchedule_Title = QtGui.QLabel(self)
        self.TrainSchedule_Title.setGeometry(QtCore.QRect(188, 20, 150, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TrainSchedule_Title.setFont(font)
        self.TrainSchedule_Title.setObjectName(("TrainSchedule_Title"))
        
        self.schedule_table = QtGui.QTableWidget(self)
        self.schedule_table.setGeometry(QtCore.QRect(100, 100, 302, 175))
        self.schedule_table.setObjectName(("schedule_table"))
        self.schedule_table.setRowCount(5)
        self.schedule_table.setColumnCount(3)
        self.schedule_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.schedule_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.schedule_table.horizontalHeader().setVisible(True)
        self.schedule_table.verticalHeader().setVisible(False)
        listOfHeaders = ['Train No', "Status", "Last Location"]
        self.schedule_table.setHorizontalHeaderLabels(listOfHeaders)
        self.populateTable()
        
        

        
        self.backButton = QtGui.QPushButton(self)
        self.backButton.setGeometry(QtCore.QRect(20, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backButton.setFont(font)
        self.backButton.setObjectName(("backButton"))
        self.backButton.clicked.connect(self.goBackOneScreen)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def populateTable(self):
        #self.schedule_table.setItem(2,2,QtGui.QTableWidgetItem("hi"))
        for trainNo in xrange(5):
            TrainNumber = str(trainNo+1)
            self.schedule_table.setItem(trainNo, 0, QtGui.QTableWidgetItem(TrainNumber))
            status = self.ts.get_status(trainNo+1)
            self.schedule_table.setItem(trainNo, 1, QtGui.QTableWidgetItem(status))
            recentLoc = self.ts.get_recent_location(trainNo+1)
            self.schedule_table.setItem(trainNo, 2, QtGui.QTableWidgetItem(recentLoc))
            

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.TrainSchedule_Title.setText(QtGui.QApplication.translate("Form", "Train Schedule", None, QtGui.QApplication.UnicodeUTF8))
    
        self.backButton.setText(QtGui.QApplication.translate("Form", "<- Go Back", None, QtGui.QApplication.UnicodeUTF8))

    def goBackOneScreen(self):
        print "Going Back one screen"
        self.goBack.emit()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = passengerTrainSchedWidget(2087219) #Using Bruce Wayne to Test Widget as standalone
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
