from .JSON_Handler import export_to_json
import datetime
import logging
import praw
from .Compressing_Handler import compress_files
from .Path_Finder import get_path
log_directory = get_path('Logs')
def create_reddit_object():

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


def collect_subreddit_data(subreddit: praw.models.Subreddit, logger: logging.Logger, filter_type: str):
    """
    Collect text-only data (posts and comments) from a specified subreddit,
    using the user-specified filter type.

    :param subreddit: A praw.models.Subreddit object
    :param logger: Logger object for logging messages
    :param filter_type: String specifying the filter type ('new', 'hot', 'top', 'rising', 'controversial', 'gilded')
    """
    data = []
    post_count = 0
    collected_post_ids = set()  # Set to store collected post IDs

    logger.info(f"Starting data collection from 'r/{subreddit.display_name}' using '{filter_type}' filter")

    # Select the appropriate generator based on the filter_type
    filter_types = {
        'new': subreddit.new,
        'hot': subreddit.hot,
        'gilded': subreddit.gilded,
        'top': subreddit.top,
        'rising': subreddit.rising,
        'controversial': subreddit.controversial
    }

    if filter_type not in filter_types:
        logger.error(f"Invalid filter_type: {filter_type}")
        raise ValueError(f"Invalid filter_type: {filter_type}")

    post_generator = filter_types[filter_type](limit=None)

    try:
        for submission in post_generator:
            if not submission.is_self:  # Skip non-text posts
                continue

            if submission.id in collected_post_ids:  # Skip if we've already collected this post
                continue

            post = {
                'CreatedAt': submission.created_utc,
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
                logger.error(f"Error processing comments for post {submission.id}: {str(e)} comment might be deleted")

            data.append(post)
            collected_post_ids.add(submission.id)  # Add the post ID to our set
            post_count += 1

            logger.debug(f"Collected post {post_count}: {submission.selftext[:50]}")  # Use debug for detailed logging
            print(f"Collected post {post_count}: {submission.title}")  # Print the current post count and title

            if post_count == 1000:
                export_to_json(data, f"{subreddit.display_name}_{filter_type}")
                logger.info(f"Exported batch of 1000 posts for {subreddit.display_name}_{filter_type}")
                print(f"Exported batch of 1000 posts for {subreddit.display_name}_{filter_type}")  # Print export status
                data = []  # Clear data after exporting
                post_count = 0

        if data:  # Export any remaining data
            export_to_json(data, f"{subreddit.display_name}_{filter_type}")
            logger.info(f"Exported final batch of {len(data)} posts for {subreddit.display_name}_{filter_type}")
            print(f"Exported final batch of {len(data)} posts for {subreddit.display_name}_{filter_type}")  # Print final export status

    except KeyboardInterrupt:
        logger.info("Data collection interrupted by user.")
        print("Data collection interrupted by user.")
    finally:
        compress_files(log_directory, subreddit.display_name)
        logger.info(f"Data collection complete. Total posts collected: {len(collected_post_ids)}")
        print(f"Data collection complete. Total posts collected: {len(collected_post_ids)}")

