window.onload = function () {
    var ctx = document.getElementById('weeklyChart').getContext('2d');
    var gradient = ctx.createLinearGradient(0, 0, 0, 250);
    gradient.addColorStop(0, 'rgba(54, 162, 235, 0.5)');
    gradient.addColorStop(1, 'rgba(54, 162, 235, 0.1)');

    var weeklyChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Activity',
                data: [300, 350, 400, 450, 500, 550, 475],
                backgroundColor: gradient,
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
                padding: {
                    bottom: 10
                }
            },
            scales: {
                x: {
                    display: true,
                    ticks: {
                        padding: 5
                    }
                },
                y: {
                    beginAtZero: true
                }
            }
        }
    });
};
