from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from wtforms.validators import Length,EqualTo, Email, DataRequired, ValidationError # type: ignore
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):  # must be validate_username 
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("UserName already exists! PLease try another name")
    def validate_email(self, email_to_check):
        email_addr = User.query.filter_by(email=email_to_check.data).first() 
        if email_addr:
            raise ValidationError("Email already exists! PLease try another email")

    username = StringField(label="User Name:", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email Address:", validators=[Email(), DataRequired()])
    password1 = PasswordField(label="Password:", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password::', validators=[DataRequired()])
    submit = SubmitField(label="Sign In")



class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label="Purchase Item!")

class SellItemForm(FlaskForm):
    submit = SubmitField(label="Sell Item!")