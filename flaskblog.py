from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
# __name__ is the name of module
# so flask knows where to look for static files
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

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

@app.route("/register")
def register():
    # create an instance
    form = RegistrationForm()
    return render_template('register.html', title='Register',form=form)

@app.route("/login")
def login():
    # create an instance
    form = LoginForm()
    return render_template('login.html', title='Login',form=form)


# alterative to using environment variables
if __name__ == '__main__':
    app.run(debug=True)