//---------------------
// GRAPHS FOR USERS //
//---------------------

// Active/Inactive User
const ctx4 = document.getElementById('myChart4');
var ctx4Data = document.getElementById("myChart4Data");  
var ctx4DataValue = JSON.parse(ctx4Data.value);

new Chart(ctx4, {
    type: 'pie',
    data: {
        labels: ['Active Users', 'Inactive Users'],
        datasets: [{
            label: 'Users Status',
            data: ctx4DataValue,
            fill: false,
            backgroundColor: [
            'rgba(255, 205, 86, 0.2)',
            'rgba(54, 162, 235, 0.2)'
            ],
            borderColor: [
            'rgb(255, 205, 86)',
            'rgb(54, 162, 235)'
            ],
            hoverOffset: 4
        }]
    },
});
