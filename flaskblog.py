from flask import Flask, render_template, url_for
# __name__ is the name of module
# so flask knows where to look for static files
app = Flask(__name__)

posts = [
    {
        'author': 'Denise Leviste',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 8, 2018'
    },
    {
        'author': 'Jeraldyn Leviste',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 9, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')



# alterative to using environment variables
if __name__ == '__main__':
    app.run(debug=True)