import requests
import time
import diskcache as dc
from datetime import datetime
from config import SALES_API_URL

cache = dc.Cache("cache_dir")

def fetch_recent_orders():
    """Fetch recent sales orders with per-day caching and auto-expiry."""
    today_key = datetime.now().strftime("%Y-%m-%d")
    cache_key = f"orders_{today_key}"

    # auto-clear entries older than 1 day
    for key in list(cache.iterkeys()):
        if key != cache_key:
            del cache[key]

    # use cache if available
    cached = cache.get(cache_key)
    if cached and time.time() - cached["timestamp"] < 86400:  # valid 24h
        print("🗂 Using cached data from today")
        return cached["data"]

    try:
        response = requests.get(SALES_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        cache.set(cache_key, {"data": data, "timestamp": time.time()})
        print("🌐 Fetched new data from API and cached it")
        return data
    except requests.exceptions.RequestException as e:
        print(f"⚠️ API Error: {e}")
        return []
