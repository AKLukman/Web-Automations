"""
Why You Need Fast API to Use Your Automation Script With
- Web Application
- Mobile Application
- IOT Devices
- Or With Desktop Application
- Or Any Other B2B or B2C System

Advantages of Fast API:
- FastAPI is easy Python web framework for building APIs.
- It supports async/await for high performance.
- Uses Pydantic for automatic data validation.
- Generates Swagger docs automatically.
- Great for REST APIs, microservices, and ML model serving.
- Great for Serving Automation Features as API

What We Cover Here:
- Minimum Basic of Fast API for Your Automation Features Purpose
- More You Want to Learn A Master on Fast API course is coming ahead

Start With Fast API
- pip install fastapi uvicorn
- uvicorn main:app --reload
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/youtube-scraping")
def youtube_scraping():

    # Automation/Scrapping Logic Code Base Input

    # Automation/Scrapping Output Return
    return {"message":"Hello Fast API"}
