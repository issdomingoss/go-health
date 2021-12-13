from flask import jsonify, request, current_app
from app.models.professional_model import ProfessionalModel


def create():
    data = request.get_json()

    session = current_app.db.session

    # convert password in password_hash
    password_to_hash = data.pop("password")
    professional = ProfessionalModel(**data)
    professional.password = password_to_hash

    session.add(professional)
    session.commit()

    return jsonify(professional), 200


def get_all():

    professional_list = ProfessionalModel.query.all()

    return jsonify(professional_list), 200


def get_by_id(id):
    professional = ProfessionalModel.query.filter_by(id=id).first()
    return jsonify(professional.serialize()), 200
