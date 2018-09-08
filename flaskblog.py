from flask import Flask
# __name__ is the name of module
# so flask knows where to look for static files
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1> Home Page </h1>"

@app.route("/about")
def about():
    return "<h1> About Page </h1>"



# alterative to using environment variables
if __name__ == '__main__':
    app.run(debug=True)