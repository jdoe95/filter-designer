from PySide2.QtWidgets import (
    QMenuBar,
    QMenu,
)



def _create_file_menu(menubar, actions):
    menu = QMenu('&File', parent=menubar)

    for action in (actions.new, actions.open):
        menu.addAction(action)

    menu.addSeparator()

    for action in (actions.save, actions.save_as, actions.close):
        menu.addAction(action)

    menu.addSeparator()
    menu.addAction(actions.quit)
    return menu



def _create_help_menu(menubar, actions):
    menu = QMenu('&Help', parent=menubar)

    menu.addAction(actions.help_contents)
    menu.addSeparator()
    menu.addAction(actions.help_about)
    return menu



def create_menubar(main_window, actions):
    menubar = QMenuBar(main_window)

    for menu_func in (_create_file_menu, _create_help_menu):
        menu = menu_func(menubar, actions)
        menubar.addAction(menu.menuAction())

    return menubar

