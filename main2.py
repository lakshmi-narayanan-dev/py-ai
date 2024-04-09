from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired
import os
import docx2txt
import langchain.prompts as prompts
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from pathlib import Path
import langchain.prompts as prompts

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'Static/Files'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    input1 = StringField("Input 1", validators=[DataRequired()])
    submit = SubmitField("Ask Us!")

@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"]) 
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file =  form.file.data #First Get the data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename("CONTEXT.docx"))) #save the file
        my_file = Path("/home/anisiva/py-ai/Static/Files/CONTEXT.docx")
        if my_file.exists():
            text = docx2txt.process("/home/anisiva/py-ai/Static/Files/CONTEXT.docx") 
            #print(text)
            #prompt_value = "What is this document about?"
            prompt_value = request.form.get('input1')
            question = prompt_value
            print(question)
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

        return response
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    

