from flask import Flask, render_template, url_for

app= Flask(__name__, static_url_path='/static')

@app.route("/404")
def master():
    return render_template('master.html')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',  methods=['GET', 'POST'])    

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/registration")
def registration():
    return render_template('registration.html')

@app.route("/regi")
def regi():
    return render_template('regi.html')

@app.route("/add")
def add():
    return render_template('add.html')



if __name__ == '__main__':
    app.run(debug=True)