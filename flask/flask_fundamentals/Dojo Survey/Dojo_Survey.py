from flask import Flask, render_template, request, redirect 
app = Flask(__name__)
@app.route('/')
def form_page():
    return render_template("form.html")

@app.route('/show', methods=['POST'])
def process():
    print("GOT POST INFO")
    print(request.form)
    user_name = request.form['name']
    gender=request.form['gender']
    courses=request.form.getlist('courses')
    user_location = request.form['location']
    user_fav_lang = request.form['languages']
    user_comment = request.form['comment']
    return render_template('show.html',Name=user_name, gender=gender, courses=courses, Location=user_location, Language = user_fav_lang, Comment = user_comment)

if __name__=="__main__":
    app.run(debug=True)
