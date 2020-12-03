#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
 return unicode("インスタントグラム","UTF-8")
    #return ("Hello, World!"      
     #      + "<br><br><br><br>Apresentação do trabalho final..."
      #     + "<br><br><br><br>")
