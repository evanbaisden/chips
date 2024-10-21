import os
from dotenv import load_dotenv

load_dotenv()  # Make sure this line is present

# For debugging purposes
print("FRED_API_KEY:", os.getenv('FRED_API_KEY'))
print("NEWS_API_KEY:", os.getenv('NEWS_API_KEY'))
print("MARKETSTACK_API_KEY:", os.getenv('MARKETSTACK_API_KEY'))
print("ALPHA_VANTAGE_API_KEY:", os.getenv('ALPHA_VANTAGE_API_KEY'))
print("TIINGO_API_KEY:", os.getenv('TIINGO_API_KEY'))
