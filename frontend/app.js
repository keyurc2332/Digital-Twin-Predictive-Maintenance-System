const API_URL = "http://127.0.0.1:5000/predict";

async function fetchPrediction(){

    try{

        const response = await fetch(API_URL);

        const data = await response.json();

        if(data.status==="buffering"){

            document.getElementById("status").innerText="Buffering Sensor Data";

            return;

        }

        document.getElementById("status").innerText="Online";

        document.getElementById("health-score").innerText=data.health_score;

        document.getElementById("fault").innerText=data.fault_prediction;

        document.getElementById("anomaly").innerText=data.anomaly_detected
        ? "Detected"
        : "Normal";

        document.getElementById("rul").innerText=data.remaining_useful_life;

        document.getElementById("recommendation").innerText=
        data.maintenance_recommendation;

    }

    catch(error){

        document.getElementById("status").innerText="Backend Offline";

        console.error(error);

    }

}

fetchPrediction();

setInterval(fetchPrediction,2000);