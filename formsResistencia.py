from wtforms import Form
from wtforms import SelectField, RadioField


class Resistencias(Form):
    banda1 = SelectField('Selecciona la banda 1', 
                         choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'),
                                  ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'),
                                  ('Azul', 'Azul'), ('Morado', 'Morado'), ('Gris', 'Gris'),
                                  ('Blanco', 'Blanco')])
    banda2 = SelectField('Selecciona la banda 2', 
                         choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'),
                                  ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'),
                                  ('Azul', 'Azul'), ('Morado', 'Morado'), ('Gris', 'Gris'),
                                  ('Blanco', 'Blanco')])
    banda3 = SelectField('Selecciona la banda 3', 
                         choices=[('Negro', 'Negro'), ('Cafe', 'Cafe'), ('Rojo', 'Rojo'),
                                  ('Naranja', 'Naranja'), ('Amarillo', 'Amarillo'), ('Verde', 'Verde'),
                                  ('Azul', 'Azul'), ('Morado', 'Morado'), ('Gris', 'Gris'),
                                  ('Blanco', 'Blanco')])
    tolerancia = RadioField('Selecciona la tolerancia', choices=[('Dorado', 'Dorado'), ('Plateado', 'Plateado')])
                            