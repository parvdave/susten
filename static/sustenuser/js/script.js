// Get chatbot elements
const chatbot = document.getElementById('chatbot');
const conversation = document.getElementById('conversation');
const inputForm = document.getElementById('input-form');
const inputField = document.getElementById('input-field');
document.getElementById('submit-button').disabled = true; 

function checkInput() {
  if (inputField.value == "") {
    document.getElementById('submit-button').disabled = true; 
  } else {
    document.getElementById('submit-button').disabled = false; 
  }
}

// Add event listener to input form

// Generate chatbot response function
function generateResponse(input) {
    // Add chatbot logic here
    const responses = [
      "Hello, how can I help you today? 😊",
      "I''m sorry, I didn''t understand your question. Could you please rephrase it? 😕",
      "I''m here to assist you with any questions or concerns you may have. 📩",
      "I''m sorry, I''m not able to browse the internet or access external information. Is there anything else I can help with? 💻",
      "What would you like to know? 🤔",
      "I''m sorry, I''m not programmed to handle offensive or inappropriate language. Please refrain from using such language in our conversation. 🚫",
      "I''m here to assist you with any questions or problems you may have. How can I help you today? 🚀",
      "Is there anything specific you''d like to talk about? 💬",
      "I''m happy to help with any questions or concerns you may have. Just let me know how I can assist you. 😊",
      "I''m here to assist you with any questions or problems you may have. What can I help you with today? 🤗",
      "Is there anything specific you''d like to ask or talk about? I''m here to help with any questions or concerns you may have. 💬",
      "I''m here to assist you with any questions or problems you may have. How can I help you today? 💡",
    ];
    
    // Return a random response
    return responses[Math.floor(Math.random() * responses.length)];
  }