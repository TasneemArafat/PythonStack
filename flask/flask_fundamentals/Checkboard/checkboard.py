from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<int:row>')
@app.route('/<int:row>/<int:column>')
@app.route('/<int:row>/<int:column>/<color1>/<color2>')
def index(row = 8,column = 8, color1 = "red", color2 = "black"):
    return render_template("home.html",row_num=row,col_num=column,color_1 = color1, color_2 = color2)

if __name__=="__main__":
    app.run(debug=True)