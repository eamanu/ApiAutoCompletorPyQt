from PyQt5.QtGui import QStandardItem


class ItemCompletor(QStandardItem):
    def __init__(self, parent=None):
        super(ItemCompletor, self).__init__(parent)

    @property
    def line(self):
        return self._line

    @line.setter
    def line(self, l):
        self._line = l
        self.setText(l)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon):
        self._line = icon
        self.setIcon(icon)
