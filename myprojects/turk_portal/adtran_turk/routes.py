from flask import render_template, url_for, flash, redirect
from flask_paginate import Pagination, get_page_args
from adtran_turk import app

tasks = [

{'requester' : 'pasupathi',
'task_summary' : 'Need python parser for the defenscics results',
'task_id' : 'AD-00000',
'reward_points' : 10,
'date_created' : 'Oct 20, 2019',},

{'author' : 'thumbur',
'task_summary' : 'Optimize 4xx ONT framework',
'task_id' : 'AD-00001',
'reward_points' : 20,
'date_created' : 'Oct 21, 2019',}
]


@app.route("/")
def main():
	return render_template('main.html')

@app.route("/about")
def about():
	return render_template('about.html', title = 'About')