var apiUrl = 'http://staging-pauline-portfolio.westeurope.azurecontainer.io:8000';

function addNewQuestion() {
    let prompt = window.prompt("Quelle est ta question?")
    let chatBoxEl = document.getElementById("chat-add");
    let msgEl = document.createElement("p");
    msgEl.innerText = prompt;
    msgEl.classList.add("chat-msg");
    msgEl.classList.add("chat-question");
    chatBoxEl.appendChild(msgEl);
    let reponseEl = document.createElement("p");
    chatBoxEl.appendChild(reponseEl);
    reponseEl.classList.add("chat-msg");
    reponseEl.classList.add("chat-reponse");
    reponseEl.innerText = "...";
        
    fetch(apiUrl + '/chat/?prompt=' + prompt, {method: "POST"})
    .then(response => {
      return response.json();
    })
    .then(data => {
      reponseEl.innerText = data;
      document.getElementById("feedback").style.display = "block";
    });
}
function sendFeedback(feedback) {
  console.log("Feedback:", feedback);
  fetch(apiUrl + '/feedback/?feedback=' + feedback, {method: "POST"})
  .catch(error => {
    console.error('Error:', error);
  });
  document.getElementById("feedback").style.display = "none";
}