function getUserResponse() {
  
  let userTextElement = document.getElementById("text-input");
  let userText = userTextElement.value;
  
  
  let userHTML = `<p class="userText"><span>User:${userText}</span></p>`;
  
  
  userTextElement.value = "";
  

  let chatBotElement = document.getElementById("chat-bot");
  chatBotElement.insertAdjacentHTML('beforeend', userHTML);

  $.get('/chatbot/getResponse',{userMessage:userText}).done(function(data){
    let returnedMessage = `<p class="bot-text">Chatbot: <span>${data}</span></p>`
    chatBotElement.insertAdjacentHTML('beforeend', returnedMessage);
  })
}

let inputButton = document.getElementById("button-input");
inputButton.addEventListener("click", () => {
  getUserResponse();
});
