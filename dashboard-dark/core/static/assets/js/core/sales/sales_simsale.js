
<!--데이터 수정 -->
var list = salesList.replace(/&#39;/g, "\"");

<!-- 수정된 데이터 배열에 담기 -->
var data = JSON.parse(list);

////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

// 카테고리 매출 //
var sim_cate_sales = document.getElementById('sim_cate_sales').getContext('2d');
var sim_cate_sales_beauty       = Object.values(data[1]).splice(2,11);
var sim_cate_sales_housekeeping = Object.values(data[2]).splice(2,11);
var sim_cate_sales_fashion      = Object.values(data[3]).splice(2,11);
var sim_cate_sales_food         = Object.values(data[4]).splice(2,11);

//console.log(data_list(sim_cate_sales_beauty));
//console.log(typeof(data_list(sim_cate_sales_beauty)));

// 주문금액 //
var sim_user_sales    = document.getElementById('sim_user_sales').getContext('2d');
var unmmbr_ordr_ammnt = Object.values(data[5]).splice(2,11);
var mmbr_ordr_ammnt   = Object.values(data[6]).splice(2,11);


// 수익 및 결제수수료 //
var sim_income  = document.getElementById('sim_income').getContext('2d');
var net_profit  = Object.values(data[8]).splice(2,11);
var payment_fee = Object.values(data[7]).splice(2,11);


// 주문건수 //
var order_cnt  = document.getElementById('order_cnt').getContext('2d');
var unmmbr_cnt = Object.values(data[9]).splice(2,11);
var mmbr_cnt   = Object.values(data[10]).splice(2,11);


// 쿠폰 사용금액 //
var copn_use_amnt = document.getElementById('copn_use_amnt').getContext('2d');
var copn_amnt     = Object.values(data[11]).splice(2,11);

// 쿠폰 사용비율 //
var copn_use_rate     = document.getElementById('copn_use_rate').getContext('2d');
var copn_whol_cnt     = Object.values(data[12]).splice(2,11);
var copn_use_psbl_cnt = Object.values(data[13]).splice(2,11);
var copn_use_cnt      = Object.values(data[14]).splice(2,11);

// 첫구매 비율 및 지표 없애기 모드
var frst_buy_rate     = document.getElementById('frst_buy_rate').getContext('2d');
var tday_join_buy_cnt      = Object.values(data[15]).splice(1,11); // 당일가입구매자수
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

// 재호씨가 준거
function callAjax(url,data,callbackFunc){
	$.extend(data,data,{path : window.location.pathname});
	$.ajax({
		type : "POST",
		url : window.location.origin + "/JasonDA" + url,
		data : JSON.stringify(data),
		dataType : "json",
		contentType : "application/json",
		beforeSend : function(){
			$(".wrap_loading").show();
		},
		error : function(err){
			console.log(err);
		},
		success : function(result){
			if(result.status){
				if(callbackFunc){
					callbackFunc(result);
					$(".wrap_loading").hide();
				}
			}else{
				alert("오류가 발생하였습니다.\n오류코드 : "+result.errCode+"\n");
				$(".wrap_loading").hide();
			}
		}
	});
}



*/


// 카테고리 매출 //
var mySim_cate_sales = new Chart(sim_cate_sales, {
    type: 'line',
    data: {
        labels: labels_10,
        datasets: [
        {
            label: "뷰티",
            borderColor: "#bd24d1",
            pointBackgroundColor: "#bd24d1",
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: sim_cate_sales_beauty.reverse()
        }, {
            label: "살림",
            borderColor: "#2486d1",
            pointBackgroundColor: "#2486d1",
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: sim_cate_sales_housekeeping.reverse()
        }, {
            label: "패션",
            borderColor: "#d12444",
            pointBackgroundColor: "#d12444",
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: sim_cate_sales_fashion.reverse()
        }, {
            label: "푸드",
            borderColor: "#3ed124",
            pointBackgroundColor: "#3ed124",
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: sim_cate_sales_food.reverse()
        }]
    },
    options : {
        responsive: true,
        maintainAspectRatio: false,
        legend: legend_top,
        scales: ygraph_func,
        tooltips: tooltips_line,
        layout: layout_all
    }
});


// 수익 및 결제 수수료 //
var mySim_income = new Chart(sim_income, {
    type: "bar", // 'bar'
    data: {
        labels: labels_10,
        datasets: [{
            label: "순수익",
            backgroundColor: prft_amnt,// "transparent" = 투명하게
            borderColor: prft_amnt,
            pointBackgroundColor: prft_amnt,
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            fill: true,
            borderWidth: 2,
            data: net_profit.reverse()
        }, {
            label: "결제수수료",
            backgroundColor: use_ammnt,
            borderColor: use_ammnt,
            pointBackgroundColor: use_ammnt,
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            fill: true,
            borderWidth: 2,
            data: payment_fee.reverse()
        }]
    },
    options : {
        maintainAspectRatio: false,
        legend: legend_top,
        scales: ygraph_func,
        tooltips: tooltips_line,
        layout: layout_all
    }
});


// 주문금액 //
var mySim_user_sales = new Chart(sim_user_sales, {
    type: 'line',
    data: {
        labels: labels_10,
        datasets: [{
            label: "회원",
            borderColor: mmbr_color,
            pointBackgroundColor: mmbr_color,
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: mmbr_ordr_ammnt.reverse()
        }, {
            label: "비회원",
            borderColor: unmmbr_color,
            pointBackgroundColor: unmmbr_color,
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: unmmbr_ordr_ammnt.reverse()
        }]
    },
    options : {
        maintainAspectRatio: false,
        legend: legend_top,
        scales: ygraph_func,
        tooltips: tooltips_line,
        layout: layout_all
    }
});


// 주문건수 //
var myOrder_cnt = new Chart(order_cnt, {
    type: 'bar',
    data: {
        labels: labels_10,
        datasets : [{
            label: "회원",
            backgroundColor: mmbr_color, // transparent
            borderColor: mmbr_color,
            pointBackgroundColor: prft_amnt,
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            fill: true,
            borderWidth: 2,
            data: mmbr_cnt.reverse()
        }, {
            label: "비회원",
            backgroundColor: unmmbr_color,
            borderColor: unmmbr_color,
            pointBackgroundColor: unmmbr_color,
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            fill: true,
            borderWidth: 2,
            data: unmmbr_cnt.reverse()
        }],
    },
    options: {
        maintainAspectRatio: false, // 크기가 커져도 크기 맞추기
        legend: legend_top,
        scales: ygraph_func,
        tooltips: tooltips_line,
        layout: layout_all
    }
});


// 쿠폰 사용금액 //
var myCopn_use_amnt = new Chart(copn_use_amnt, {
    type: 'horizontalBar',
    data: {
        labels: labels_10,
        datasets : [{
            label: "쿠폰사용금액",
            backgroundColor: use_ammnt, // transparent
            borderColor: use_ammnt,
            pointBackgroundColor: use_ammnt,
            pointBorderColor: "#FFF",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            fill: true,
            borderWidth: 2,
            data: copn_amnt.reverse()
        }],
    },
    options: {
        maintainAspectRatio: false,
        legend: legend_top,
        scales: ygraph_func,
        tooltips: tooltips_line,
        layout: layout_all
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
            tooltips: {callbacks: xgraph_func},
            layout: layout_all
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
        labels: labels_10,
        datasets: [ {
            label: "회원 중 첫 구매 비율",
            borderColor: gradientStroke2,
            pointBackgroundColor: gradientStroke2,
            backgroundColor: gradientFill2,
            pointRadius: 1,
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
            backgroundColor: gradientFill,
            pointRadius: 1,
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
        maintainAspectRatio: false, // 비율 유지
        legend: legend_top,
        scales: ygraph_func,
        tooltips: tooltips_line,
        layout: layout_all
    }
});

