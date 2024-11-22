let socket = new WebSocket("ws://localhost:8765");
let msg = document.getElementById("input");


function sendmsg() {
  socket.send(msg.value);
}

socket.addEventListener("open", (event) => {
    console.log("Connexion établit");
  });

  socket.addEventListener("message", (event) => {
    console.log("Message from server ", event.data);
  });

console.log(msg);