from flask import Blueprint
from app.controllers.client_controllers import create, get_by_id, get_all,update,delete
from flask_jwt_extended import jwt_required

bp_clients = Blueprint('bp_clients', __name__, url_prefix='/clients')


bp_clients.post('')(create)
bp_clients.get("")(get_all)
bp_clients.patch('/<int:id>')(jwt_required()(update))
bp_clients.delete('/<int:id>')(jwt_required()(delete))
bp_clients.get('/<int:id>')(jwt_required()(get_by_id))
