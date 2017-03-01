import QtQuick 2.2
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.3

ApplicationWindow{

        visible:true
        width:940
        height:680

        id:root

        title: "markdwon editor"

        function setText()
        {
            exampleId.text = Math.random();
        }

        Rectangle{

            Text{
                id:exampleId
                text:"hello"
            }
        }
}
