import streamlit as st
from chat_engine import chat_response

st.set_page_config(page_title="Mini LLM", page_icon="🤖")
st.title("🤖 Mini LLM Chat")

# Estado da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada do usuário
user_input = st.chat_input("Digite sua mensagem...")

if user_input:
    # Mostra mensagem do usuário
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Gera resposta
    with st.spinner("Pensando..."):
        response = chat_response(user_input)

    # Mostra resposta
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)
