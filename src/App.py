from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@127.0.0.1:3306/slice2'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:computacao@127.0.0.1:3306/slice2'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:computacao@localhost:3306/slice2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:computacao@0.0.0.0:3306/slice2'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:computacao@172.28.0.1:3306/slice2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    key = db.Column(db.Integer)
    value = db.Column(db.Float)

    def __init__(self, value, key):
        self.key = key
        self.value = value


#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", employees = all_data)



#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        value = request.form['value']
        key = request.form['key']

        my_data = Data(key, value)

        db.session.add(my_data)
        db.session.commit()

        flash("Inserted Successfully")

        return redirect(url_for('Index'))

#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.value = request.form['value']
        my_data.key = request.form['key']

        db.session.commit()
        flash("Updated Successfully")

        return redirect(url_for('Index'))

#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Deleted Successfully")

    return redirect(url_for('Index'))

#if __name__ == "__main__":
#   app.run(debug=True)
