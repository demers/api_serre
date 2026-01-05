const ctx = document.getElementById('tempChart');

const labels = [
    "00h", "01h", "02h", "03h", "04h", "05h",
    "06h", "07h", "08h", "09h", "10h", "11h",
    "12h", "13h", "14h", "15h", "16h", "17h",
    "18h", "19h", "20h", "21h", "22h", "23h"
];

const data = {
    labels: labels,
    datasets: [
        {
            label: "Température Haut (°C)",
            data: [21,21,20,20,19,19,20,22,24,25,26,27,28,29,28,27,26,25,24,23,22,22,21,21],
            borderColor: "red",
            tension: 0.3
        },
        {
            label: "Température Bas (°C)",
            data: [20,20,19,19,18,18,19,21,23,24,25,26,27,28,27,26,25,24,23,22,21,21,20,20],
            borderColor: "blue",
            tension: 0.3
        },
        {
            label: "Température Extérieure (°C)",
            data: [15,14,14,13,13,12,12,13,15,17,18,19,20,20,19,18,17,16,15,15,15,14,14,14],
            borderColor: "green",
            tension: 0.3
        }
    ]
};

new Chart(ctx, {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'top'
            }
        },
        scales: {
            y: {
                title: {
                    display: true,
                    text: "Température (°C)"
                }
            },
            x: {
                title: {
                    display: true,
                    text: "Heure"
                }
            }
        }
    }
});
