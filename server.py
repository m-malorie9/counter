from flask import Flask, render_template, redirect, session
app = Flask(__name__)   
app.secret_key = '1234'

@app.route('/')
def main():
    if "counter" not in session:
        session["counter"] = 0

    else:
        session["counter"] += 1
    return render_template('index.html', session = session["counter"])

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/addtwo')
def add_two():
    session["counter"] +=1
    return redirect('/')




if __name__=="__main__":
    app.run(debug=True)