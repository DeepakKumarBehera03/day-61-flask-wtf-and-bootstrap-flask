from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "Deepak"


class MyForm(FlaskForm):
    name = StringField(label="name", validators=[DataRequired()])
    gmail = EmailField(label="gmail", validators=[DataRequired()])
    date = DateField(label="DOB", validators=[DataRequired()])
    Password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        print(f"Name : {login_form.name.data}")
        print(f"Email : {login_form.gmail.data}")
        print(f"Password : {login_form.Password.data}")
        print(f"DOB : {login_form.date.data}")
        if login_form.name.data == "Deepak" and login_form.gmail.data == "deepakjgrt99@gmail.com":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
