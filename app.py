from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
