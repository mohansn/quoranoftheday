function drawPieChart (piedata) 
{
    var chart = new d3pie ("chart", {
        size: {
            canvasHeight: 700,
            canvasWidth: 700
        },
        header: {
            title: {
                text: "Stats for Quorans of the Day"
            },
            subtitle: {
                text: "Click on any slice to see answers on that topic"
            }
        },
        data: {
            content: piedata
        },
        callbacks: {
            onClickSegment: function(a) {
                window.open (a.data.link);
            }
        }
    });
}
