from flask_sqlalchemy import SQLAlchemy
import enum
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema

db = SQLAlchemy()

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albumes = db.relationship('Album', secondary='album_cancion', back_populates='canciones')

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    anio = db.Column(db.String(128))
    descripcion = db.Column(db.String(128))
    medio = db.Column(db.Enum(Medio))
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    canciones = db.relationship('Cancion', secondary='album_cancion', back_populates='albumes')
    __table_args__ = (db.UniqueConstraint('usuario_id', 'titulo', name='titu_unico_album'),)

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.anio, self.descripcion, self.medio)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    contrasenia = db.Column(db.String(128))
    albumes = db.relationship('Album', cascade="all, delete, delete-orphan")

    def __repr__(self):
        return "{}-{}".format(self.nombre, self.contrasenia)

albumes_canciones = db.Table('album_cancion',  \
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True)
)

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        if isinstance(value, list):
            return [{'llave': item.name, 'valor': item.value} for item in value]
        return {'llave': value.name, 'valor': value.value}

class AlbumSchema(SQLAlchemySchema):
    medio = EnumADiccionario(attribute=('medio',))
    class Meta:
        model = Album
        include_relationships = True
        load_instance = True

    class CancionesSchema(SQLAlchemySchema):
        def _serialize(self, value, attr, obj, **kwargs):
            if value is None:
                return None
           
