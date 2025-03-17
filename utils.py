import requests
from bs4 import BeautifulSoup
import pandas as pd
from gtts import gTTS
import os
from transformers import pipeline

import requests

def scrape_news(company_name):
    """
    Fetch news articles related to the given company name using NewsAPI.
    """
    newsapi_key = os.getenv("NEWSAPI_KEY") 
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={newsapi_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        articles = []
        for item in data.get("articles", [])[:10]:  
            title = item.get("title", "")
            summary = item.get("description", "")
            link = item.get("url", "")
            articles.append({
                "title": title,
                "summary": summary,
                "link": link
            })

        return articles

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []


def analyze_sentiment(text):
    """
    Perform sentiment analysis on the given text.
    Returns 'positive', 'negative', or 'neutral'.
    """
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return result['label']




def text_to_speech(text, language='hi'):
    """
    Convert text to speech in Hindi and save as an audio file.
    """
    tts = gTTS(text=text, lang=language)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file