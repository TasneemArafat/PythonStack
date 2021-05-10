from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def Hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say_name(name):
    return f"Hi {name}!"

@app.route("/repeat/<times>/<word>")
def repeat_word(times,word):
    return render_template("index.html",repeat=int(times),word_typed=word)

@app.errorhandler(404)
def errormessage(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)