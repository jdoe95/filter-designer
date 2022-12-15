from PySide2.QtWidgets import (
    QWidget,
    QSplitter,
    QTreeView,
    QMdiArea,
)



class WorkspaceDocument(QWidget):
    def __init__(self, parent):
        super().__init__(parent)



class WorkspaceArea(QSplitter):
    def __init__(self, main_window):
        super().__init__(parent=main_window)

        treeView = QTreeView(self)
        treeView.setMinimumWidth(100)

        mdiArea = QMdiArea(self)

        self.addWidget(treeView)
        self.addWidget(mdiArea)






