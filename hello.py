#!/usr/bin/env python
# -*- coding: utf-32 -*-
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
     #return 'aáãç'
    #return ("Hello, World!"      
           #+ "<br><br><br><br>Apresentação do trabalho final..."
           #+ "<br><br><br><br>TESTE")
return 'インスタントグラム'
