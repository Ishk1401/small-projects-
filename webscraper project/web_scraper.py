import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

# Fetch HTML
url = 'https://www.bbc.com/news'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
html = response.text

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')
headlines = soup.find_all(['h1', 'h2', 'h3'])

# Extract titles
titles = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

# Save to headlines.txt
with open('headlines.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        f.write(f"{title}\n")

# Sentiment analysis (optional)
with open('sentiment_report.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        polarity = TextBlob(title).sentiment.polarity
        f.write(f"{title} | Sentiment: {polarity:.2f}\n")