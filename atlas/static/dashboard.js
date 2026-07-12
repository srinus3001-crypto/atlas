async function updateMissionStatus(missionId){

    try{

        const response = await fetch(`/status/${missionId}`);

        if(!response.ok){
            return;
        }

        const data = await response.json();

        document.getElementById("stage").innerHTML =
            "📍 " + data.stage;

        document.getElementById("message").innerHTML =
            data.message;

        document.getElementById("progress").style.width =
            data.progress + "%";

        document.getElementById("progressText").innerHTML =
            data.progress + "%";

        if(data.progress >= 100){

            clearInterval(window.statusInterval);

        }

    }

    catch(error){

        console.log(error);

    }

}

function startStatusPolling(missionId){

    updateMissionStatus(missionId);

    window.statusInterval = setInterval(function(){

        updateMissionStatus(missionId);

    },2000);

}