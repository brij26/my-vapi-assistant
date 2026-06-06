// =========================
// BACKEND URL
// =========================

const BACKEND_URL =
  "https://my-vapi-assistant.onrender.com/chat";

// =========================
// INIT
// =========================

export function initializeChat() {

  const sendBtn =
    document.getElementById(
      "sendBtn"
    );

  const userInput =
    document.getElementById(
      "userInput"
    );

  // SEND BUTTON

  sendBtn.addEventListener(
    "click",
    sendMessage
  );

  // ENTER KEY

  userInput.addEventListener(
    "keypress",
    (event) => {

      if (event.key === "Enter") {

        sendMessage();

      }

    }
  );

}

// =========================
// SEND MESSAGE
// =========================

async function sendMessage() {

  const input =
    document.getElementById(
      "userInput"
    );

  const message =
    input.value.trim();

  if (!message) return;

  addMessage(
    "You",
    message,
    "user-msg"
  );

  input.value = "";

  try {

    const response =
      await fetch(
        BACKEND_URL,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json"
          },

          body: JSON.stringify({
            message: message
          })
        }
      );

    const data =
      await response.json();

    addMessage(
      "AI",
      data.response,
      "bot-msg"
    );

  } catch (error) {

    console.error(error);

    addMessage(
      "AI",
      "Error connecting to backend.",
      "bot-msg"
    );

  }

}

// =========================
// ADD MESSAGE
// =========================

function addMessage(
  sender,
  text,
  className
) {

  const messages =
    document.getElementById(
      "messages"
    );

  const div =
    document.createElement("div");

  div.className =
    `message ${className}`;

  div.innerHTML =
    `<strong>${sender}:</strong> ${text}`;

  messages.appendChild(div);

  messages.scrollTop =
    messages.scrollHeight;

}