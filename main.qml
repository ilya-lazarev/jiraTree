import QtQuick 2.0
import QtQuick.Layouts 1.3
import QtQuick.Window 2.2
import QtQuick.Extras 1.4
import QtQuick.Controls 2.0
import QtQuick.Controls.Universal 2.0

Pane {
    id: mainItem
    bottomPadding: 6
    rightPadding: 6
    leftPadding: 6
    topPadding: 6
    spacing: 4
    ColumnLayout {
        id: columnLayout1
        anchors.fill: parent


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
            anchors.top: parent.top
            anchors.topMargin: 0

            Text {
                id: idLabel
                text: qsTr("Issue ID")
                font.bold: true
                anchors.leftMargin: 20
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 12
            }

            TextEdit {
                focus: true
                id: idInput
                width: 300
                height: 17
                text: qsTr("PSADEV-596")
                anchors.verticalCenter: parent.verticalCenter
                font.pixelSize: 12
            }

            Button {
                id: bGo
                objectName: 'bGo'
                width: 64
                height: 32
                text: qsTr("Go")
                autoExclusive: false
                highlighted: false
                anchors.leftMargin: 20
                anchors.verticalCenter: idInput.verticalCenter
            }
        }
        Row {
            id: row2
            anchors.top: row1.bottom
            anchors.right: parent.right
            anchors.bottom: parent.bottom
            anchors.left: parent.left
            anchors.topMargin: 0
        }
    }
}
