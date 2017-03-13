import QtQuick 2.5
import QtQuick.Controls 1.4

Item {
    id: mainMenu

    property MenuBar menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            MenuItem { action: MainActions.mainActions.connectAction }
            MenuItem { action: MainActions.quitAction }
        }
        Menu {
            title: qsTr("&Jira")
            MenuItem { action: MainActions.goAction }
        }
        Menu {
            title: qsTr("&Help")
            MenuItem { action: MainActions.aboutAction }
        }
    }
}
