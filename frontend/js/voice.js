const startBtn = document.getElementById("start-btn");
const transcript = document.getElementById("transcript");
const aiResponse = document.getElementById("ai-response");

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

    startBtn.addEventListener("click", () => {

        recognition.start();

        transcript.value = "🎤 Listening...";
        aiResponse.value = "Waiting for speech...";

    });

    recognition.onresult = function (event) {

        const text = event.results[0][0].transcript;

        transcript.value = text;

        aiResponse.value =
`You said:

${text}

(This is a placeholder response. Later we'll connect it to the AI backend.)`;

    };

    recognition.onerror = function () {

        transcript.value = "❌ Could not recognize speech.";

    };

} else {

    transcript.value =
        "Speech Recognition is not supported in this browser.";

}