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
        return render_template('result.html', twenty=twenty, ten=ten)

if __name__ == '__main__':
    app.run()
