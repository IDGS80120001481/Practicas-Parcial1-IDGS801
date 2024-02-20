from wtforms import Form, StringField, RadioField
from wtforms.validators import DataRequired, Length, Email

class Traductor(Form):
    español = StringField("Palabra en español", validators=[
        DataRequired(message="No has escrito la palabra en español"),
        Length(min=3, max=50, message="Ingresa una palabra valida de entre 3 y 50 caracteres")
    ])
    ingles = StringField("Palabra en ingles", validators=[
        DataRequired(message="No has escrito la palabra en ingles"),
        Length(min=3, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
    buscar = StringField("Palabra a buscar", validators=[
        DataRequired(message="No has escrito la palabra a buscar"),
        Length(min=4, max=50, message="Ingresa una palabra valida de entre 4 y 50 caracteres")
    ])
    traductor = RadioField('Selecciona el lenguaje', choices=[('Español', 'Español'), ('Ingles', 'Ingles')])