#!/usr/bin/python
# vim: set expandtab:
 
from flask import Flask, flash, abort, redirect, url_for, request, render_template, make_response, json, Response
import os, sys
 
app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		credit_slips = int(request.form['credit_slips'])
		tips  = int(request.form['tips'])
		supplies  = int(request.form['supplies'])
		tape_total  = request.form['tape_total']
		total_credits = credit_slips + tips + supplies
		net_total = float(tape_total) - float(total_credits)
		return render_template('cash.html', credit_slips=credit_slips, tips=tips, supplies=supplies, tape_total=tape_total, net_total=net_total)
	return render_template('index.html')	

@app.route('/', methods=['GET', 'POST'])
def cash():
	if request.method == 'POST':
		hundred = int(request.form['hundred'])
                hundred_total = int(hundred) * 100.00
                fifty = int(request.form['fifty'])
                fifty_total = int(fifty) * 50.00
                twenty = int(request.form['twenty'])
                twenty_total = int(twenty) * 20.00
                ten = int(request.form['ten'])
                ten_total = int(ten) * 10.00
                five  = int(request.form['five'])
                five_total = int(five) * 5.00
                one  = int(request.form['one'])
                one_total = int(one) * 1.00
                quarter  = int(request.form['quarter'])
                quarter_total = int(quarter) * 0.25
                dime  = int(request.form['dime'])
                dime_total = int(dime) * 0.10
                nickel  = int(request.form['nickel'])
                nickel_total = int(nickel) * 0.05
                penny  = int(request.form['penny'])
                penny_total = int(penny) * 0.01
                total_amount = (hundred_total + fifty_total + twenty_total + ten_total + five_total + one_total + quarter_total + dime_total + nickel_total + penny_total)
		return render_template('result.html', credit_slips=credit_slips, tips=tips, supplies=supplies, tape_total=tape_total, total_credits=total_credits, net_total=net_total, hundred=hundred, hundred_total=hundred_total, fifty=fifty,fifty_total=fifty_total, twenty = twenty,twenty_total=twenty_total, ten=ten,ten_total=ten_total, five=five,five_total=five_total, one=one, one_total=one_total, quarter=quarter, quarter_total=quarter_total, dime=dime, dime_total=dime_total, nickel=nickel, nickel_total=nickel_total, penny=penny, penny_total=penny_total, total_amount=total_amount)
	return render_template('index.html')
 
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
