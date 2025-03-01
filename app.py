from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# You can add more routes here if needed
@app.route('/api/get-data')
def get_data():
    # Example of Python logic or data fetching
    data = {"message": "Hello from Python!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
