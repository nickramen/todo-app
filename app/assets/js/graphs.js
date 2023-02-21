//---------------------------
// USERS SATISFACTION
//---------------------------

//Display saved rate
const satisfactionRate = document.getElementById('userSatisfactionRate');
var satisfactionRateValue = satisfactionRate.value
var rateInputs = document.getElementsByName('rating')

for(var inputs = 0; inputs < rateInputs.length; inputs++){
    if(rateInputs[inputs].value == satisfactionRateValue){
        rateInputs[inputs].checked = true;
    }
}

//Edit rate when star is clicked
rateInputs.forEach(function(rateInputs) {
    rateInputs.addEventListener('click', function() {
        // Get the value of the clicked input
        var value = this.value;
        // Call a function and pass the id as an argument
        update_satisfaction_rate(value);
    });
});
function update_satisfaction_rate(value) {
    fetch('/update_satisfaction_rate', {
        method: 'POST',
        body: value
    })
    .then(response => response.text())
    .then(data => {
        if (data.success) {
            //window.location.href = 'http://127.0.0.1:5000/index';
        } else {
        }
    })
    .catch(error => console.error(error));
}



//---------------------------
// GRAPHS FOR USERS
//---------------------------

const ctx = document.getElementById('myChart1');
var ctxData = document.getElementById("myChart1Data");  
var ctxDataValue = JSON.parse(ctxData.value);

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        datasets: [{
            axis: 'y',
            label: 'Total tasks per day',
            data: ctxDataValue,
            fill: false,
            backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        indexAxis: 'y',
        scales: {
            y: {
            beginAtZero: true
            }
        }
    }
});


const ctx2 = document.getElementById('myChart2');
var ctx2Data = document.getElementById("myChart2Data");  
var ctx2DataValue = JSON.parse(ctx2Data.value);

new Chart(ctx2, {
    type: 'doughnut',
    data: {
        labels: ['Done', 'Undone'],
        datasets: [{
            label: 'Total tasks per week',
            data: ctx2DataValue,
            fill: false,
            backgroundColor: [
            'rgba(75, 192, 192, 0.2)',
            'rgba(255, 99, 132, 0.2)'
            ],
            borderColor: [
            'rgb(75, 192, 192)',
            'rgb(255, 99, 132)',
            ],
            hoverOffset: 4
        }]
    },
});


const ctx3 = document.getElementById('myChart3');
var ctx3Data = document.getElementById("myChart3Data");
var ctx3DataLabels = document.getElementById("myChart3DataLabels");    
var ctx3DataValue = JSON.parse(ctx3Data.value);
var ctx3DataLabelsValue = ctx3DataLabels.value

new Chart(ctx3, {
    type: 'bar',
    data: {
        labels: ['Home', 'Personal', 'School', 'Social', 'Travel', 'Work', 'Work'],
        datasets: [{
            axis: 'y',
            label: 'Tasks per category',
            data: ctx3DataValue,
            fill: false,
            backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(201, 203, 207, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
            beginAtZero: true
            }
        }
    }
});

// new Chart(ctx3, {
//     type: 'polarArea',
//     data: {
//         labels: ['Home', 'Personal', 'School', 'Social', 'Travel', 'Work', 'Workout'],
//         datasets: [{
//             label: 'Tasks per category',
//             data: [1,2,2,1,1,2,1],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(255, 159, 64, 0.2)',
//                 'rgba(255, 205, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(201, 203, 207, 0.2)'
//             ],
//             borderColor: [
//                 'rgb(255, 99, 132)',
//                 'rgb(255, 159, 64)',
//                 'rgb(255, 205, 86)',
//                 'rgb(75, 192, 192)',
//                 'rgb(54, 162, 235)',
//                 'rgb(153, 102, 255)',
//                 'rgb(201, 203, 207)'
//             ],
//             hoverOffset: 4
//         }]
//     },
//     options: {}
// });


// google.charts.load("current", {packages:["corechart"]});
// google.charts.setOnLoadCallback(drawChart);
// function drawChart() {
//     var data = google.visualization.arrayToDataTable([
//         ['Category', 'Task Count'],
//         ['Home',    11],
//         ['Personal',9],
//         ['School',  10],
//         ['Social',  6],
//         ['Travel',  7],
//         ['Work',    11],
//         ['Workout', 7]
//     ]);

//     var options = {
//         title: 'Top used categories',
//         is3D: true,
//     };

//     var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
//     chart.draw(data, options);
// }