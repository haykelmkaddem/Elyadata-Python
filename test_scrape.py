import os
from scraper import scrape_facebook
from posts import get_posts_from_database
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")
access_token = os.getenv("ACCESS_TOKEN")

def test_scrape_facebook():
    result = scrape_facebook(url, access_token)

    # Assert that the result is a dictionary
    assert isinstance(result, dict)

    # Assert that the result contains a "message" key with value "Scraping successful!"
    assert "message" in result
    assert result["message"] == "Scraping successful!"

def test_get_posts_from_database():
    # Call the get_posts_from_database function
    posts = get_posts_from_database()

    # Assert that the result is a list
    assert isinstance(posts, list)

    # Assert that each item in the list is a dictionary with the expected keys
    for post in posts:
        assert isinstance(post, dict)
        assert "id" in post
        assert "message" in post
        assert "created_time" in post

def test_get_posts_from_database_sorted():
    # Call the get_posts_from_database function to get a list of posts from the database
    posts_list = get_posts_from_database()

    # Sort the posts by their created_time in descending order to get a sorted_posts_list
    sorted_posts_list = sorted(posts_list, key=lambda post: post["created_time"], reverse=True)

    # Check if the original posts_list is equal to the sorted_posts_list
    assert posts_list == sorted_posts_list


def test_database_contains_posts():
    # Call the scrape_facebook function to scrape Facebook for posts and insert them into the database
    scrape_facebook(url, access_token)

    # Call the get_posts_from_database function to get a list of posts from the database
    posts_list = get_posts_from_database()

    # Check if the length of the posts_list is greater than zero
    assert len(posts_list) > 0

