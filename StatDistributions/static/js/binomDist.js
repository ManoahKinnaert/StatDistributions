const nslider = document.getElementById("n-slider")
const nindicator = document.getElementById("n-value")
const pslider = document.getElementById("p-slider")
const pindicator = document.getElementById("p-value")

const pmf = document.getElementById("pmf")
const cdf = document.getElementById("cdf")

const cdfChart = new Chart(cdf, {
    type: 'scatter',
    data: {
        labels: [],
        datasets: [{
            label: "P(X <= k)",
            data: [],
            borderColor: "rgb(90, 20, 250)"
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { display: false },
            title: {
                display: true,
                text: "Cumulative Distribution Function (CDF)",
                font: { size: 16 }
            }
        },

        scales: {
            y: {
                type: "linear",
                title: {
                    display: true,
                    text: "P(X <= k)",
                    font: { size: 10 }
                }
            },

            x: {
                type: "linear",
                title: {
                    display: true,
                    text: "N",
                    font: { size: 10 }
                }
            }
        }
    }
})

const pmfChart = new Chart(pmf, {
    type: 'scatter',
    data: {
        labels: [],
        datasets: [{
            label: "P(X = k)",
            data: [],
            borderColor: "rgb(90, 20, 250)"
        }]
    },

    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { display: false },
            title: {
                display: true,
                text: "Probability Mass Function (PMF)",
                font: { size: 16 }
            }
        },

        scales: {
            y: {
                type: "linear",
                title: {
                    display: true,
                    text: "P(X = k)",
                    font: { size: 10 }
                }
            },

            x: {
                type: "linear",
                title: {
                    display: true,
                    text: "k",
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

async function calculateBinom(p, n) {
    const response = await fetch(
        `/binom_calc?p=${encodeURIComponent(p)}&n=${encodeURIComponent(n)}`
    );

    if (!response.ok) {
        throw new Error(`Server returned ${response.status}`);
    }
    return await response.json();
}

async function updateCharts() {
    const p = pslider.value
    const n = nslider.value

    pindicator.textContent = p
    nindicator.textContent = n

    try {
        const data = await calculateBinom(p, n)
        if (data) {
            updateChartData(cdfChart, data.x, data.y_cdf)
            updateChartData(pmfChart, data.x, data.y_pmf)
        }
    } catch (error) {
        console.log("Could not generate binomial distribution functions:", error)
    }
}

nslider.addEventListener("input", updateCharts)
pslider.addEventListener("input", updateCharts)

updateCharts()