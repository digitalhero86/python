from flask import Flask, redirect, session, g, redirect, request, url_for, abort, render_template, flash
#create webapplication
app = Flask(__name__)
#Default Config
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
    ))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print request.form['twenty']
        return render_template('result.html', twentys=twentys, tens=tens)
if __name__ == '__main__':
    app.run()


credit_slips = input ("What is the total amount of credit slips? ")
tips = input ("What is the total amount of tips? ")
supplies = input ("Put receipt into envelope, What is the total amount of supplies? ")
tape_total = input ("Total amount on tape? ")
test = (credit_slips + tips + supplies)
net_total = tape_total - test

a = 0
while a != 1:

    #twenty = input ("How many $20 do you have? ")
    twenty = ['twenty']
    twenty_amount = 20.00
    total_twenty = twenty_amount * twenty

    ten = input ("How many $10 do you have? ")
    ten_amount = 10.00
    total_ten = ten_amount * ten

    five = input ("How many $5 do you have? ")
    five_amount = 5.00
    total_five = five * five_amount

    one = input ("How many $1 do you have? ")
    one_amount = 1.00
    total_one = one_amount * one

    quarter = input ("How many $0.25 do you have? ")
    quarter_amount = .25
    total_quarter = quarter * quarter_amount

    dime = input ("How many $.010 do you have? ")
    dime_amount = .10
    total_dime = dime * dime_amount

    nickel = input ("How many $0.05 do you have? ")
    nickel_amount = .05
    total_nickel = nickel * nickel_amount

    penny = input ("How many $0.01 do you have? ")
    penny_amount = .01
    total_penny = penny * penny_amount

    total_amount = (total_twenty + total_ten + total_five + total_one + total_quarter + total_dime + total_nickel + total_penny)

    if int (net_total) == int (total_amount):
        print "CORRECT!!"
        print "The total amount of cash you have is: " + int(total_amount) 
        morning_till = 175
        bag_money = total_amount - morning_till
        print "Please put " + int (bag_money) + " in the bank bag."
        a +=1
    else:
        balance_difference = int(tape_total) - int(total_amount)
        print "You need to recount your money. You are off by: " + int(balance_difference)
