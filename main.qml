import QtQuick 2.0
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import QtQuick.Extras 1.4
import QtQuick.Controls 1.4
import QtQuick.Controls 2.0
import Qt.labs.folderlistmodel 2.1

Pane {
    id: pane1
    spacing: 12
    anchors.fill: parent

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
                //                    anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 12
            }

            TextField {
                id: idInput
                height: 24
                //                    anchors.verticalCenter: parent.verticalCenter
                placeholderText: qsTr("PSADEV-?")
            }
            Button {
                id: bGo
                objectName: 'bGo'
                //                iconSource: uri('img/go.svg')
                width: 64
                height: 24
                text: qsTr("Go")
                autoExclusive: false
                highlighted: false
                anchors.leftMargin: 20
                //                    anchors.verticalCenter: idInput.verticalCenter
            }

        }

    }

    Connections {
        target: bGo
        onClicked: console.log("clicked")
    }
}



