## initialization
import streamlit as st
import pandas as pd

## layout and style
st.set_page_config(layout='wide')

## Define and load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css('style.css')

## sidebar
function_key = st.sidebar.selectbox("Choose the preferred service", ["Chatbot Service", "Data Visualization"])
if function_key == 'Data Visualization':
    api_key = st.sidebar.selectbox("Choose your preferred API: ", ["Option A", "Option B"])
    visualization_type = st.sidebar.selectbox("Choose the type of visualization", ["Histogram", "Pie Chart", "Trend Analysis"])
    
    # st.set_page_config(page_title='File Upload App') # set page config
    st.title('Upload a file') # title for the uploader
    uploaded_file = st.file_uploader("Choose a file") # file uploader widget
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.write("Filename:", uploaded_file.name)
        st.write("Filetype:", uploaded_file.type)
        st.write("Filesize:", uploaded_file.size)
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            st.write(df)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    ## Analysis
    
else:
    api_key = st.sidebar.selectbox("Choose your preferred API: ", ["Option A", "Option B"])
    ## styling
    st.header("🤖Streamlit Smart Window")

    ## main content area
    user_input = st.text_input("What is on your mind?")
    if st.button("Send"):
        response = "This is a response to the user query."
        st.write(response)

    ## stage management
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    st.session_state.conversation.append(user_input)
    for message in st.session_state.conversation: # display the conversation
        st.write(message)
