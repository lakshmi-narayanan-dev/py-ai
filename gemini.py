from flask import Flask, render_template, request
import docx2txt
import langchain.prompts as prompts
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from pathlib import Path
import langchain.prompts as prompts


app = Flask(__name__)

@app.route('/')
def gemini():
    return render_template('gemini.html')

@app.route('/submit', methods=['POST'])
def submit():
     # Get the question data from the form
    question = request.form['input_data']
    
    # Generate a demo response message
    response = "This is a demo response to the question: " + question
    
     # Print the response message in the terminal
    #  
    print("The Question is:", question)
    text = docx2txt.process("/home/anisiva/py-ai/Static/Files/CONTEXT.docx") 

    def ask_question(question, document_text):
        qa_prompt = prompts.PromptTemplate(
        input_variables=["question", "context_str", "length"],
        template="Imagine you are a Human Resource Manager."
                 "Your task is to provide the detail accurate answer from the provided context."
                 "Get me each answers with point wise"
                 "Make sure to add the required words in the output."
                 "Write an answer within ({length}) words for the question below based on the provided context. "
                 "Try not to alter the content as much as possible."
                 "The answer must be short and based on the question asked to you"
                 "If provided context does not have sufficient information with regards to Question,Then reply 'Reference materials not located. Reformulate your question using the tips from the user guide for a precise answer.'"
                 "Context: {context_str}\n"
                 "Question: {question}\n"
                 "Answer: ",
                )
        qa_chain = LLMChain(llm=ChatOpenAI(temperature=0.0, model_name='gpt-4-1106-preview',
                                    openai_api_key=''), prompt=qa_prompt)
        answer = qa_chain.run({"question": question, "context_str": document_text, "length": 80})
        return f'{answer}'

    response = ask_question(question, text)
    print(response)
    
    # Return the response message
    return response



        









if __name__ == '__main__':
    app.run(debug=True)
