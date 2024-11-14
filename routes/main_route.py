from flask import Blueprint, jsonify,request
from kf.producer import send_message

Email = Blueprint('Email', __name__)

@Email.route('/api/email', methods=['POST'])
def insert_new_email():
    new_email = request.json
    send_message(new_email)
    return jsonify("is send to sended"),200


