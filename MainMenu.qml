import QtQuick.Controls 1.4

MenuBar {
        Menu {
            title: qsTr("&File")
            MenuItem { action: quitAction }
        }
        Menu {
            title: qsTr("&Edit")
        }
        Menu {
            title: qsTr("&Jira")
        }
        Menu {
            title: qsTr("&Help")
        }
}
