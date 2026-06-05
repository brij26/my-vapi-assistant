import streamlit as st
import streamlit.components.v1 as components

st.title("My Vapi AI Assistant")

# The HTML/JS snippet from your Vapi Dashboard
vapi_widget_html = """
<script src="https://cdn.jsdelivr.net/gh/VapiAI/html-script-tag@latest/dist/assets/index.js" defer></script>
<script>
  window.addEventListener('load', () => {
    window.vapiSDK.run({
      apiKey: "7fb0ee2c-8348-4172-8e00-216308ecc8b3",
      assistant: "e6027c22-8da9-426d-b621-87da74856ae2",
      config: { mode: "chat", showChat: true, showTranscript: true }
    });
  });
</script>
"""

# Embed the widget
components.html(vapi_widget_html, height=600)