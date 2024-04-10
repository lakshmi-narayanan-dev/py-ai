from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def gemini():
    return render_template('gemini.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['input_data']
    # Here you can do whatever you want with the received data
    # For example, print it
    print("Received data:", data)
    # Or you can write it to a file
    with open('data.txt', 'w') as file:
        file.write(data)
    return 'Data received successfully'

if __name__ == '__main__':
    app.run(debug=True)
