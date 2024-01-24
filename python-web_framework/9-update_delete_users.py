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
            name = request.form.get('name')
            email = request.form.get('email')

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

# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        flash('User not found!', 'error')
        return redirect(url_for('display_users'))

    if request.method == 'POST':
        try:
            # Extract the updated name and email from the form data
            new_name = request.form.get('name')
            new_email = request.form.get('email')

            # Validate the data: ensure both fields are provided
            if not new_name or not new_email:
                flash('Both name and email are required.', 'error')
            else:
                # Update the corresponding user in the User table
                user.name = new_name
                user.email = new_email
                db.session.commit()
                flash('User updated successfully!', 'success')
        except IntegrityError as e:
            db.session.rollback()
            flash('Error: Email address already taken.', 'error')
        except Exception as e:
            db.session.rollback()
            flash('Error updating user. Please try again.', 'error')

    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        flash('User not found!', 'error')
        return redirect(url_for('display_users'))

    if request.method == 'POST':
        try:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully!', 'success')
            return redirect(url_for('display_users'))
        except Exception as e:
            db.session.rollback()
            flash('Error deleting user. Please try again.', 'error')

    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
