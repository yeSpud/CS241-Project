from flask import render_template, Flask
import sys

app = Flask(__name__)
app.config["DEBUG"] = True


def startup():

    # Check for valid command line arguments
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python3 App.py <local IP> <remote IP> [stream IP]")
        return

    # TODO Get current local IP
    print(f"Local IP: {sys.argv[1]}\nRemote IP: {sys.argv[2]}")

    # TODO Try getting MJPEG from optional argument

    # TODO Start app
    #app.run(port=80, host=)
    app.run(port=80)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")


@app.errorhandler(404)
def error404(err):
    return render_template("404.html"), 404


if __name__ == "__main__":
    startup()
