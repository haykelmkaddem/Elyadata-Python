from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from scraper import scrape_facebook
from posts import get_posts_from_database
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

templates = Jinja2Templates(directory="templates")

url = os.getenv("URL")
access_token = os.getenv("ACCESS_TOKEN")

@app.get("/scrape")
async def scrape(request: Request):
    result = scrape_facebook(url, access_token)
    db_posts = get_posts_from_database()
    posts_list = db_posts
    return templates.TemplateResponse("posts.html", {"request": request, "posts": posts_list})
