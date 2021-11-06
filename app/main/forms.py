from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,RadioField,TextAreaField
from wtforms.validators import Required
from wtforms import ValidationError
from  ..models import User


class PitchForm(FlaskForm):
    category = RadioField('Category:', choices=[('PickUP','pickup'),('Interview','interview'),('Product','product'),('Promotion','promotion')])
    # title = StringField('Title:',validators=[Required()])
    content = TextAreaField('Content:',validators=[Required()])
    submit = SubmitField('Post')
    