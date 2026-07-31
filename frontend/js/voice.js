const startBtn = document.getElementById("start-btn");
const transcript = document.getElementById("transcript");
const aiResponse = document.getElementById("ai-response");

const clearBtn = document.getElementById("clear-btn");
const speakBtn = document.getElementById("speak-btn");


console.log(startBtn);
console.log(transcript);
console.log(aiResponse);


if ("webkitSpeechRecognition" in window || "SpeechRecognition" in window) {

    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    const recognition = new SpeechRecognition();

    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = "en-US";


    // Start microphone
    startBtn.addEventListener("click", () => {

        recognition.start();

        transcript.value = "🎤 Listening...";
        aiResponse.value = "Waiting for speech...";

    });


    // Speech received
    recognition.onresult = function(event) {

        const text = event.results[0][0].transcript;

        transcript.value = text;


        aiResponse.value =
`You said:

${text}

(This is a placeholder response.
AI connection will be added next.)`;

    };


    // Error handling
    recognition.onerror = function(event) {

        console.log(event.error);

        transcript.value =
        "❌ Could not recognize speech.";

    };


}
else {

    transcript.value =
    "Speech Recognition is not supported in this browser.";

}



// Clear button
clearBtn.addEventListener("click", () => {

    transcript.value = "";
    aiResponse.value = "";

});



// Speak AI response
speakBtn.addEventListener("click", () => {

    const text = aiResponse.value;

    if (!text.trim()) {
        return;
    }


    const speech = new SpeechSynthesisUtterance(text);

    speech.lang = "en-US";

    window.speechSynthesis.speak(speech);

});