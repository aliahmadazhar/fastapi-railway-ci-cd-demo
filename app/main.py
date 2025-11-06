from fastapi import FastAPI, HTTPException, Query
import requests

app = FastAPI(title="Reddit Info API")

REDDIT_BASE = "https://www.reddit.com"

@app.get("/")
def home():
    return {"message": "Welcome to the Reddit Info API!"}

@app.get("/reddit")
def reddit_info(subreddit: str = Query(..., description="Subreddit name (without r/)")):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; DemoApp/1.0)"}

    # Get subreddit info
    about_url = f"{REDDIT_BASE}/r/{subreddit}/about.json"
    response = requests.get(about_url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Subreddit not found")

    data = response.json()["data"]

    # Get top post
    top_url = f"{REDDIT_BASE}/r/{subreddit}/top.json?limit=1&t=day"
    top_resp = requests.get(top_url, headers=headers)
    top_post_data = None
    if top_resp.status_code == 200 and len(top_resp.json().get("data", {}).get("children", [])) > 0:
        post = top_resp.json()["data"]["children"][0]["data"]
        top_post_data = {
            "title": post["title"],
            "upvotes": post["ups"],
            "url": f"{REDDIT_BASE}{post['permalink']}"
        }

    return {
        "subreddit": data["display_name"],
        "title": data["title"],
        "subscribers": data["subscribers"],
        "active_users": data.get("active_user_count"),
        "description": data["public_description"],
        "top_post": top_post_data
    }
