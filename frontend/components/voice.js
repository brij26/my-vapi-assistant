import Vapi from "https://esm.sh/@vapi-ai/web";

// =========================
// CONFIG
// =========================

const PUBLIC_KEY =
  "38308316-bd09-45a0-894a-55af9a09eb11";

const ASSISTANT_ID =
  "e6027c22-8da9-426d-b621-87da74856ae2";

// =========================
// INIT
// =========================

export function initializeVoice() {

  const vapi =
    new Vapi(PUBLIC_KEY);

  let active = false;

  const callBtn =
    document.getElementById(
      "callBtn"
    );

  // =========================
  // STATUS
  // =========================

  function setStatus(
    text,
    live = false
  ) {

    document.getElementById(
      "statusText"
    ).textContent = text;

    const dot =
      document.getElementById("dot");

    if (live) {

      dot.classList.add("live");

    } else {

      dot.classList.remove("live");

    }

  }

  // =========================
  // BUTTON
  // =========================

  callBtn.addEventListener(
    "click",
    async () => {

      try {

        if (!active) {

          active = true;

          setStatus(
            "Connecting...",
            true
          );

          callBtn.textContent =
            "🔴 End Call";

          callBtn.classList.add("end");

          await vapi.start(
            ASSISTANT_ID
          );

        } else {

          vapi.stop();

        }

      } catch (error) {

        console.error(error);

        setStatus(
          "Voice Error",
          false
        );

      }

    }
  );

  // =========================
  // EVENTS
  // =========================

  vapi.on(
    "call-start",
    () => {

      setStatus(
        "Connected · Speak now",
        true
      );

    }
  );

  vapi.on(
    "call-end",
    () => {

      active = false;

      setStatus(
        "Call ended",
        false
      );

      callBtn.textContent =
        "📞 Start Voice Call";

      callBtn.classList.remove("end");

    }
  );

  vapi.on(
    "speech-start",
    () => {

      setStatus(
        "Agent speaking...",
        true
      );

    }
  );

  vapi.on(
    "speech-end",
    () => {

      setStatus(
        "Listening...",
        true
      );

    }
  );

  vapi.on(
    "error",
    (err) => {

      console.error(err);

      setStatus(
        "Voice Error",
        false
      );

    }
  );

}