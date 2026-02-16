function sendMessage() {

    let message = document.getElementById("userInput").value;

    fetch("/chatbot", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chatResponse").innerText = data.reply;
    });
}