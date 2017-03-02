import QtQuick 2.0
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import QtQuick.Extras 1.4
import QtQuick.Controls 2.0
import QtQuick.Controls 1.4
import Qt.labs.folderlistmodel 2.1


Pane {
    id: mainPane
    anchors.fill: parent
    Action {
        id: connectAction
        text: qsTr("&Connect")
        shortcut: "Ctrl-N"
        iconName: "connect"
        iconSource: "img/connect.png"
        onTriggered: base.onConnect()
        tooltip: qsTr("Connect to JIRA server")
    }

    Action {
        id: quitAction
        text: qsTr("&Quit")
        shortcut: "Ctrl-Q"
        iconName: "exit"
        iconSource: "img/exit.png"
        onTriggered: base.onClose()
        tooltip: qsTr("Quits application")
    }
    Action {
        id: goAction
        text: qsTr("&Go")
        shortcut: "Ctrl-G"
        iconName: "go"
        iconSource: "img/go.svg"
        onTriggered: base.goHandler()
        tooltip: qsTr("Analyze the issue")
    }

    Action {
        id: aboutAction
        text: qsTr("&About")
        iconName: "about"
        iconSource: "img/about.png"
        onTriggered: base.onAbout()
        tooltip: qsTr("Shows About dialog")
    }
    property MenuBar mainMenuBar: MenuBar {
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

    ColumnLayout {
        id: column1
        anchors.fill: parent
        spacing: 12

        RowLayout {
            id: row2
            Layout.fillWidth: true

            spacing: 12
            Rectangle {
                color: "#ad4c4c"
                anchors.fill: parent
                height: parent.height
                width: 100
            }
            Rectangle {
                height: parent.height
                Layout.fillWidth: true
                anchors.fill: parent
                color: "#5a68cf"
            }
            //            SplitView {
            //                id: splitView1
            //                anchors.fill: parent


            //                TreeView {
            //                    id: treeItem
            //                    Layout.minimumWidth: 400
            //                    TableViewColumn {
            //                        title: "Name"
            //                        role: "fileName"
            //                        width: 300
            //                    }
            //                    TableViewColumn {
            //                        title: "Permissions"
            //                        role: "filePermissions"
            //                        width: 100
            //                    }
            //                    model: FolderListModel {
            //                        id: folderModel
            //                        nameFilters: ["*.*"]
            //                    }
        }
        RowLayout {
            id: row1
            Layout.fillWidth: true
            Layout.fillHeight: true
            spacing: 12
            //        anchors.right: parent.right
            //        anchors.rightMargin: 0
            //        anchors.left: parent.left
            anchors.leftMargin: 20
            //        anchors.topMargin: 0
            //            height: 24

            Text {
                id: idLabel
                text: qsTr("Issue ID")
                font.bold: true
                anchors.leftMargin: 20
                font.pixelSize: 12
            }

            TextField {
                id: idInput
                height: 24
                placeholderText: qsTr("PSADEV-?")
            }
            Button {
                id: bGo
                //                iconSource: uri('img/go.svg')
                width: 64
                height: 24
                action: goAction
                //                    text: qsTr("Go")
                anchors.leftMargin: 20
            }

        }

    }
    Component.onCompleted: {
        console.log(mainPane.mainMenuBar)
        base.setMenu(mainPane.mainMenuBar)
    }
}
