from PyQt5 import Qt


def create_qt_button(icon, callback, title=""):
    button = Qt.QPushButton(title)
    button.setIcon(icon)
    button.pressed.connect(callback)
    return button
