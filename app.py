import sys
from PyQt5.QtWidgets import QApplication, QListView

# from CompletorModel import CompletorModel
# from QCompletorView import QCompletorView
from ApiAutoCompletorPyQt import *
from ApiAutoCompletorPyQt.QCompletorView import QCompletorView

app = QApplication(sys.argv)
'''
list = QListView()
list.setWindowTitle('Example')
list.setMinimumSize(600, 400)

model = CompletorModel()
model.addLinePrediction('a')
model.addLinePrediction('b')

list.setModel(model)
list.show()

l = QCompletorView()
model = CompletorModel()
model.list_predictions = ['b', 'a', 'c']
model.fill_list_model()

l.show_list_predictions2(model)
'''
ll = QCompletorView()
Model.list_predictions = ['b', 'a', 'c']
Model.fill_list_model()

ll.show_list_predictions2(Model)

app.exec_()

