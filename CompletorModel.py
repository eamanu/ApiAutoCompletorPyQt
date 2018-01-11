from PyQt5.QtCore import (
    Qt,
    QVariant
)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import QModelIndex

from ItemCompletor import ItemCompletor


class CompletorModel(QStandardItemModel):
    def __init__(self, parent=None):
        super(CompletorModel, self).__init__(parent)
        self.___text_script_complete = ''
        self.___line_editor = 0
        self.___column_editor = 0
        self.___list_pred_position = None
        self.___list_predictions = list
        self.___language = None

    # Save the complete Script
    @property
    def text_script_complete(self):
        return self.___text_script_complete

    @text_script_complete.setter
    def text_script_complete(self, script):
        self.___text_script_complete = script

    # Save the actual line number
    @property
    def line_editor(self):
        return self.___line_editor

    @line_editor.setter
    def line_editor(self, line):
        self.___line_editor = line

    # Save the actual column number
    @property
    def column_editor(self):
        return self.___column_editor

    @column_editor.setter
    def column_editor(self, column):
        self.___column_editor = column

    # Save the language of the script
    @property
    def language(self):
        return self.___language

    @language.setter
    def language(self, lang):
        self.___language = lang

    # Positions from the editor
    @property
    def list_pred_position(self):
        return self.___list_pred_position

    @list_pred_position.setter
    def list_pred_position(self, qpoint):
        self.___list_pred_position = qpoint

    # Lis of predictions
    @property
    def list_predictions(self):
        return self.___list_predictions

    @list_predictions.setter
    def list_predictions(self, l_predictions):
        self.___list_predictions = l_predictions

    def _add_line_prediction(self, prediction):
        ic = ItemCompletor()
        ic.line = prediction
        self.appendRow(ic)

    def row_count(self, parent=QModelIndex()):
        return False  # TODO

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or \
           not 0 <= index.row() < self.rowCount():
            return QVariant()

        row = index.row()
        if role == Qt.DisplayRole:
            return str(self.___list_predictions[row])
        return QVariant()

    def give_count_list_predictions(self):
        return len(self.___list_pred_position)

    def fill_list_model(self):
        for item in self.___list_predictions:
            self._add_line_prediction(item)
