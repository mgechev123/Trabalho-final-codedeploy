from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!A implantacao automatica do codigo funcionou!'
