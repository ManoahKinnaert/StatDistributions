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