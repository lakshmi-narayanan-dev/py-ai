from flask import Flask, render_template
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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'Static/Files'

class UploadFileForm(FlaskForm):
    file = FileField("File")

 # Additional input fields
    input1 = StringField("Input 1", validators=[DataRequired()])
    # input2 = StringField("Input 2", validators=[DataRequired()])

    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods=['GET', "POST"]) 
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file =  form.file.data #First Get the data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename("CONTEXT.docx"))) #save the file
        my_file = Path("/home/n6ine-dev/Downloads/Py-H-C/Static/Files/CONTEXT.docx")
        if my_file.exists():
            text = docx2txt.process("/home/n6ine-dev/Downloads/Py-H-C/Static/Files/CONTEXT.docx") 
            print(text)
        return "File Has Been Uploaded"
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
