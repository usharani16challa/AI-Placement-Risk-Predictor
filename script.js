function predict() {
    const cgpa = parseFloat(document.getElementById("cgpa").value);
    const internship = parseInt(document.getElementById("internship").value);
    const tier = parseInt(document.getElementById("tier").value);

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            cgpa: cgpa,
            internship: internship,
            college_tier: tier
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // 🔥 check output in console
        document.getElementById("result").innerText = data.prediction;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}