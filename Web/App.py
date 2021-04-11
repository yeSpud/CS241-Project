from flask import render_template, Flask, request
from sys import argv

app = Flask(__name__)
app.config["DEBUG"] = True

remoteIP: str = ""
mjpegIP: str = ""


def startup():

    # Check for valid command line arguments
    if len(argv) > 4 or len(argv) < 3:
        print("Usage: python3 App.py <local IP> <remote IP> [stream IP]")
        return

    # Get current local and IPs
    localIP = argv[1]
    global remoteIP
    remoteIP = argv[2]
    print(f"Local IP: {localIP}\nRemote IP: {remoteIP}")

    # Try getting MJPEG from optional argument
    if len(argv) == 4:
        global mjpegIP
        mjpegIP = argv[3]
        print(f"mjpeg stream IP: {mjpegIP}")

    # Start app
    app.run(port=80, host=localIP)


@app.route('/', methods=["GET"])
def index():
    print(remoteIP)
    if request.remote_addr == remoteIP:
        return render_template("oldindex.html", mjpeg=mjpegIP)
    else:
        return error403(None)


@app.errorhandler(403)
def error403(err):
    return render_template("403.html"), 403


@app.errorhandler(404)
def error404(err):
    return render_template("404.html"), 404


if __name__ == "__main__":
    startup()


