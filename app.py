import streamlit as st
from agent_graph import research_assistant

st.set_page_config(page_title="AI Chatbot", layout="wide")

st.title("💬 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    role = "👤 You:" if message["role"] == "user" else "🤖 Bot:"
    with st.chat_message(message["role"]):
        st.markdown(f"**{role}** {message['content']}")

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
 
    with st.chat_message("user"):
        st.markdown(f"**👤 You:** {user_input}")

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = research_assistant.invoke({"input_message": user_input})["search_result"]["output"]
            except:
                response = research_assistant.invoke({"input_message": user_input})["search_result"]
        
        st.markdown(f"**🤖 Bot:** {response}")

    st.session_state["messages"].append({"role": "assistant", "content": response})
