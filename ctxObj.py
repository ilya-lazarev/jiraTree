import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import *


class MyClass(QObject):
    changeText = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_obj = MyClass()

    timer = QTimer()
    timer.start(2000)

    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()
    ctx.setContextProperty("my_obj", my_obj)
    engine.load('ctxObj.qml')
    root = engine.rootObjects()[0]
    timer.timeout.connect(root.setText)
    sys.exit(app.exec_())