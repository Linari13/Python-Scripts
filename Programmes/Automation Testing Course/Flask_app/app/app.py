from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello, world!'}) #jsonify turns the dictionary into a valid json string

if __name__ == '__main__':
    app.run()

