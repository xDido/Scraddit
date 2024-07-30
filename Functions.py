import datetime
import json
import logging
import os
import time

import praw
from dotenv import load_dotenv


def create_reddit_object():
    load_dotenv()  # Load environment variables from .env file

    reddit = praw.Reddit(
        client_id="nYw8u5M8iSndcbHofKBItw",
        client_secret="hdATxiS5ma7W42VbcJFH74Lv0eDEig",
        user_agent="True",
        username="UNIMET_52",
        password="Gucmetscrappe@2002"
    )

    return reddit


def choose_subreddit(reddit: praw.Reddit, sub_name: str):
    if not isinstance(sub_name, str):
        raise ValueError("sub_name must be a string")

    subreddit = reddit.subreddit(sub_name)
    return subreddit


def collect_subreddit_data(subreddit: praw.reddit.Subreddit):
    """
    Continuously collect text-only data (posts and comments) from a specified subreddit,
    using PRAW's stream_generator to efficiently fetch new posts.

    :param subreddit: A praw.models.Subreddit object
    """
    data = []
    post_count = 0
    collected_post_ids = set()  # Set to store collected post IDs
    last_post_id = None  # Variable to store the last collected post ID

    logging.basicConfig(filename='reddit_scraper.log', level=logging.INFO)

    print(f"Starting continuous data collection from r/{subreddit.display_name}")
    print("Press Ctrl+C to stop the script")
    try:
        for submission in subreddit.top(limit=None):
            if not submission.is_self:  # Skip non-text posts
                continue

            if submission.id in collected_post_ids:  # Skip if we've already collected this post
                print(f"Skipping duplicate post: {submission.id}")
                continue

            post = {
                'post_id': submission.id,
                'title': submission.title,
                'post_content': submission.selftext,
                'post_score': submission.score,
                'post_time': datetime.datetime.fromtimestamp(submission.created_utc).isoformat(),
                'comments': []
            }

            try:
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    comment_details = {
                        'comment_content': comment.body,
                        'comment_score': comment.score,
                        'comment_time': datetime.datetime.fromtimestamp(comment.created_utc).isoformat()
                    }
                    post['comments'].append(comment_details)
            except Exception as e:
                logging.error(f"Error processing comments for post {submission.id}: {str(e)}")

            data.append(post)
            collected_post_ids.add(submission.id)  # Add the post ID to our set
            last_post_id = submission.id  # Update the last post ID
            post_count += 1

            print(f"Collected post {post_count}: {submission.title[:50]}...")
            logging.info(f"Collected post {post_count}: {submission.id}")

            if post_count == 1000:
                export_to_json(data, subreddit.display_name)
                data = []  # Clear data after exporting
                post_count = 0  # Reset post count
        export_to_json(data, subreddit.display_name)

    except KeyboardInterrupt:
        print("\nScript stopped by user. Exporting final data...")
        if data:
            export_to_json(data, subreddit.display_name)
        print(f"Last collected post ID: {last_post_id}")
        print("Data collection complete.")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred. Check the log file for details. Retrying in 65 seconds...")
        print(f"Last collected post ID: {last_post_id}")
        time.sleep(65)  # Wait for 65 seconds before retrying



def export_to_json(data, subreddit_name):
    """
    Export collected Reddit data to a JSON file.
    :param data: List of dictionaries containing post and comment data
    :param subreddit_name: Name of the subreddit (used for filename)
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"r_{subreddit_name}_{timestamp}.json"

    file_path = os.path.join(os.getcwd(), filename)

    with open(file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=2)

    print(f"Data exported to {file_path}")
