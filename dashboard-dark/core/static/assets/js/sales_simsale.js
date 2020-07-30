
<!--데이터 수정 -->
var list = salesList.replace(/&#39;/g, "\"");

<!-- 수정된 데이터 배열에 담기 -->
var data = JSON.parse(list);

// 카테고리 매출 //
var sim_cate_sales = document.getElementById('sim_cate_sales').getContext('2d');
var sim_cate_sales_beauty       = Object.values(data[1]).splice(1,11);
var sim_cate_sales_housekeeping = Object.values(data[2]).splice(1,11);
var sim_cate_sales_fashion      = Object.values(data[3]).splice(1,11);
var sim_cate_sales_food         = Object.values(data[4]).splice(1,11);


// 주문금액 //
var sim_user_sales    = document.getElementById('sim_user_sales').getContext('2d');
var unmmbr_ordr_ammnt = Object.values(data[5]).splice(1,11);
var mmbr_ordr_ammnt   = Object.values(data[6]).splice(1,11);


// 수익 및 결제수수료 //
var sim_income  = document.getElementById('sim_income').getContext('2d');
var net_profit  = Object.values(data[8]).splice(1,11);
var payment_fee = Object.values(data[7]).splice(1,11);


// 주문건수 //
var order_cnt  = document.getElementById('order_cnt').getContext('2d');
var unmmbr_cnt = Object.values(data[9]).splice(1,11);
var mmbr_cnt   = Object.values(data[10]).splice(1,11);


// 쿠폰 사용금액 //
var copn_use_amnt = document.getElementById('copn_use_amnt').getContext('2d');
var copn_amnt     = Object.values(data[11]).splice(1,11);

// 쿠폰 사용비율 //
var copn_use_rate = document.getElementById('copn_use_rate').getContext('2d');
var copn_whol_cnt     = Object.values(data[12]).splice(1,11);
var copn_use_psbl_cnt = Object.values(data[13]).splice(1,11);
var copn_use_cnt      = Object.values(data[14]).splice(1,11);

// 첫구매 비율 및 지표 없애기 모드
var frst_buy_rate  = document.getElementById('frst_buy_rate').getContext('2d');
var myLegendContainer = document.getElementById("myChartLegend");

var tday_join_buy_cnt = Object.values(data[15]).splice(1,11); // 당일가입구매자수
var tday_join_cnt          = Object.values(data[16]).splice(1,11); // 당일가입자수
var tday_buy_mmbr_cnt      = Object.values(data[17]).splice(1,11); // 당일구매회원수
var frst_buy_mmbr_cnt      = Object.values(data[18]).splice(1,11); // 첫구매회원수



/////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////// 객체 ///////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////

/*
$.ajax({
        url: "/rest/1/pages/245", // 클라이언트가 HTTP 요청을 보낼 서버의 URL 주소
        data: { name: "홍길동" }, // HTTP 요청과 함께 서버로 보낼 데이터
        method: "GET", // HTTP 요청 메소드(GET, POST 등)
        dataType: "json" // 서버에서 보내줄 데이터/의
     })

      var labels[10];

      for(var i=0; i<10; i++) {
        labels[i] = response.label[i];
      }

*/


// 카테고리 매출 //
var mySim_cate_sales = new Chart(sim_cate_sales, {
    type: 'line',
    data: {
        labels: ["10일전", "9일전", "8일전", "7일전", "6일전", "5일전", "4일전", "3일전", "2일전", "1일전"],
        datasets: [{
            label: "뷰티",
            borderColor: "#bd24d1",
            pointBorderColor: "#FFF",
            pointBackgroundColor: "#bd24d1",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [sim_cate_sales_beauty[10],sim_cate_sales_beauty[9],sim_cate_sales_beauty[8],sim_cate_sales_beauty[7],sim_cate_sales_beauty[6]
                  ,sim_cate_sales_beauty[5],sim_cate_sales_beauty[4],sim_cate_sales_beauty[3],sim_cate_sales_beauty[2],sim_cate_sales_beauty[1]]
        }, {
            label: "살림",
            borderColor: "#2486d1",
            pointBorderColor: "#FFF",
            pointBackgroundColor: "#2486d1",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [sim_cate_sales_housekeeping[10],sim_cate_sales_housekeeping[9],sim_cate_sales_housekeeping[8],sim_cate_sales_housekeeping[7],sim_cate_sales_housekeeping[6]
                  ,sim_cate_sales_housekeeping[5],sim_cate_sales_housekeeping[4],sim_cate_sales_housekeeping[3],sim_cate_sales_housekeeping[2],sim_cate_sales_housekeeping[1]]
        }, {
            label: "패션",
            borderColor: "#d12444",
            pointBorderColor: "#FFF",
            pointBackgroundColor: "#d12444",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [sim_cate_sales_fashion[10],sim_cate_sales_fashion[9],sim_cate_sales_fashion[8],sim_cate_sales_fashion[7],sim_cate_sales_fashion[6]
                  ,sim_cate_sales_fashion[5],sim_cate_sales_fashion[4],sim_cate_sales_fashion[3],sim_cate_sales_fashion[2],sim_cate_sales_fashion[1]]
        }, {
            label: "푸드",
            borderColor: "#3ed124",
            pointBorderColor: "#FFF",
            pointBackgroundColor: "#3ed124",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [sim_cate_sales_food[10],sim_cate_sales_food[9],sim_cate_sales_food[8],sim_cate_sales_food[7],sim_cate_sales_food[6]
                  ,sim_cate_sales_food[5],sim_cate_sales_food[4],sim_cate_sales_food[3],sim_cate_sales_food[2],sim_cate_sales_food[1]]
        }]
    },
    options : {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            position: 'top',
        },
        scales: ygraph_func,
        tooltips: {
            bodySpacing: 4,
            mode:"nearest",
            intersect: 0,
            position:"nearest",
            xPadding:10,
            yPadding:10,
            caretPadding:10,
            callbacks: xgraph_func
        },
        layout:{
            padding:{left:1,right:15,top:1,bottom:1}
        }

    }
});


