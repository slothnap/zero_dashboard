<!--데이터 수정 -->
var list = userList.replace(/&#39;/g, "\"");

<!-- 수정된 데이터 배열에 담기 -->
var data = JSON.parse(list);

console.log(data);


// 카테고리 매출 //
var mmbr_join_cnt = document.getElementById('mmbr_join_cnt').getContext('2d');
var day_join_naver  = Object.values(data[1]).splice(1,11);
var day_join_kakao  = Object.values(data[3]).splice(1,11);
var day_join_gnrl   = Object.values(data[2]).splice(1,11);


// 일일 접속자 //
var day_visit = document.getElementById('day_visit').getContext('2d');

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////// 객체 ///////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 카테고리 매출 //
var myMmbr_join_cnt = new Chart(mmbr_join_cnt, {
    type: 'bar',
    data: {
        labels: labels_10,
        datasets : [{
            label: "카카오",
            backgroundColor: '#59d05d',
            borderColor: '#59d05d',
            data: [day_join_kakao[10],day_join_kakao[9],day_join_kakao[8],day_join_kakao[7],day_join_kakao[6]
                  ,day_join_kakao[5],day_join_kakao[4],day_join_kakao[3],day_join_kakao[2],day_join_kakao[1]],
        },{
            label: "네이버",
            backgroundColor: '#fdaf4b',
            borderColor: '#fdaf4b',
            data: [day_join_naver[10],day_join_naver[9],day_join_naver[8],day_join_naver[7],day_join_naver[6]
                  ,day_join_naver[5],day_join_naver[4],day_join_naver[3],day_join_naver[2],day_join_naver[1]],
        }, {
            label: "일반",
            backgroundColor: '#177dff',
            borderColor: '#177dff',
            data: [day_join_gnrl[10],day_join_gnrl[9],day_join_gnrl[8],day_join_gnrl[7],day_join_gnrl[6]
                  ,day_join_gnrl[5],day_join_gnrl[4],day_join_gnrl[3],day_join_gnrl[2],day_join_gnrl[1]],
        }],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            position : 'bottom'
        },
        title: {
            display: true,
            text: 'Traffic Stats'
        },
        tooltips: {
            mode: 'index',
            intersect: false
        },
        responsive: true,
        scales: {
            xAxes: [{
                stacked: true,
            }],
            yAxes: [{
                stacked: true
            }]
        }
    }
});


// 일일 접속자 //
var myDay_visit = new Chart(day_visit, {
    type: 'line',
    data: {
        labels: labels_10,
        datasets: [{
            label: "방문자수",
            borderColor: "#1d7af3",
            pointBorderColor: "#FFF",
            pointBackgroundColor: "#1d7af3",
            pointBorderWidth: 2,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 1,
            pointRadius: 4,
            backgroundColor: 'transparent',
            fill: true,
            borderWidth: 2,
            data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 900]
        }]
    },
    options : {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            position: 'bottom',
            labels : {
                padding: 10,
                fontColor: '#1d7af3',
            }
        },
        tooltips: {
            bodySpacing: 4,
            mode:"nearest",
            intersect: 0,
            position:"nearest",
            xPadding:10,
            yPadding:10,
            caretPadding:10
        },
        layout:{
            padding:{left:15,right:15,top:15,bottom:15}
        }
    }
});