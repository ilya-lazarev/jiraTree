import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 2.0

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Shortcut {

    }

    Menu {
        title: qsTr("&File")
    }
    Menu {
        title: qsTr("&Edit")
    }
    Menu {
        title: qsTr("&J")
    }
    Menu {
        title: qsTr("&Help")
        MenuItem { text: qsTr("About")
        }

        MainForm {
            anchors.fill: parent
            mouseArea.onClicked: {
                Qt.quit();
            }
        }
    }
}
