import facebook
import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")  

def scrape_facebook(url, access_token):
    graph = facebook.GraphAPI(access_token)
    posts = graph.get_connections(url, "posts")

    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = db.cursor()

    for post in posts["data"]:
        post_id = post.get("id")
        message = post.get("message", "")
        created_time = post.get("created_time")

        created_time = datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S%z")

        query = "INSERT IGNORE INTO posts (post_id, message, created_time) SELECT %s, %s, %s FROM DUAL WHERE NOT EXISTS (SELECT * FROM posts WHERE post_id = %s)"
        values = (post_id, message, created_time, post_id)

        cursor.execute(query, values)

    db.commit()

    return {"message": "Scraping successful!"}
