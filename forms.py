from wtforms import Form
from wtforms import StringField, TelField, IntegerField

from wtforms import EmailField
from wtforms.validators import DataRequired, Email


class Coordenadas(Form):
    coordenadaX1 = IntegerField('coordenada X')
    coordenadaY1 = IntegerField("coordenada Y")
    coordenadaX2 = IntegerField("coordenada X2")
    coordenadaY2 = IntegerField("coordenada Y2")