from PySide2.QtWidgets import (
    QAction,
)
from PySide2.QtGui import (
    QIcon,
)
from types import SimpleNamespace


_labels = {
    'new'           : '&New',
    'open'          : '&Open',
    'save'          : '&Save',
    'save_as'       : 'Save &As',
    'close'         : '&Close',
    'quit'          : '&Quit',
    'help_contents' : '&Contents',
    'help_about'    : '&About',
}

_shortcuts = {
    'new'           : 'Ctrl+N',
    'open'          : 'Ctrl+O',
    'save'          : 'Ctrl+S',
    'save_as'       : 'Shift+Ctrl+S',
    'quit'          : 'Ctrl+F4',
    'help_contents' : 'F1',
}

_theme_icons = {
    'new'           : 'document-new',
    'open'          : 'document-open',
    'save'          : 'document-save',
    'save_as'       : 'document-save-as',
    'help_about'    : 'help-about',
    'help_contents' : 'help-contents',
    'quit'          : 'application-exit',
}


def create_actions(main_window):
    actions = SimpleNamespace()

    for name, label in _labels.items():
        action = QAction(label, parent=main_window)
        setattr(actions, name, action)

    for name, shortcut in _shortcuts.items():
        action = getattr(actions, name)
        action.setShortcut(shortcut)

    for name, icon_name in _theme_icons.items():
        action = getattr(actions, name)
        action.setIcon(QIcon.fromTheme(icon_name))

    return actions