// 수익 및 결제 수수료 //
var mySim_income = new Chart(sim_income, {
    type: 'line',
    data: {
        labels: ["10일전", "9일전", "8일전", "7일전", "6일전", "5일전", "4일전", "3일전", "2일전", "1일전"],
        datasets: [{
            label: "순수익",
            borderColor: prft_amnt,
            pointBorderColor: "#FFF",
            pointBackgroundColor: prft_amnt,
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [net_profit[10],net_profit[9],net_profit[8],net_profit[7],net_profit[6]
                  ,net_profit[5],net_profit[4],net_profit[3],net_profit[2],net_profit[1]]
        }, {
            label: "결제수수료",
            borderColor: use_ammnt,
            pointBorderColor: "#FFF",
            pointBackgroundColor: use_ammnt,
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [payment_fee[10],payment_fee[9],payment_fee[8],payment_fee[7],payment_fee[6]
                  ,payment_fee[5],payment_fee[4],payment_fee[3],payment_fee[2],payment_fee[1]]
        }]
    },
    options : {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            position: 'top',
        },
        scales: ygraph_func,
        tooltips: {
            bodySpacing: 4,
            mode:"nearest",
            intersect: 0,
            position:"nearest",
            xPadding:10,
            yPadding:10,
            caretPadding:10,
            callbacks: xgraph_func
        },
        layout:{
            padding:{left:1,right:15,top:1,bottom:1}
        }

    }
});


