async function sendPrediction() {
    const input = document.getElementById('anticipation').value;

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ number: input })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById('result').innerText = data.result;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error: only float is supported!';
    }
}
