import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download the resources
nltk.download('punkt')
nltk.download('stopwords')

# Import the tokenize_text function from the web scraper
from NLP_Tokenization import tokenize_text

# URL to scrape
url = "https://www.cybrary.it/catalog"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the course cards
    course_cards = soup.find_all("div", class_="card-component_list is-3 w-dyn-items")

    # Iterate through each course card and print its title, content, and URL
    for course_card in course_cards:
        # Extract the title
        title = course_card.find("h3", class_="heading-style-h5").text.strip()
        
        # Extract the content
        content = course_card.find("div", class_="text-size-small w-richtext").text.strip()
        
        # Extract the course URL
        course_url = course_card.find("a", class_="card-component_link-wrapper w-inline-block")["href"]
        
        # Tokenize the content
        tokens = tokenize_text(content)

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]

        # Print the course title, content, and URL
        print(f"Title: {title}")
        print(f"Content: {filtered_tokens}")
        print(f"URL: {course_url}")
        print("-" * 50)  # Print a line of dashes for separation
else:
    print("Failed to retrieve the page")
