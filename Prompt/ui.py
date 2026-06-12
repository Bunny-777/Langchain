
import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="CohereLabs/tiny-aya-earth",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

st.header("Researcher Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    if not user_input:
        st.warning("Please enter a prompt first.")
    else:
        try:
            with st.spinner("Generating response..."):
                result = model.invoke(user_input)

            st.subheader("Response")
            st.write(result.content)

        except Exception as e:
            st.error("Something went wrong")
            st.code(str(e))