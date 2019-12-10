from flask_wtf import FlaskForm
from wtforms import SubmitField

from flask_wtf.file import FileField, FileRequired


class AnchorPhotoForm(FlaskForm):
    photo = FileField('Anchor Photo', validators=[FileRequired()])
    submit_anchor = SubmitField('Upload photo')


class TestPhotoForm(FlaskForm):
    photo = FileField('Test Photo', validators=[FileRequired()])
    submit_test = SubmitField('Upload photo')
