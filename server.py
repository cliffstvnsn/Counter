from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'



@app.route("/")
def counterButton():
    if 'counter' in session:
        session["counter"] += 1
        print(session)
    else:
        session['counter'] = 1
    return render_template("index.html")

@app.route("/add2")
def add2():
    if 'counter' in session:
        session['counter'] += 1
        print(session)
    return redirect("/")

@app.route('/clearNumber')
def delete_cookies():
    session.clear()
    print(session)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)