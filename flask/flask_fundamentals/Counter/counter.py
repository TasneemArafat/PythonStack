from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="Shhh!!"


@app.route('/')
def home():
    if 'times' in session:
        session['times'] +=1

    else:
        session['times']=1

    return render_template("home.html",visits=session['times'])

@app.route('/destroy_session', methods=['GET','POST'])
def destroy():
    session.clear()
    return redirect('/')   

@app.route('/plus_2',methods=['POST'])
def plus_2():
    if 'times' in session:
        print("Yes")
        session['times'] +=1
        # session['counter']+=1
    else:
        session['times']=1
        # session['counter']=1
    return redirect('/')

@app.route('/increment',methods=['POST'])
def pincrement():
    if 'times' in session:
        session['times'] +=int(request.form['increment']) - 1
        # session['counter'] +=int(request.form['increment']) - 1
    else:
        session['times']=int(request.form['increment'])
        # session['counter']=int(request.form['increment'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)