// 주문금액 //
var mySim_user_sales = new Chart(sim_user_sales, {
    type: 'line',
    data: {
        labels: ["10일전", "9일전", "8일전", "7일전", "6일전", "5일전", "4일전", "3일전", "2일전", "1일전"],
        datasets: [{
            label: "회원",
            borderColor: mmbr_color,
            pointBorderColor: "#FFF",
            pointBackgroundColor: mmbr_color,
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [mmbr_ordr_ammnt[10],mmbr_ordr_ammnt[9],mmbr_ordr_ammnt[8],mmbr_ordr_ammnt[7],mmbr_ordr_ammnt[6]
                  ,mmbr_ordr_ammnt[5],mmbr_ordr_ammnt[4],mmbr_ordr_ammnt[3],mmbr_ordr_ammnt[2],mmbr_ordr_ammnt[1]]
        }, {
            label: "비회원",
            borderColor: unmmbr_color,
            pointBorderColor: "#FFF",
            pointBackgroundColor: unmmbr_color,
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [unmmbr_ordr_ammnt[10],unmmbr_ordr_ammnt[9],unmmbr_ordr_ammnt[8],unmmbr_ordr_ammnt[7],unmmbr_ordr_ammnt[6]
                  ,unmmbr_ordr_ammnt[5],unmmbr_ordr_ammnt[4],unmmbr_ordr_ammnt[3],unmmbr_ordr_ammnt[2],unmmbr_ordr_ammnt[1]]
        }]
    },
    options : {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            position: 'top',
        },
        scales: ygraph_func,
        tooltips: {
            bodySpacing: 4,
            mode:"nearest",
            intersect: 0,
            position:"nearest",
            xPadding:10,
            yPadding:10,
            caretPadding:10,
            callbacks: xgraph_func
        },
        layout:{
            padding:{left:1,right:15,top:1,bottom:1}
        }

    }
});


