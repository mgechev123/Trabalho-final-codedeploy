from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return ("Hello, World!"      
           + "<br><br><br><br>Apresentacao trabalho final!"
           + "<br><br><br><br>TESTE")
