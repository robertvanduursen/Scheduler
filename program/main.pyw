from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys, os, math

app = QtWidgets.QApplication(sys.argv)
# app.setStyle('Fusion')

nodeColours = {
    0: QtGui.QColor(0, 0, 220, 255),
    1: QtGui.QColor(220, 128, 0, 255),
    2: QtGui.QColor(220, 0, 220, 255),
    3: QtGui.QColor(220, 220, 0, 255),
    4: QtGui.QColor(100, 0, 0, 255),
    5: QtGui.QColor(100, 0, 100, 255),
    6: QtGui.QColor(100, 100, 0, 255),
    7: QtGui.QColor(100, 0, 255, 255),
    8: QtGui.QColor(100, 255, 0, 255),
}


def node_colour(nr):
    if nr in nodeColours.keys():
        return nodeColours[nr]
    return nodeColours[0]


root = os.path.dirname(__file__)
save_file = None


class CanvasModule(QtWidgets.QMainWindow):
    words = {}
    connections = {}

    filePath = False

    def __init__(self):
        super().__init__()

        self.ui = uic.loadUi(root + r"\canvas.ui", self)
        self.ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.treeWidget_init()

        self.setContentsMargins(10, 10, 10, 10)
        self.show()

        self.zoom = 100.0
        self.make_connections()

    def treeWidget_init(self):
        tw = self.treeWidget

        tw.setDragEnabled(True)
        tw.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        tw.setExpandsOnDoubleClick(False)

        self.setList = tw
        self.populate_treeWidget()

    def populate_treeWidget(self):
        """
        Refresh the setList widget with the vis set in scene
        :return:
        """
        # clear UI
        # self.setList.clear()
        for s in ['hey', 'you']:
            # append name to UI list
            # https://doc.qt.io/qt-5/qtreewidgetitem.html
            item = QtWidgets.QTreeWidgetItem(self.setList)
            item.setText(0, s)
            self.setList.addTopLevelItem(item)

    def make_connections(self):
        self.close_btn.pressed.connect(self.quit)

    def quit(self):
        print('exiting')
        print('saving')
        self.save()
        sys.exit()

    def save(self):
        f = QtCore.QFile("file.dat")
        f.open(QtCore.QIODevice.WriteOnly)

        # stream.writeQString()
        # l = QtWidgets.QTreeWidgetItem()
        print('selecting all')
        l = self.setList
        print('selecting ')
        l.selectAll()
        print('sel')
        stream = QtCore.QDataStream(f)

        print('saving in progress')
        for item in l.selectedItems():
            print(item)
            # stream << item
            item.write(stream)

            # self.copiedItem.clear()
            # self.pasteOffset = 5
            # stream = QtCore.QDataStream(self.copiedItem, QtCore.QIODevice.WriteOnly)
            # self.writeItemToStream(stream, item)


        print('saved')


        '''
        QFile file("file.dat");
        file.open(QIODevice::WriteOnly);
        QDataStream out(&file);   // we will serialize the data into the file
        out << QString("the answer is");   // serialize a string
        out << (qint32)42;        // serialize an integer

        :return:
        '''

    def clear_graph(self):
        self.scene.clear()

# todo: saving and loading


c = CanvasModule()

styleSheet = """
QMainWindow {
    background-color: #4e4e4e;
    color: #ffffff;
}

QPushButton {
    background-color: #4e4e4e;
    color: #ffffff;
}

QPushButton#enterStatement {
    background-color: #ffffff;
    color: #4e4e4e;
}
"""

app.setStyleSheet(styleSheet)

sys.exit(app.exec())
