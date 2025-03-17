from fastapi import FastAPI
from pydantic import BaseModel
import utils

app = FastAPI()

class CompanyRequest(BaseModel):
    company_name: str

@app.post("/analyze")
def analyze_news(request: CompanyRequest):
    articles = utils.scrape_news(request.company_name)
    for article in articles:
        article['sentiment'] = utils.analyze_sentiment(article['summary'])
    return {"articles": articles}