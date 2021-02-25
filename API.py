from flask import render_template, Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=["GET"])
def index():

    rgbList = []
    for B in [0, 1]:
        for G in [0,1]:
            for R in [0,1]:
                rgbList.append((R*255, G*255, B*255))

    return render_template("index.html", colorArray=rgbList)


@app.errorhandler(404)
def error404(err):
    return render_template("404.html"), 404


app.run(port=80)
