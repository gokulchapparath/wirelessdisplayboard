from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def defpage():
    return '''
    <html>
    <head>
    <body>
    <h1>WELCOME TO WIRELESS NOTICE BOARD<h1>
    </body>
    </head>
    </html>
    '''

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/registration")
def registration():
    return render_template('registration.html')
@app.route("/request")
def request():
    return render_template('request.html')


if __name__ == '__main__':
    app.run(debug=True)