from flask import Blueprint, request, abort
from json import dumps

from app.models.base import db
from app.models.generic import Generic


generic = Blueprint('generic', __name__)


@generic.route('/generic/', methods=['GET'])
def get_all_generic():
    g = Generic.query.all()
    return dumps(Generic.serialize_list(g)) if g else {}, 200


@generic.route('/generic/<int:generic_id>', methods=['GET'])
def get_generic(generic_id):
    g = Generic.query.get(generic_id)
    return dumps(g.serialize()) if g else {}, 200


@generic.route('/generic/', methods=['POST'])
def create_generic():
    data = request.get_json()
    f1 = data['field1'] if 'field1' in data else None
    f2 = data['field2'] if 'field2' in data else None

    g = Generic(field1=f1, field2=f2)
    db.session.add(g)
    db.session.commit()
    return '', 201


@generic.route('/generic/<int:generic_id>', methods=['PUT'])
def edit_generic(generic_id):
    data = request.get_json()
    f1 = data['field1'] if 'field1' in data else None
    f2 = data['field2'] if 'field2' in data else None

    g = Generic.query.get(generic_id)
    if not g:
        return '', 404
    g.field1 = f1
    g.field2 = f2
    db.session.commit()
    return '', 204


@generic.route('/generic/<int:generic_id>', methods=['DELETE'])
def delete_generic(generic_id):
    g = Generic.query.get(generic_id)
    if not g:
        return '', 404
    db.session.delete(g)
    db.session.commit()
    return '', 204
