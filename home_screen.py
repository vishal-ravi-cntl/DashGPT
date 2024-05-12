import streamlit as st

st.title("DashGPT")

# Initialize chat history
if "chats" not in st.session_state:
    st.session_state.chats = []

# Display chat messages from history on app rerun
for chat in st.session_state.chats:
    with st.chat_message(chat["role"],avatar=chat["avatar"]):
        st.markdown(chat["title"])
        st.write(chat["content"])

# React to user input
if prompt := st.chat_input("Message DashGPT"):
    userTitle="##### You"
    userAvatar=None
    gptAvatar="dash-logo.png"
    gptTitle="##### DashGPT"

    # Display user message in chat message container
    with st.chat_message("user"):
        st.write(userTitle)
        st.write(prompt)
    # Add user message to chat history
    st.session_state.chats.append({"role": "user", "content": prompt,"title":userTitle,"avatar":userAvatar})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message(name="assistant",avatar=gptAvatar):
        st.markdown(gptTitle)
        st.write(response)
    # Add assistant response to chat history
    st.session_state.chats.append({"role": "assistant", "content": response,"title":gptTitle,"avatar":gptAvatar})