# Import required libraries
from utils import output_list

from dotenv import load_dotenv
from itertools import zip_longest

import streamlit as st
from streamlit_chat import message

# output_llm = iter(output_llm)
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# Load environment variables
load_dotenv()

# Set streamlit page configuration
st.set_page_config(page_title="DataWhisper")
st.title("DataWhisper - Contextual AI chatbot with Integrated Knowledge")

# Initialize session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI generated responses

if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store past user inputs

if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""  # Store the latest user input

# Initialize the ChatOpenAI model
chat = ChatOpenAI(
    temperature=0.5,
    model_name="gpt-3.5-turbo"
)


def build_message_list():
    """
    Build a list of messages including system, human and AI messages.
    """
    # Start zipped_messages with the SystemMessage
    zipped_messages = [SystemMessage(
        content="You are a helpful AI assistant talking with a human. If you do not know an answer, just say 'I don't know', do not make up an answer.")]

    # Zip together the past and generated messages
    for human_msg, ai_msg in zip_longest(st.session_state['past'], st.session_state['generated']):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(
                content=human_msg))  # Add user messages
        if ai_msg is not None:
            zipped_messages.append(
                AIMessage(content=ai_msg))  # Add AI messages

    return zipped_messages



def generate_response(output_llm):
    """
    Generate AI response using the ChatOpenAI model.
    """
    # Build the list of messages
    zipped_messages = build_message_list()

    # Generate response using the chat model
#     ai_response = chat(zipped_messages)
#     global index
#     index = index+1
#     print("output_llm",output_llm)
    return output_llm

#     return ai_response.content


# Define function to submit user input
index=-1
def submit():
    # Set entered_prompt to the current value of prompt_input
    st.session_state.entered_prompt = st.session_state.prompt_input
    # Clear prompt_input
    st.session_state.prompt_input = ""
#     global index
#     index = index+1
#     print("index",index)
    


# Create a text input for user
st.text_input('Prajwal: ', key='prompt_input', on_change=submit)



if st.session_state.entered_prompt != "":
    # Get user query
    user_query = st.session_state.entered_prompt

    # Append user query to past queries
    st.session_state.past.append(user_query)

    # Generate response
#     global index
    
    
    
#     output_llm = [
#     "There are a total of 8 employees",'''Sure, Here is the SQL query I ran to get the results,\ \n
#                  ```SELECT COUNT(*) FROM 'Employee'``` \n I am using the sqlite:///Chinook.db and the Employee table from it.I executed this query on the DB to get to the answer.''']
#     output = generate_response(output_list.pop())

    # Append AI response to generated responses
    st.session_state.generated.append(output_list.pop(0))

# Display the chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        # Display AI response
        message(st.session_state["generated"][i], key=str(i))
        # Display user message
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')


# # Add credit
# st.markdown("""
# ---
# Made with 🤖 by [Austin Johnson](https://github.com/AustonianAI)""")
