from flask import session, jsonify
from ..Backend import delete_json_files, delete_log_files
from ..Backend.Compressing_Handler import delete_zip_files
from . import session_bp
@session_bp.route('/set_session', methods=['GET'])
def set_session():
    session['user'] = 'test_user'
    return jsonify({'message': 'Session variable set!'})

@session_bp.route('/get_session', methods=['GET'])
def get_session():
    user = session.get('user', 'Not Set')
    return jsonify({'user': user})
@session_bp.route('/clear_session', methods=['POST'])
def clear_session():
    delete_log_files()
    delete_json_files()
    session.clear()
    delete_zip_files()
    return jsonify({'message': 'Session cleared'}), 200