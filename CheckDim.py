import numpy as np

import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from window import Ui_MainWindow




class Editor(QtGui.QMainWindow,QtGui.QWidget):

    def __init__(self, app):

        super(Editor, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.launch)
        self.ui.pushButton_2.clicked.connect(self.makeInput)

        self.ui.pushButton_2.setVisible(False)

        self.outputdim = np.zeros(4)

        # Variables UI
        self.show()
        self.app = app



    def launch(self) :

        inputdim = [self.ui.spinBox.value(),self.ui.spinBox_2.value(),self.ui.spinBox_3.value()]
        stride = [self.ui.spinBox_4.value(),self.ui.spinBox_5.value()]
        weight = [self.ui.spinBox_6.value(),self.ui.spinBox_7.value(),self.ui.spinBox_8.value(),self.ui.spinBox_9.value()]


        print("*"*50)
        print("Layer of input : " + str(inputdim))

        if (self.ui.radioButton.isChecked()) : 
            pad = 1 # SAME
        else :
            pad = 0 # VALID


        if ((inputdim[0] - weight[0] + pad)%stride[0]!=0):
            print("Error dimension 1")
        self.outputdim[0] = (inputdim[0] - weight[0]+ pad)/stride[0] + 1

        if ((inputdim[1] - weight[1]+ pad)%stride[1]!=0):
            print("Error dimension 2")
        self.outputdim[1] = (inputdim[1] - weight[1]+ pad)/stride[1] + 1

        if (inputdim[2]!=weight[2]) : 
            print("Error dimension 3")
        self.outputdim[2] = weight[3]


        self.ui.Result.setText("[" + str(int(self.outputdim[0])) + ", " + str(int(self.outputdim[1])) + ", " + str(int(self.outputdim[2])) + "]")
		
        self.ui.pushButton_2.setVisible(True)


    def makeInput(self) : 

        self.ui.spinBox.setValue(self.outputdim[0])
        self.ui.spinBox_2.setValue(self.outputdim[1])
        self.ui.spinBox_3.setValue(self.outputdim[2])

        self.ui.pushButton_2.setVisible(False)
        



def main():
    
    QtGui.QApplication.setStyle("windowsvista")
    app = QtGui.QApplication(sys.argv)
    ex = Editor(app)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

