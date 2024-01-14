import requests
import feedparser

def arxiv_search(search_query):
    try:
        api_url = f'http://export.arxiv.org/api/query?search_query={search_query}&max_results=5'
        response = requests.get(api_url)

        if response.status_code == 200:
            feed = feedparser.parse(response.text)
            entries = feed.entries
            return entries
        else:
            return f"Error: {response.status_code} - {response.text}"

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