// 주문건수 //
var myOrder_cnt = new Chart(order_cnt, {
    type: 'bar',
    data: {
        labels: ["10일전", "9일전", "8일전", "7일전", "6일전", "5일전", "4일전", "3일전", "2일전", "1일전"],
        datasets : [{
            label: "회원",
            backgroundColor: mmbr_color,
            borderColor: mmbr_color,
            data: [mmbr_cnt[10],mmbr_cnt[9],mmbr_cnt[8],mmbr_cnt[7],mmbr_cnt[6]
                  ,mmbr_cnt[5],mmbr_cnt[4],mmbr_cnt[3],mmbr_cnt[2],mmbr_cnt[1]],
        }, {
            label: "비회원",
            backgroundColor: unmmbr_color,
            borderColor: unmmbr_color,
            data: [unmmbr_cnt[10],unmmbr_cnt[9],unmmbr_cnt[8],unmmbr_cnt[7],unmmbr_cnt[6]
                  ,unmmbr_cnt[5],unmmbr_cnt[4],unmmbr_cnt[3],unmmbr_cnt[2],unmmbr_cnt[1]],
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {position : 'top'},
        <!--title: {display: true,text: '가입자수'},-->
        tooltips: {mode: 'index',intersect: true},
        scales: ygraph_func
    }
});


// 쿠폰 사용금액 //
var myCopn_use_amnt = new Chart(copn_use_amnt, {
    type: 'bar',
    data: {
        labels: ["10일전", "9일전", "8일전", "7일전", "6일전", "5일전", "4일전", "3일전", "2일전", "1일전"],
        datasets : [{
            label: "쿠폰사용금액",
            backgroundColor: use_ammnt,
            borderColor: use_ammnt,
            data: [copn_amnt[10],copn_amnt[9],copn_amnt[8],copn_amnt[7],copn_amnt[6]
                  ,copn_amnt[5],copn_amnt[4],copn_amnt[3],copn_amnt[2],copn_amnt[1]
                  ],
        }],
    },
    options: {
        <!-- title: {display: true,text: '가입자수'},-->
        responsive: true, maintainAspectRatio: false, legend: {position : 'bottom'},
        legend: {
            position: 'top',
        },
        tooltips:
        {
            mode: 'index',
            intersect: false,
            callbacks: xgraph_func
        },
        responsive: true,
        scales: ygraph_func


    }
});

// 쿠폰 사용비율 //
var myCopn_use_rate = new Chart(copn_use_rate, {
        type: 'pie',
        data: {
            datasets: [{
                data: [copn_use_cnt[1], copn_use_psbl_cnt[1]],
                backgroundColor :[use_ammnt,prft_amnt],
                borderWidth: 0
            }],
            labels: ['사용', '미사용']
        },
        options : {
            responsive: true,
            maintainAspectRatio: false,
            legend: {
                position : 'bottom',
                labels : {
                    fontColor: 'rgb(154, 154, 154)',
                    fontSize: 11,
                    usePointStyle : true,
                    padding: 20
                }
            },
            pieceLabel: {
                render: 'percentage',
                fontColor: 'white',
                fontSize: 14,
            },
            tooltips: false,
            layout: {
                padding: {
                    left: 20,
                    right: 20,
                    top: 20,
                    bottom: 20
                }
            }
        }
    })

// 첫구매 비율
// Chart with HTML Legends

var gradientStroke = frst_buy_rate.createLinearGradient(500, 0, 100, 0);
gradientStroke.addColorStop(0, '#177dff');
gradientStroke.addColorStop(1, '#80b6f4');

var gradientFill = frst_buy_rate.createLinearGradient(500, 0, 100, 0);
gradientFill.addColorStop(0, "rgba(23, 125, 255, 0.7)");
gradientFill.addColorStop(1, "rgba(128, 182, 244, 0.3)");

var gradientStroke2 = frst_buy_rate.createLinearGradient(500, 0, 100, 0);
gradientStroke2.addColorStop(0, '#f3545d');
gradientStroke2.addColorStop(1, '#ff8990');

var gradientFill2 = frst_buy_rate.createLinearGradient(500, 0, 100, 0);
gradientFill2.addColorStop(0, "rgba(243, 84, 93, 0.7)");
gradientFill2.addColorStop(1, "rgba(255, 137, 144, 0.3)");

var myFrst_buy_rate = new Chart(frst_buy_rate, {
    type: 'line',
    data: {
        labels: ["10일전", "9일전", "8일전", "7일전", "6일전", "5일전", "4일전", "3일전", "2일전", "1일전"],
        datasets: [ {
            label: "회원 중 첫 구매 비율",
            borderColor: gradientStroke2,
            pointBackgroundColor: gradientStroke2,
            pointRadius: 1,
            backgroundColor: gradientFill2,
            fill: true,
            borderWidth: 1,
            data: [Math.round((frst_buy_mmbr_cnt[10] / tday_buy_mmbr_cnt[10] * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[9]  / tday_buy_mmbr_cnt[9]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[8]  / tday_buy_mmbr_cnt[8]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[7]  / tday_buy_mmbr_cnt[7]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[6]  / tday_buy_mmbr_cnt[6]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[5]  / tday_buy_mmbr_cnt[5]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[4]  / tday_buy_mmbr_cnt[4]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[3]  / tday_buy_mmbr_cnt[3]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[2]  / tday_buy_mmbr_cnt[2]  * 100) * 100) / 100
                  ,Math.round((frst_buy_mmbr_cnt[1]  / tday_buy_mmbr_cnt[1]  * 100) * 100) / 100
                  ]

        }, {
            label: "가입일 구매 인원 비율",
            borderColor: gradientStroke,
            pointBackgroundColor: gradientStroke,
            pointRadius: 1,
            backgroundColor: gradientFill,
            fill: true,
            borderWidth: 1,
            data: [Math.round((tday_join_buy_cnt[10] / tday_join_cnt[10] * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[9]  / tday_join_cnt[9]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[8]  / tday_join_cnt[8]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[7]  / tday_join_cnt[7]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[6]  / tday_join_cnt[6]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[5]  / tday_join_cnt[5]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[4]  / tday_join_cnt[4]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[3]  / tday_join_cnt[3]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[2]  / tday_join_cnt[2]  * 100) * 100) / 100
                  ,Math.round((tday_join_buy_cnt[1]  / tday_join_cnt[1]  * 100) * 100) / 100
                  ]
        }]
    },
    options : {
        responsive: true,
        maintainAspectRatio: false, // 비율 유지
        legend: {
            position: 'top'
        },
        scales: ygraph_func,
        tooltips: {
            bodySpacing: 4,
            mode:"nearest",
            intersect: 0,
            position:"nearest",
            xPadding:10,
            yPadding:10,
            caretPadding:10,
            callbacks: xgraph_func
        },
        layout:{
            padding:{left:15,right:15,top:1,bottom:1}
        }


    }
});

