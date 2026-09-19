import feedparser
import os

feeds = {
    "WORLD": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "TECHNOLOGY": "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "SCIENCE": "https://www.sciencedaily.com/rss/top/science.xml"
}

os.makedirs("drafts", exist_ok=True)

print("\n🌍 GLOBAL INFO NEWS COLLECTOR\n")

for category, url in feeds.items():

    feed = feedparser.parse(url)

    filename = f"drafts/{category.lower()}.txt"

    with open(filename, "w", encoding="utf-8") as file:

        file.write(f"{category} NEWS\n")
        file.write("=" * 50 + "\n\n")

        for article in feed.entries[:10]:

            file.write(f"Title: {article.title}\n")

            if hasattr(article, "link"):
                file.write(f"Link: {article.link}\n")

            file.write("\n" + "-" * 50 + "\n\n")

    print(f"Saved: {filename}")

print("\nDone!")