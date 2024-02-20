from wtforms import Form
from wtforms import StringField, TelField, IntegerField

from wtforms import EmailField
from wtforms.validators import DataRequired, Email

class Nombres(Form):
    Nom1= StringField('Nombre 1')
    Nom2 = StringField("Nombre 2")