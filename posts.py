import mysql.connector
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")  

def get_posts_from_database():
    db = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM posts ORDER BY created_time DESC"
    cursor.execute(query)

    posts = []
    for id, post_id, message, created_time in cursor:
        posts.append({"id": post_id, "message": message, "created_time": created_time})

    db.close()

    return posts
