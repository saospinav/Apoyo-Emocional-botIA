async function enviarMensaje() {
    const input = document.getElementById("user-input");
    const mensaje = input.value;
    if (!mensaje) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user"><strong>Tú:</strong> ${mensaje}</div>`;

    const respuesta = await fetch("/preguntar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensaje })
    });

    const data = await respuesta.json();
    chatBox.innerHTML += `<div class="bot"><strong>Bot:</strong> ${data.respuesta}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = "";
}
