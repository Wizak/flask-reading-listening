from app import db
from sqlalchemy.dialects.postgresql import UUID

import uuid

class Text(db.Model):
    __tablename__ = 'text'

    id_text = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Text, nullable=False)
    sound = db.relationship('Sound', backref='text', lazy=True)


class Sound(db.Model):
    __tablename__ = 'sound'

    id_sound = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)
    text_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('text.id_text'),
        default=uuid.uuid4)
