#!/usr/bin/python
# vim: set expandtab:
from pymongo import MongoClient 
from flask import Flask, flash, abort, redirect, url_for, request, render_template, make_response, json, Response, jsonify
import os, sys
import datetime

app = Flask(__name__)

def mongo_db():
	client = MongoClient()
	db = client.till_database
	return db 
def mongo_receipts():
	db = mongo_db()
	col = db.receipts
	return col
def mongo_cash():
	db = mongo_db()
	col = db.cash
	return col
 
@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
		col = mongo_receipts()
                credit_slips = int(request.form['credit_slips'])
                tips = int(request.form['tips'])
                supplies = int(request.form['supplies'])
                tape_total = request.form['tape_total']
                total_credits = credit_slips + tips + supplies
                net_total = float(tape_total) - float(total_credits)
#Here I post my results of the form as well as a couple of calculations into my collection mongo_receipts
		post = {"date": datetime.datetime.now(),
			"credit_slips" : credit_slips,
			"tips": tips,
			"supplies": supplies,
			"tape_total": tape_total,
			"total_credits" : total_credits,
			"net_total" : net_total} 
		post_id = col.insert(post)
                return render_template('cash.html')
        return render_template('index.html')        

@app.route('/test-receipts/')
def test():
	col = mongo_receipts()
	json_data = []
	results = col.find({},{'_id':0})	
	for result in results:
		json_data.append(result)
	return jsonify({'output': json_data})
@app.route('/test-cash/')
def testcash():
	col = mongo_cash()
	json_data = []
	results = col.find({},{'_id':0}).sort({date: -1})
	for result in results:
		json_data.append(result)
	return jsonify({'output': json_data})
@app.route('/result/')
def results():
	receipt_result = col.mongo_receipt
	tc = receipt_result['key2']
	
	

@app.route('/cash', methods=['GET', 'POST'])
def cash():
        if request.method == 'POST':
		col = mongo_cash()
                hundred = int(request.form['hundred'])
                hundred_total = hundred * 100.00
                fifty = int(request.form['fifty'])
                fifty_total = int(fifty) * 50.00
                twenty = int(request.form['twenty'])
                twenty_total = int(twenty) * 20.00
                ten = int(request.form['ten'])
                ten_total = int(ten) * 10.00
                five = int(request.form['five'])
                five_total = int(five) * 5.00
                one = int(request.form['one'])
                one_total = int(one) * 1.00
                quarter = int(request.form['quarter'])
                quarter_total = int(quarter) * 0.25
                dime = int(request.form['dime'])
                dime_total = int(dime) * 0.10
                nickel = int(request.form['nickel'])
                nickel_total = int(nickel) * 0.05
                penny = int(request.form['penny'])
                penny_total = int(penny) * 0.01
                total_amount = (hundred_total + fifty_total + twenty_total + ten_total + five_total + one_total + quarter_total + dime_total + nickel_total + penny_total)
		
		post = {"date": datetime.datetime.now(),
			"hundred" : hundred_total,
			"fifty" : fifty_total,
			"twenty" : twenty_total,
			"ten" : ten_total,
			"five" : five_total,
			"one" : one_total,
			"quarter" : quarter_total,
			"dime" : dime_total,
			"nickel" : nickel_total,
			"penny" : penny_total,
			"total_amount" : total_amount}
		post_id = col.insert(post)
                return render_template('result.html')
        return render_template('cash.html')
 
if __name__ == "__main__":
        app.debug = True
        app.run(host='0.0.0.0')
