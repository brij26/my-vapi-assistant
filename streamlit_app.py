import streamlit as st
import streamlit.components.v1 as components

st.title("My Vapi AI Assistant")

# The HTML/JS snippet from your Vapi Dashboard
vapi_widget_html = """
<script>
  var vapiInstance = null;
  const assistant = "e6027c22-8da9-426d-b621-87da74856ae2"; // Substitute with your assistant ID
  const apiKey = "7fb0ee2c-8348-4172-8e00-216308ecc8b3"; // Substitute with your Public key from Vapi Dashboard.
  const buttonConfig = {}; // Modify this as required

  (function (d, t) {
    var g = document.createElement(t),
      s = d.getElementsByTagName(t)[0];
    g.src =
      "https://cdn.jsdelivr.net/gh/VapiAI/html-script-tag@latest/dist/assets/index.js";
    g.defer = true;
    g.async = true;
    s.parentNode.insertBefore(g, s);

    g.onload = function () {
      vapiInstance = window.vapiSDK.run({
        apiKey: apiKey, // mandatory
        assistant: assistant, // mandatory
        config: buttonConfig, // optional
      });
    };
  })(document, "script");
</script>

"""

# Embed the widget
components.html(vapi_widget_html, height=600)