from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import inspect
import datetime


db = SQLAlchemy()


class Serializer(object):
    def __format(self, obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        return obj

    def serialize(self):
        return {m: self.__format(getattr(self, m)) for m in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
