////////////////////////////////////////////////////////
////////////////////////////////////////////////////////
var labels_10 = ["10일전", "9일전", "8일전", "7일전", "6일전", "5일전", "4일전", "3일전", "2일전", "1일전"];


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
                    else if(label > 1000)
                    {
                        return label/1000+',000';
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

          console.log(dataLabel);

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

// 옵션쪽

// 마우스 가져가 놓았을때 데이터 어떻게 나올지

var tooltips_line =
{
    bodySpacing: 4,
    mode:"nearest",
    intersect: 0,
    position:"nearest",
    xPadding:10,
    yPadding:10,
    caretPadding:10,
    callbacks: xgraph_func
};

// 화면크기
var layout_all =
{
    padding: {
        left: 1,
        right: 1,
        top: 1,
        bottom: 1
    }
};

// 그래프 목록 어디에 나타낼지
var legend_top =
{
    position: 'top' // bottom
};

