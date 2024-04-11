from flask import Flask, render_template, request

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
    
    # Return the response message
    return response

if __name__ == '__main__':
    app.run(debug=True)
