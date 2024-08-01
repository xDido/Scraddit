import os
from . import delete_bp
from flask import request, jsonify, flash, redirect, url_for
@delete_bp.route('/delete-logs', methods=['POST'])
def delete_log_files():
    try:
        delete_log_files()  # Clean up log files
        return jsonify({'message': 'Log files cleaned up successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to clean up log files'}), 500

@delete_bp.route('/delete-json', methods=['POST'])
def delete_json_files():
    try:
        delete_json_files()  # Clean up JSON files
        return jsonify({'message': 'JSON files cleaned up successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to clean up JSON files'}), 500
@delete_bp.route('/delete-zip', methods=['POST'])
def delete_zip_files():
    try:
        delete_zip_files()  # Clean up ZIP files
        return jsonify({'message': 'ZIP files cleaned up successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to clean up ZIP files'}), 500
