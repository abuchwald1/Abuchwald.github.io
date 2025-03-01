from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Your Python code to get data or perform tasks
    message = "Welcome to my website!"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
