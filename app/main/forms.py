from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,RadioField,TextAreaField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    category = RadioField('Category:', choices=[('PickUP','pickup'),('Interview','interview'),('Product','product'),('Promotion','promotion')])
    content = TextAreaField('Content:',validators=[Required()])
    submit = SubmitField('Post')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment:',validators=[Required()])
    submit = SubmitField('Post')
    
class AddBioForm(FlaskForm):
    bio = TextAreaField('Bio:',validators=[Required()])
    submit = SubmitField('Post')
    