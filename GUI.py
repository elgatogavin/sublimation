from PyQt5.QtWidgets import QApplication, QWidget

application = QApplication([])
mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Hello World')
mainWindow.show()

application.exec()