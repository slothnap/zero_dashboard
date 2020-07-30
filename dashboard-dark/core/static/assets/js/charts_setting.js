

    // y축 단위값 나타내기
var ygraph_func =
{
    yAxes:
    [
        {
            ticks:
            {
                beginAtZero: true, // y축 값 0부터 시작
                callback:
                function(label, index, labels)
                {
                    if(label > 100000000)
                    {
                        return label/100000000+',000만';
                    }
                    else if(label > 10000)
                    {
                        return label/10000+'만';
                    }
                    else
                        return label
                }
            },
            scaleLable:
            {
                display: true,
                labelString: '1k = 1000'
            }
        }
    ]
};

// x축 단위값 나타내기

var xgraph_func =
{
      label: function(tooltipItem, data)
      {
          console.log(data); //데이터 값 찾아보기

          var dataLabel = data.datasets[tooltipItem.datasetIndex].label;
          var value = ': ' + data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index].toLocaleString();

          //console.log(value);

          if (Chart.helpers.isArray(dataLabel))
          {

              dataLabel = dataLabel.slice();
              dataLabel[0] += value;

          }
          else
          {
              dataLabel += value;
          }

          return dataLabel;
      }
};