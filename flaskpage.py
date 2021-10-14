from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', )"

#class Entries(db.Model):
  #  id = db.Column(db.Integer)
  #  waste_amount = db.Column(db.Integer)
  #  paper = db.Column(db.Integer)
  #  food_waste = db.Column(db.Integer)
  #  metal = db.Column(db.Integer)
  #  plastic = db.Column(db.Integer)
   # glass = db.Column(db.Integer)
   # organic = db.Column(db.Integer)
  #  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow

    #def __repr__(self):
     #   return f"Entries('{self.waste_amount}', '{self.date}', )"


entries = [
    {
        'username'  :  'Max Mustermann',
        'date': 'April 20, 2021',
        'waste_amount' : '6kg' ,
        'paper' : '0,2kg' ,
        'metal' :   '2kg' ,
        'plastic' : '0,15kg' ,
        'glass' : '2,2kg',
        'organic' : '1,45kg'
    },

    {
        'username'  :  'Erika Musterman',
        'date_posted': 'October 12, 2021',
        'waste_amount' : '13kg' ,
        'paper' : '0,2kg' ,
        'metal' :   '4kg' ,
        'plastic' : '0,15kg' ,
        'glass' : '2,2kg',
        'organic' : '2,45kg'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About Us')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':

    app.run(port=1337, debug=True)
