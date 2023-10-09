# # import streamlit as st
# # import langchain
# # import openai
# # from transformers import load_tool
# # from langchain.llms import OpenAI
# # from langchain_experimental.autonomous_agents import HuggingGPT
# # # %env OPENAI_API_BASE=http://localhost:8000/v1
# # llm = OpenAI(model_name="gpt-3.5-turbo")
# # agent = HuggingGPT(llm, hf_tools)

# # # Title
# # st.title('EurekaX')

# # # Set OpenAI API
# # openai.api_key = "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"



# # # Create LangChain agent
# # # agent = langchain.Agent()
# # hf_tools = [
# #     load_tool(tool_name)
# #     for tool_name in [
# #         "document-question-answering",
# #         "image-captioning",
# #         "image-question-answering",
# #         "image-segmentation",
# #         "speech-to-text",
# #         "summarization",
# #         "text-classification",
# #         "text-question-answering",
# #         "translation",
# #         "huggingface-tools/text-to-image",
# #         "huggingface-tools/text-to-video",
# #         "text-to-speech",
# #         "huggingface-tools/text-download",
# #         "huggingface-tools/image-transformation",
# #     ]
# # ]

# # # From elements
# # question_types = ["text", "choice", "check button", "radio button"]

# # # Create survey form
# # def create_survey(text):
# #     # LangChain analyze text
# #     questions = agent.run(text)

# #     # Make survey form
# #     survey = []
# #     for question in questions:
# #         if question["type"] == "text":
# #             survey.append(st.text_input(question["label"]))
# #         elif question["type"] == "choice":
# #             survey.append(st.selectbox(question["label"], question["options"]))
# #         elif question["type"] == "check button":
# #             survey.append(st.checkbox(question["label"], question["options"]))
# #         elif question["type"] == "radio button":
# #             survey.append(st.radio(question["label"], question["options"]))

# #     return survey

# # # Main UI
# # def main():
# #     # Input UI form from text
# #     text = st.text_input("Input your suvery details. AI make form from them:")

# #     # Generate survey from text
# #     survey = create_survey(text)

# #     # Show survey UI
# #     st.write(survey)

# # # Start program
# # if __name__ == "__main__":
# #     main()



# import streamlit as st
# from langchain.llms import OpenAI  # Corrected import
# from transformers import load_tool
# from langchain_experimental.autonomous_agents import HuggingGPT

# # Set OpenAI API key
# OpenAI.api_key = "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"  # Replace with your actual API key

# # Create LangChain agent
# llm = OpenAI(model_name="gpt-3.5-turbo")

# # Define the hf_tools list
# hf_tools = [
#     load_tool(tool_name)
#     for tool_name in [
#         "document-question-answering",
#         "image-captioning",
#         "image-question-answering",
#         "image-segmentation",
#         "speech-to-text",
#         "summarization",
#         "text-classification",
#         "text-question-answering",
#         "translation",
#         "huggingface-tools/text-to-image",
#         "huggingface-tools/text-to-video",
#         "text-to-speech",
#         "huggingface-tools/text-download",
#         "huggingface-tools/image-transformation",
#     ]
# ]

# # Create the agent
# agent = HuggingGPT(llm, hf_tools)

# # Title
# st.title('EurekaX')

# # Create survey form
# def create_survey(text):
#     # LangChain analyze text
#     questions = agent.run(text)

#     # Make survey form
#     survey = []
#     for question in questions:
#         if question["type"] == "text":
#             survey.append(st.text_input(question["label"]))
#         elif question["type"] == "choice":
#             survey.append(st.selectbox(question["label"], question["options"]))
#         elif question["type"] == "check button":
#             survey.append(st.checkbox(question["label"], question["options"]))
#         elif question["type"] == "radio button":
#             survey.append(st.radio(question["label"], question["options"]))

#     return survey

# # Main UI
# def main():
#     # Input UI form from text
#     text = st.text_input("Input your survey details. AI makes a form from them:")

#     # Generate survey from text
#     survey = create_survey(text)

#     # Show survey UI
#     st.write(survey)

