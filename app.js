document.getElementById('data-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const userData = {
        income: parseInt(document.getElementById('income').value),
        existingDebts: parseInt(document.getElementById('existing-debts').value),
        creditHistory: parseInt(document.getElementById('credit-history').value),
    };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('credit-score').textContent = data.score;
        updateRiskLevel(data.score);
    });
});

function updateRiskLevel(score) {
    const riskLevel = document.getElementById('risk-level');
    if (score > 750) {
        riskLevel.textContent = "Risk Level: Low";
        riskLevel.style.color = "green";
    } else if (score > 600) {
        riskLevel.textContent = "Risk Level: Moderate";
        riskLevel.style.color = "orange";
    } else {
        riskLevel.textContent = "Risk Level: High";
        riskLevel.style.color = "red";
    }
}
