from flask import Flask, jsonify, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def super_secret_password():
    return jsonify({'super_secret_password': 'jacked cable'})
    
if __name__ == '__main__':
    app.debug=True
    app.run()
