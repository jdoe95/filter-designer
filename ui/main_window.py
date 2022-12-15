from PySide2.QtWidgets import (
    QMainWindow,
    QStatusBar,

)
from .actions import create_actions
from .menus import create_menubar
from .workspace_area import WorkspaceArea

_title = 'Filter Designer'
_minimum_size = (800, 600)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(_title)
        self.setMinimumSize(*_minimum_size)

        actions = create_actions(self)

        # Connect actions to slots
        action_slots = {
            # source: destination
            actions.quit.triggered: self.close
        }
        for action, slot in action_slots.items():
            action.connect(slot)

        menubar = create_menubar(self, actions)
        self.setMenuBar(menubar)

        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)

        workspaceArea = WorkspaceArea(self)
        self.setCentralWidget(workspaceArea)










