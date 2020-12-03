#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
 #return unicode("　|Ｔ￣て￣￣`ー-<","UTF-8")
return unicode("<br><br><br><br> ＿　　　　　　　　／<br>　|Ｔ￣て￣￣`ー-<<br>　|｜　　￣＼　　 ヽ<br>　|/　　　 ＼＼　 _|<br>＿|＼_＿　､＼＼)／L|／<br>　　(_(_＼_)_)ﾉ","UTF-8")
    #return ("Hello, World!"      
     #      + "<br><br><br><br>Apresentação do trabalho final..."
      #     + "<br><br><br><br>")
