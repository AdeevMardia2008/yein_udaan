import streamlit as st
import google.generativeai as genai

# Set the page configuration
st.set_page_config(page_title="Yein Udaan Chatbot", page_icon=":robot_face:", layout="wide")

# Add custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f4f8;  /* Light background color */
        font-family: 'Arial', sans-serif;  /* Font style */
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;  /* Dark sidebar color */
        color: white;
    }
    h1 {
        color: #2980b9;  /* Primary color for headers */
        font-size: 2.5em;  /* Larger header size */
        text-align: center;  /* Centered header */
    }
    h2 {
        color: #27ae60;  /* Secondary color for subheaders */
        font-size: 1.5em;  /* Larger subheader size */
    }
    .stTextInput>div>input {
        background-color: #ecf0f1;  /* Light input background */
        border: 2px solid #2980b9;  /* Input border color */
        border-radius: 5px;  /* Rounded corners */
        padding: 10px;  /* Padding inside the input */
        font-size: 1em;  /* Font size */
        border-color: #ffff00;
    }
    .stTextInput>div>input:focus {
        border-color: #27ae60;  /* Change border color on focus */
        outline: none;  /* Remove default outline */
    }
    .stButton>button {
        background-color: #2980b9;  /* Button color */
        color: white;  /* Button text color */
        border: none;  /* Remove border */
        border-radius: 5px;  /* Rounded corners */
        padding: 10px 20px;  /* Padding for the button */
        font-size: 1em;  /* Font size */
        cursor: pointer;  /* Pointer cursor on hover */
        transition: background-color 0.3s;  /* Smooth transition */
    }
    .stButton>button:hover {
        background-color: #ffff00;  /* Change button color on hover */
    }
    .chat-history {
        background-color: #ffffff;  /* White background for chat history */
        border-radius: 5px;  /* Rounded corners */
        padding: 10px;  /* Padding for chat history */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
    }
    </style>
""", unsafe_allow_html=True)

# Add the logo
st.sidebar.image("https://yeinudaan.org/wp-content/uploads/2020/10/YU-Logo_without-tagline.png", use_container_width=True)
st.sidebar.markdown("# Yein Udaan")

# Configure the Google Generative AI
GOOGLE_API_KEY = "AIzaSyDQ-KKFb0ztH4MG0f_ckAgL92J74vHpsJ4"
genai.configure(api_key=GOOGLE_API_KEY)

geminiModel = genai.GenerativeModel("gemini-pro")
chat = geminiModel.start_chat(history=[])

def get_gemini_response(query):
    instantResponse = chat.send_message(query, stream=True)
    return instantResponse

st.header("Yein Udaan - Bridge the opportunity gap through learning.")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

inputText = st.text_input("Input: ", key="input")
submitButton = st.button("Get Response")

if submitButton and inputText:
    output = get_gemini_response(inputText)
    st.session_state['chat_history'].append(("You", inputText))
    st.subheader("The Response is")
    for outputChunk in output:
        st.write(outputChunk.text)
        st.session_state['chat_history'].append(("Bot", outputChunk.text))

st.subheader("Chat History") 
chat_container = st.container()
with chat_container:
    for role, text in st.session_state['chat_history']:
        st.markdown(f"<div class='chat-history'><strong>{role}:</strong> {text}</div>", unsafe_allow_html=True)
