from app.models.base import db, Serializer


class Generic(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String(100), nullable=False)
    field2 = db.Column(db.String(100))
    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
