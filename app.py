import sys
from PyQt5.QtWidgets import QApplication, QListView


from CompletorModel import CompletorModel
from QCompletorView import QCompletorView


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
'''
l = QCompletorView()
model = CompletorModel()
model.list_predictions = ['b', 'a', 'c']
model.fill_list_model()

l.show_list_predictions2(model)

app.exec_()

