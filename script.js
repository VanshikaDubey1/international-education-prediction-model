document.getElementById("predictForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const data = {
        country: document.getElementById("country").value,
        degree: document.getElementById("degree").value,
        field: document.getElementById("field").value,
        duration: parseInt(document.getElementById("duration").value),
    };

    fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .then((response) => {
            if (!response.ok) throw new Error("Network response error");
            return response.json();
        })
        .then((result) => {
            document.getElementById("result").innerHTML = `
                <h3>Prediction Result:</h3>
                <p><strong>Tuition:</strong> $${result.tuition}</p>
                <p><strong>Living Expenses:</strong> $${result.living}</p>
                <p><strong>Total:</strong> $${result.total}</p>
            `;
        })
        .catch((error) => {
            console.error("Error:", error);
            document.getElementById("result").innerHTML = `<p class="error">Failed to fetch prediction. Try again.</p>`;
        });
});