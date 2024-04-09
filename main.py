# pip install eel

import eel
import docx2txt
import langchain.prompts as prompts
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

eel.init('UI')

@eel.expose
def App():
    print('Application Running Sucessfully')
  
App()

 # Extract text from DOCX or TXT file
text = docx2txt.process("./Understanding-NSCLC-Pathophysiology_020924_Final.docx") 
#print(text)

prompt_value = "What is your name?"
question = prompt_value

# Do something with the extracted text (e.g., store it, analyze it, etc.)

# def ask_question(question, document_text):
#     qa_prompt = prompts.PromptTemplate(
#         input_variables=["question", "context_str", "length"],
#         template="Imagine you are a Human Resource Manager."
#                 "Your task is to provide the detail accurate answer from the provided context."
#                 "Get me each answers with point wise"
#                 "Make sure to add the required words in the output."
#                 "Write an answer within ({length}) words for the question below based on the provided context. "
#                 "Try not to alter the content as much as possible."
#                 "The answer must be short and based on the question asked to you"
#                 "If provided context does not have sufficient information with regards to Question,Then reply 'Reference materials not located. Reformulate your question using the tips from the user guide for a precise answer.'"
#                 "Context: {context_str}\n"
#                 "Question: {question}\n"
#                 "Answer: ",
#     )
#     qa_chain = LLMChain(llm=ChatOpenAI(temperature=0.0, model_name='gpt-3.5-turbo-0125',
#                                       openai_api_key='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'), prompt=qa_prompt)
#     answer = qa_chain.run({"question": question, "context_str": document_text, "length": 80})
#     return f'{answer}'

# response = ask_question(question, text)
# print(response)

eel.start('index.html')
