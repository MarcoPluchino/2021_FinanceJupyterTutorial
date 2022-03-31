
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Gui():
    '''
    Main Graphical User Interface
    '''
    
    def __init__(self,show=False,dict = {},user='developer',verbose=False):
        print(f"Class gui(show = {show}, dict = ..., user = {user})\n ")
        self.swc = dict
        if show:
            print("TODO")
            from . import ui_gui
    #         app = QtWidgets.QApplication(sys.argv)
    #         MainWindow = QtWidgets.QMainWindow()  
    #         self.ui = ui_gui.Ui_MainWindow()
    #         self.ui.setupUi(MainWindow)
    #         self.CustomizeUI()
    #         MainWindow.show()
    #         sys.exit(app.exec_())
        
    # def CustomizeUI(self):
    #     '''
    #     Customize GUI
    #     '''
    #     # Init 
    #     swc = self.swc
    #     row_swc = (lambda sheet,column,row: (swc[sheet][swc[sheet][column] == row])) # return all row
        
    #     # TOOLBAR
    #     ## Build .bat

    #     self.ui.actionBuild.triggered.connect(self.OnBuild)


    # # FUNCTION ACTIONS
    # def OnBuild(self):
    #     print("TODO")
    #     # self.ui.statusbar.showMessage("Build Project...")
    #     # dirname,basename = os.path.split(self.compile_project_file) 
    #     # self.ui.statusbar.showMessage("OK...")
    # def OnFlash(self):
    #     print("TODO")

    # def OnInfo(self):
    #     print("TODO")
    # def OnSWC():
    #     print("TODO")

    # def ToDo(self):
    #     # https://coderslegacy.com/python/pyqt5-qmessagebox/
    #     msgBox = QMessageBox()
    #     msgBox.setIcon(QMessageBox.Information) #Icon { NoIcon, Question, Information, Warning, Critical }
    #     msgBox.setText("To do text")
    #     msgBox.setWindowTitle("To do title")
    #     msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msgBox.setDefaultButton(QMessageBox.Cancel)
    #     msgBox.exec_()
    #     if msgBox.clickedButton() is msgBox.button(QMessageBox.Ok):
    #         print("Yes button clicked")
    #     else:
    #         print("Cancel")
    #     self.ui.statusbar.showMessage(f"To Do")