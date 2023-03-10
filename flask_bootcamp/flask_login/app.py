from flask import Flask,render_template,flash,abort,url_for,redirect,request
from myproject import app, db
from flask_login import login_user,login_required,logout_user
from myproject.models import Userfrom
from myproject.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash
from myproject.models import User

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
@login_required  #this will redirect to login page
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user=user.query.filter_by(email=form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully!')
            next=request.args.get('next')
            if next == None or not next[0] == '/':
                next=url_for('home')
    return render_template('login.html',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('login'))
    return render_template('home.html', form=form)




if __name__ == "__main__":
    app.run(debug=True)