from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
@app.route('/play/<x>')
@app.route('/play/<x>/<color>')
def level_3(x=3,color="blue"):
    return render_template("index.html",repeat=int(x),box_color=color)

if __name__ == "__main__":
    app.run(debug=True)
