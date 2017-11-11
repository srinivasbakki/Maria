# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:49:40 2017

@author: sbakki
From scratch -code mostly picked from 
https://tsaprailis.com/2016/06/02/How-to-build-and-deploy-a-Facebook-Messenger-bot-with-Python-and-Flask-a-tutorial/

This will be incremental building - to learn how this interfaces with facebook
Steps:
    
1) Host a Heroku application and just print out a Hello world type string: Check
2) Just put in GET method and check the behavior: Nothing happened! 
3) Just check if the print works or only return: 
    
"""

from flask import Flask, request
import json
import requests

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
#PAT = ''


@app.route('/', methods=['GET'])
def handle_verification():
    return"Handling verification."
    
if __name__ == '__main__':
    app.run()
    