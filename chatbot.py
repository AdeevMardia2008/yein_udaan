import streamlit as st
import google.generativeai as genai

st.markdown("# Ask your doubts to the AI chatbot!")
st.sidebar.markdown("# Yein Udaan")

GOOGLE_API_KEY = "AIzaSyAMEUSbRYnHHEVj0hfUgdeoOfLFeFUYvdQ"
genai.configure(api_key=GOOGLE_API_KEY)

geminiModel=genai.GenerativeModel("gemini-pro") 
chat = geminiModel.start_chat(history=[])

def get_gemini_response(query):
    instantResponse=chat.send_message(query,stream=True)
    return instantResponse

st.header("Yein Udaan - Bridge the opportunity gap through learning.")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

inputText=st.text_input("Input: ",key="input")
submitButton=st.button("Get Response")

if submitButton and inputText:
    output=get_gemini_response(inputText)
    st.session_state['chat_history'].append(("You", inputText))
    st.subheader("The Response is")
    for outputChunk in output:
        st.write(outputChunk.text)
        st.session_state['chat_history'].append(("Bot", outputChunk.text))
        
st.subheader("Chat History") 
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
