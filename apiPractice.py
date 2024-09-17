from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
# Define a route for the API
@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name}! Hope you're having a great day!")

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'GET':
        return jsonify(message="This is a POST request")
    else:
        return jsonify(message="This is a GET request")
 
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    name = request.form.get('name')
    return jsonify(message=f"Thank you, {name}!")
 
if __name__ == '__main__':
    app.run(debug=True)


