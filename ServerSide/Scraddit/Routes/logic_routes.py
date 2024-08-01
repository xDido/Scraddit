from flask import request, jsonify,session
from . import logic_bp
from ..Backend.Praw_Handler import create_reddit_object, choose_subreddit, collect_subreddit_data
from ..Backend.JSON_Handler import export_to_json
from ..Backend.Logging_Handler import setup_logging

SESSION_STORAGE = {}


# Route for collecting subreddit data
@logic_bp.route('/setup-reddit', methods=['POST'])
def setup_reddit():
    if not 'user' in session:
        return jsonify({
            'message': 'User session unavailable',
        }), 404
    data = request.json
    sub_name = data.get('sub_name')

    if not sub_name:
        return jsonify({'error': 'sub_name is required'}), 400

    try:
        reddit = create_reddit_object()  # Create Reddit object
        subreddit = choose_subreddit(reddit, sub_name)  # Choose subreddit

        # Store necessary details
        SESSION_STORAGE['subreddit_name'] = sub_name
        SESSION_STORAGE['reddit'] = reddit  # Store Reddit object
        SESSION_STORAGE['subreddit'] = subreddit  # Store subreddit object
        return jsonify({'message': f'Subreddit {sub_name} selected', 'subreddit': sub_name, 'session_user': session.get('user')}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'Failed to setup Reddit object or choose subreddit'}), 500


@logic_bp.route('/collect-data', methods=['POST'])
def collect_data():
    filter_type = request.json.get('filter_type', 'new')
    sub_name = SESSION_STORAGE.get('subreddit_name')
    if not sub_name:
        return jsonify({'error': 'No subreddit selected. Please set up Reddit first.'}), 400
    try:
        logger = setup_logging()  # Set up logging
        subreddit = SESSION_STORAGE.get('subreddit')
        collect_subreddit_data(subreddit, logger, filter_type)  # Collect data
        return jsonify(
            {'message': f'Data collection completed for subreddit {sub_name} with filter {filter_type}'}), 200
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to collect data'}), 500


@logic_bp.route('/export-data', methods=['POST'])
def export_data():
    filter_type = request.json.get('filter_type', 'new')

    sub_name = SESSION_STORAGE.get('subreddit')
    if not sub_name:
        return jsonify({'error': 'No subreddit selected. Please set up Reddit first.'}), 400
    try:
        export_to_json(sub_name, filter_type)  # Export to JSON
        return jsonify({'message': f'Data exported to JSON for subreddit {sub_name} with filter {filter_type}'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to export data'}), 500
