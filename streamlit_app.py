import streamlit as st
import streamlit.components.v1 as components

st.title("My Vapi AI Assistant")

# The HTML/JS snippet from your Vapi Dashboard
vapi_widget_html = """
<div id="vapi-widget-container"></div>
<script src="https://cdn.jsdelivr.net/gh/VapiAI/html-script-tag@latest/dist/assets/index.js" defer></script>
<script>
  window.addEventListener('DOMContentLoaded', () => {
    // Adding a small delay to ensure the SDK is fully initialized
    setTimeout(() => {
      if (window.vapiSDK) {
        window.vapiSDK.run({
          apiKey: "38308316-bd09-45a0-894a-55af9a09eb11",
          assistant: "e6027c22-8da9-426d-b621-87da74856ae2",
          config: {
            mode: "chat",
            showChat: true,
            showTranscript: true,
            position: "bottom-right"
          }
        });
      } else {
        console.error("Vapi SDK failed to load.");
      }
    }, 1000);
  });
</script>
"""

# Embed the widget
components.html(vapi_widget_html, height=600)