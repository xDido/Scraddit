from Functions import create_reddit_object, choose_subreddit, collect_subreddit_data
import datetime
def main():
    # Create a Reddit object
    reddit = create_reddit_object()

    # Specify the subreddit name
    subreddit_name = "PersonalFinanceEgypt"

    # Choose the subreddit
    subreddit = choose_subreddit(reddit, subreddit_name)

    print(f"Starting continuous data collection from r/{subreddit_name}")
    print("The script will run until you stop it manually.")
    print("Press Ctrl+C to stop the script at any time.")

    try:
        # Start continuous data collection
        collect_subreddit_data(subreddit)
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    finally:
        print("Data collection process ended.")

if __name__ == "__main__":
    main()