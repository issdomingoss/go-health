from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.client_model import ClientModel
    from app.models.deficiency_model import DeficiencyModel
    from app.models.surgery_model import SurgeryModel
    from app.models.diseases_model import DiseaseModel
    from app.models.deficiency_client import deficiencyclientmodel
    from app.models.disease_client import diseaseclientmodel
    from app.models.surgery_client import surgeryclientmodel

    Migrate(app, app.db)
