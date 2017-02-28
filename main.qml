import QtQuick 2.0
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import QtQuick.Extras 1.4
import QtQuick.Controls 1.4
import QtQuick.Controls 2.0

Column {
    id: column1
    anchors.fill: parent
    spacing: 4

    Row {
        id: row1
        //            height: 51
        Layout.columnSpan: 12
        Layout.rowSpan: 2
        spacing: 12
        anchors.right: parent.right
        anchors.rightMargin: 0
        anchors.left: parent.left
        anchors.leftMargin: 20
        anchors.topMargin: 0
        height: 24

        Text {
            id: idLabel
            text: qsTr("Issue ID")
            font.bold: true
            anchors.leftMargin: 20
            anchors.verticalCenter: parent.verticalCenter
            font.pixelSize: 12
        }

        TextField {
            id: idInput
            height: 24
            anchors.verticalCenter: parent.verticalCenter
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
            anchors.verticalCenter: idInput.verticalCenter
        }

    }

    Row {
        id: row2
        spacing: 12
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.bottom: parent.bottom

        SplitView {
            id: splitView1
            anchors.fill: parent

            TreeView {
                id: treeItem
                Layout.minimumWidth: 400
                TableViewColumn {
                    title: "Name"
                    role: "fileName"
                    width: 300
                }
                TableViewColumn {
                    title: "Permissions"
                    role: "filePermissions"
                    width: 100
                }
            }

            TextArea {
                text: qsTr("Example")
                id: propsItem
                Rectangle {
                    color: "red"
                    anchors.fill: parent

                }
            }
        }
    }
    Connections {
        target: bGo
        onClicked: print("clicked")
    }
}