# # Start program
# if __name__ == "__main__":
#     main()

# import streamlit as st
# from langchain.llms import OpenAI
# from transformers import load_tool
# from langchain_experimental.autonomous_agents import HuggingGPT

# # Set OpenAI API key
# OpenAI.api_key = "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"  # Replace with your actual API key

# # Create LangChain agent
# llm = OpenAI(model_name="gpt-3.5-turbo")

# # Define the hf_tools list
# hf_tools = [
#     load_tool(tool_name)
#     for tool_name in [
#         "document-question-answering",
#         "image-captioning",
#         "image-question-answering",
#         "image-segmentation",
#         "speech-to-text",
#         "summarization",
#         "text-classification",
#         "text-question-answering",
#         "translation",
#         "huggingface-tools/text-to-image",
#         "huggingface-tools/text-to-video",
#         "text-to-speech",
#         "huggingface-tools/text-download",
#         "huggingface-tools/image-transformation",
#     ]
# ]

# # Create the agent
# agent = HuggingGPT(llm, hf_tools)

# # Title
# st.title('EurekaX')

# # Create survey form
# def create_survey(text):
#     # LangChain analyze text
#     questions = agent.run(text)

#     # Make survey form
#     survey = []
#     for question in questions:
#         if isinstance(question, dict) and "type" in question:
#             if question["type"] == "text":
#                 survey.append(st.text_input(question["label"]))
#             elif question["type"] == "choice":
#                 survey.append(st.selectbox(question["label"], question["options"]))
#             elif question["type"] == "check button":
#                 survey.append(st.checkbox(question["label"], question["options"]))
#             elif question["type"] == "radio button":
#                 survey.append(st.radio(question["label"], question["options"]))
#         else:
#             st.warning(f"Invalid question format: {question}")

#     return survey

# # Main UI
# def main():
#     # Input UI form from text
#     text = st.text_input("Input your survey details. AI makes a form from them:")

#     # Generate survey from text
#     survey = create_survey(text)

#     # Show survey UI
#     st.write(survey)

# # Start program
# if __name__ == "__main__":
#     main()
import streamlit as st
from langchain.llms import OpenAI
from transformers import load_tool
from langchain_experimental.autonomous_agents import HuggingGPT
import matplotlib.pyplot as plt

# Set OpenAI API key
OpenAI.api_key = "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"  # Replace with your actual API key

# Create LangChain agent
llm = OpenAI(model_name="gpt-3.5-turbo")

# Define the hf_tools list
hf_tools = [
    load_tool(tool_name)
    for tool_name in [
        "document-question-answering",
        "image-captioning",
        "image-question-answering",
        "image-segmentation",
        "speech-to-text",
        "summarization",
        "text-classification",
        "text-question-answering",
        "translation",
        "huggingface-tools/text-to-image",
        "huggingface-tools/text-to-video",
        "text-to-speech",
        "huggingface-tools/text-download",
        "huggingface-tools/image-transformation",
    ]
]

# Create the agent
agent = HuggingGPT(llm, hf_tools)

# Title
st.title('EurekaX')

# Create survey form
def create_survey(text):
    # LangChain analyze text
    questions = agent.run(text)

    # Make survey form
    survey = {}
    for question in questions:
        if isinstance(question, dict) and "type" in question:
            if question["type"] == "text":
                survey[question["label"]] = st.text_input(question["label"])
            elif question["type"] == "choice":
                survey[question["label"]] = st.selectbox(question["label"], question["options"])
            elif question["type"] == "check button":
                survey[question["label"]] = st.checkbox(question["label"], question["options"])
            elif question["type"] == "radio button":
                survey[question["label"]] = st.radio(question["label"], question["options"])
        else:
            st.warning(f"Invalid question format: {question}")

    return survey

# Main UI
def main():
    # Input UI form from text
    text = st.text_input("Input your survey details. AI makes a form from them:")

    # Generate survey from text
    survey = create_survey(text)

    # Show survey UI
    st.write(survey)

# Start program
if __name__ == "__main__":
    main()
