const muslider = document.getElementById("mu-slider")
const muindicator = document.getElementById("mu-value")
const sigmaslider = document.getElementById("sigma-slider")
const sigmaindicator = document.getElementById("sigma-value")
const ctx = document.getElementById("normaldist")

const normaldist = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: "Probability",
            data: [],
            borderColor: "rgb(90, 20, 250)",
            backgroundColor: "rgba(90, 20, 250, 0.2)",
            fill: true,
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,
        elements: {
            point: {
                radius: 0
            }
        },
        plugins: {
            legend: { display: false },
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
                    text: "Probability density",
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
    const response = await fetch(
        `/normal_calc?mu=${encodeURIComponent(mu)}&sigma=${encodeURIComponent(sigma)}`
    );

    if (!response.ok) {
        throw new Error(`Server returned ${response.status}`);
    }
    return await response.json();
}

async function updateNormalDistribution() {
    const mu = muslider.value;
    const sigma = sigmaslider.value;

    muindicator.textContent = mu;
    sigmaindicator.textContent = sigma;

    try {
        const data = await calculateNormal(mu, sigma);
        if (data) {
            updateChartData(normaldist, data.x, data.y);
        }
    } catch (error) {
        console.error("Could not calculate normal distribution:", error);
    }
}

muslider.addEventListener("input", updateNormalDistribution);
sigmaslider.addEventListener("input", updateNormalDistribution);

updateNormalDistribution();