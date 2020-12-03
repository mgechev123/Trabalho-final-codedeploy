#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
     return 'a'
 #   return ("Hello, World!"      
  #         + "<br><br><br><br>Apresentacao trabalho final!"
   #        + "<br><br><br><br>TESTE")
