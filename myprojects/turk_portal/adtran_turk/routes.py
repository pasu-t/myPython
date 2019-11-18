from flask import render_template, url_for, flash, redirect
from flask_paginate import Pagination, get_page_args
from adtran_turk import app

tasks_list = [

{'Requester' : 'pasupathi',
'Task Summary' : 'Need python parser for the defenscics results Need python parser for the defenscics results Need python parser for the defenscics results',
'Reward_Points' : 10,
'status' : 'pending',
'Task_Id' : 'AD-00000',},

{'Requester' : 'thumbur',
'Task Summary' : 'Optimize 4xx ONT framework',
'Reward_Points' : 20,
'status' : 'in progress',
'Task_Id' : 'AD-00001',}
]

@app.route("/")
def home():
	return render_template('home.html', tasks_list=tasks_list)

@app.route("/about")
def about():
	return render_template('about.html', title = 'About')