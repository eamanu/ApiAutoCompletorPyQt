from PyQt5.QtWidgets import QListView


class QCompletorView(QListView):
    def __init__(self, parent=None):
        super(QCompletorView, self).__init__(parent)

    def set_model(self, model):
        self.setModel(model)

    def show_list_predictions2(self, model):
        self.set_model(model)
        self.hide()
        self.show()

    def show_list_predictions(self, model):
        self.set_model(model)
        self.hide()
        self.move(model.___list_pred_position)
        self.show()

    def hide_list_predictions(self):
        self.hide()

    def clear_list_predictiones(self):
        self.clear()


