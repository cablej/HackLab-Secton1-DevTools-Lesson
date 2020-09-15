from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/super_secret_password/tas_only/do_not_enter/password', methods=['GET'])
def super_secret_password():
    return 'super_secret_password'
    
if __name__ == '__main__':
    app.debug=True
    app.run()
