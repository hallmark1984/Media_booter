import requests
import feedparser
from datetime import datetime, timezone, timedelta
from time import mktime

class RedditProvider:
    def fetch(self, category, lookback_mins):
        url = f"https://www.reddit.com/r/{category}/new.json"
        headers = {"User-Agent": "MediaBooter/1.0"}
        try:
            r = requests.get(url, headers=headers, timeout=10)
            posts = r.json().get('data', {}).get('children', [])
        except: return []

        cutoff = datetime.now(timezone.utc) - timedelta(minutes=lookback_mins)
        results = []
        for p in [post['data'] for post in posts]:
            dt = datetime.fromtimestamp(p['created_utc'], tz=timezone.utc)
            if dt < cutoff: continue
            results.append({
                'source': 'reddit', 'category': category, 'external_id': p['id'],
                'title': p['title'], 'url': f"https://reddit.com{p['permalink']}",
                'author': p['author'], 'created_at_external': dt,
                'raw_data': {'ups': p.get('ups'), 'comments': p.get('num_comments')}
            })
        return results

class BBCProvider:
    def fetch(self, category, lookback_mins):
        url = f"https://feeds.bbci.co.uk/news/{category}/rss.xml"
        feed = feedparser.parse(url)
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=lookback_mins)
        results = []
        for entry in feed.entries:
            try:
                dt = datetime.fromtimestamp(mktime(entry.published_parsed), tz=timezone.utc)
                if dt < cutoff: continue
                results.append({
                    'source': 'bbc', 'category': category, 'external_id': entry.id,
                    'title': entry.title, 'url': entry.link, 'author': 'BBC News',
                    'created_at_external': dt, 'raw_data': {'summary': entry.summary}
                })
            except: continue
        return results

PROVIDERS = {'reddit': RedditProvider(), 'bbc': BBCProvider()}
