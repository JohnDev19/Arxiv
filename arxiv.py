# arxiv.py

import requests

def arxiv_search(search_query):
    try:
        api_url = f'http://export.arxiv.org/api/query?search_query={search_query}&max_results=5'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            return response.text
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

if __name__ == "__main__":
    print_welcome_ascii()
    
    search_query = input("Enter your search query: ")
    
    result = arxiv_search(search_query)
    
    print("\nArxiv API Result:")
    print(result)
