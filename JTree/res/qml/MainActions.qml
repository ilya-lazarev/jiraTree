import QtQuick 2.7
import QtQuick.Controls 1.4

Item {
    id: mainActions

    property Action connectAction: Action {
        text: qsTr("&Connect")
        shortcut: "Ctrl-N"
        iconName: "connect"
        iconSource: "qrc:/res/img/connect.png"
        onTriggered: mainWindow.onConnect()
        tooltip: qsTr("Connect to JIRA server")
    }

    property Action quitAction: Action {
        text: qsTr("&Quit")
        shortcut: "Ctrl-Q"
        iconName: "exit"
        iconSource: "qrc:/res/img/exit.png"
        onTriggered: mainWindow.onClose()
        tooltip: qsTr("Quits application")
    }
    property Action goAction: Action {
        text: qsTr("&Go")
        shortcut: "Ctrl-G"
        iconName: "go"
        iconSource: "qrc:/res/img/go.svg"
        onTriggered: mainWindow.goHandler()
        tooltip: qsTr("Analyze the issue")
    }

    property Action aboutAction: Action {
        text: qsTr("&About")
        iconName: "about"
        iconSource: "qrc:/res/img/about.png"
        onTriggered: mainWindow.onAbout()
        tooltip: qsTr("Shows About dialog")
    }

}

