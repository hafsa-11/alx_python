from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alx_flask_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()

            flash('User added successfully!', 'success')
        except IntegrityError as e:
            db.session.rollback()
            flash('Error: Email address already exists.', 'error')
        except Exception as e:
            db.session.rollback()
            flash('Error adding user. Please try again.', 'error')

    return render_template('add_user.html')

@app.route('/users')
def display_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
