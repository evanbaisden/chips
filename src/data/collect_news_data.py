import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
project_root = os.getenv('PROJECT_ROOT')
raw_data_dir = os.path.join(project_root, 'data', 'raw')

def fetch_news(query, api_key):
    url = ('https://newsapi.org/v2/everything?'
           f'q={query}&'
           'sortBy=publishedAt&'
           'language=en&'
           'pageSize=100&'
           f'apiKey={api_key}')
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    df = pd.DataFrame(articles)
    return df

def main():
    api_key = os.getenv('NEWS_API_KEY')
    if not api_key:
        raise ValueError("NEWS_API_KEY not found in environment variables.")

    company_queries = ['NVIDIA', 'AMD', 'Intel', 'TSMC', 'ASML', 'Qualcomm', 'Micron Technology', 'Broadcom', 'Texas Instruments']
    all_news = pd.DataFrame()

    for query in company_queries:
        print(f"Fetching news for {query}...")
        df = fetch_news(query, api_key)
        df['company'] = query
        all_news = all_news.append(df, ignore_index=True)

    all_news.to_csv(os.path.join(raw_data_dir, 'news_data.csv'), index=False)
    print("News data saved successfully.")

if __name__ == "__main__":
    main()
