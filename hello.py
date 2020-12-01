from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return utf8_encode('Hello, World!<br><br>Teste apresentacao trabalho final!<br><br><br><br> ＿　　　　　　　　／<br>　|Ｔ￣て￣￣`ー-<<br>　|｜　　￣＼　　 ヽ<br>　|/　　　 ＼＼　 _|<br>＿|＼_＿　､＼＼)／L|／<br>　　(_(_＼_)_)ﾉ');
