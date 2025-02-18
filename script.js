// script.js
const insightsElement = document.getElementById('insights');

// Get NeuraDSP insights
fetch('https://api.neuradsp.com/insights')
    .then(response => response.json())
    .then(data => {
        insightsElement.textContent = data.insights;
    });
