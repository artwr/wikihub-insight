from flask import render_template, jsonify
from flask import request, Response
from app import app
from helpers import getYearlyData
from helpers import getMonthlyData
from helpers import getDailyData
import json
#from starbase import Connection
import happybase

# db = mdb.connect(user="api", host="127.0.0.1", passwd="msqlapi", db="gdelt", charset='utf8')
# c = Connection(host='127.0.0.1', port=7070)
# t1 = c.table('wikiedits')
# t2 = c.table('wikieditssmall')


# ROUTING/VIEW FUNCTIONS
@app.route('/')
@app.route('/index')
def index():
    # Renders index.html.
    return render_template('index.html')

@app.route('/author')
def contact():
    # Renders author.html.
    return render_template('author.html')

@app.route('/page/', methods=['GET'])
def page(): 
    qs = request.query_string 
    titleparam = request.args.get("title")
    yearly_data = getYearlyData(titleparam)
    datastr = str(yearly_data)
    count2011 = yearly_data.get(2011,"")
    return qs + " " + str(count2011)

@app.route('/demo', methods=['GET'])
def demo():
    # Renders demo.html.
    return render_template('demo.html')

@app.route('/test/', methods=['GET'])
def test():
    return request.query_string + "\n<br>\n" + request.args.get("user")
    

@app.route('/api/page/<string:title>', methods=['GET'])
def api():
    qs = request.query_string
    titleparam = request.args.get("title")
    yearly_data = getYearlyData(titleparam)
    # Queries the DB and returns data
    # cur = db.cursor()   
    return jsonify(yearly_data)

# @app.route('/api/top', methods=['GET'])
# def api():
#     # Queries the DB and returns data
#     # cur = db.cursor()   
#     return render_template('api.html')