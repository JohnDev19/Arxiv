import urllib.request
import feedparser

def arxiv_search(search_query):
    try:
        api_url = f'http://export.arxiv.org/api/query?search_query={search_query}&max_results=5'
        response = urllib.request.urlopen(api_url)
        content = response.read()

        feed = feedparser.parse(content)
        entries = feed.entries
        return entries

    except Exception as e:
        return f"Error: {e}"

def print_welcome_ascii():
    welcome_ascii = """
      _____           _     _____ _____ _____ 
     |   __|_____ ___|_|___|  |  |     |  _  |
     |__   |  _  |  _| | -_|  |  | | | |   __|
     |_____|_|   |_| |_|___|_____|_|_|_|__|
                    WELCOME TO ARXIV
    """
    print(welcome_ascii)

def format_results(entries):
    for entry in entries:
        title = entry.title
        summary = entry.summary
        link = entry.link

        print(f"\nTitle: {title}\nDescription: {summary}\nURL: {link}\n")

if __name__ == "__main__":
    print_welcome_ascii()

    search_query = input("Enter your search query: ")

    result_entries = arxiv_search(search_query)

    print("\nArxiv API Results:")
    format_results(result_entries)
