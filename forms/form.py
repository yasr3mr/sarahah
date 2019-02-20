from wtforms import Form,StringField,PasswordField,TextAreaField,validators


class UserForm(Form):
	name = StringField('Name',[validators.Length(min=3,max=250),validators.DataRequired()])
	username = StringField('Username',[validators.Length(min=3,max=250),validators.DataRequired()])
	email = StringField('Email',[validators.Length(max=250),validators.DataRequired()])
	password = PasswordField('Password',[validators.Length(min=3,max=250),validators.DataRequired(),validators.EqualTo('confirm',"Passwords Not Match")])
	confirm = PasswordField('Confirm Password',[validators.Length(min=3,max=250)])


class MessagesForm(Form):
	message = TextAreaField('Message',[validators.DataRequired(),validators.Length(min=10,max=250)])
	