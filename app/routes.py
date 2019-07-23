from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/results', methods = ["GET","POST"])
def results():
    if request.method == "GET":
        return redirect("/index")
    else:
        print(request.values)
        gems = ["Garnet", "Amethyst", "Aquamarine", "Diamond", "Emerald", "Pearl", "Ruby", "Peridot", "Sapphire", "Opal", "Topaz", "Turquoise"]
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        print(request.form)
        if "month" not in request.form:
            return redirect("/")

        gem = request.form["month"]
        link = ""
        month = ""

        for g in gems:
            if g == gem:
                link = "static/" + g.lower() + ".png"
                month = months[gems.index(g)]

        return render_template('results.html', gem = gem, month = month, link = link)