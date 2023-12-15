from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed


class InputImageForm(FlaskForm):
    image = FileField('Image', validators=[
        FileRequired(), FileAllowed(['jpg', 'jpeg', 'img', 'png'])])
    submit = SubmitField('Confirm')