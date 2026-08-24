const ctx = document.getElementById("normaldist")

const normaldist = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: "Probability",
            data: [],
            borderColor: "blue",
            backgroundColor: "rgba(20, 20, 200, 0.2)",
            fill: true,
        }]
    },

    options: {
        plugins: {
            legend: { display: false},
            title: {
                display: true,
                text: "Normal Distribution",
                font: { size: 16 }
            }
        },

        scales: {
            y: {
                type: "linear",
                title: {
                    display: true,
                    text: "Probability",
                    font: { size: 10 }
                }
            },

            x: {
                type: "linear",
                title: {
                    display: true,
                    text: "Some values",
                    font: { size: 10 }
                }
            }
        }
    }
})

function updateChartData(chart, labels, newData) {
    chart.data.labels = labels  
    chart.data.datasets[0].data = newData  
    chart.update()
}

async function calculateNormal(mu, sigma) {
    const response = await fetch(`/normal_calc?mu=${mu}&sigma=${sigma}`);

    if (!response.ok) {
        throw new Error(`Server returned ${response.status}`);
    }

    const data = await response.json();
    return data;
}