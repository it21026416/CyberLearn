import requests
from bs4 import BeautifulSoup
import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# IT21026416
# Download the resources
nltk.download('punkt')
nltk.download('stopwords')
 
# Import the tokenize_text function from the web scraper
from NLP_Tokenization import tokenize_text

# URL to scrape
url = "https://thehackernews.com/search/label/Cyber%20Attack"


# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the article headlines and content
    articles = soup.find_all("div", class_="clear home-right")


    # Iterate through each article and print its headline and content
    for article in articles:
        headline = article.find("h2", class_="home-title").text.strip()
        content = article.find("div", class_="home-desc").text.strip()

        print(headline)
        print("-" * 50)  # Print a line of dashes for separation

        # Tokenize the content
        tokens = tokenize_text(content)
        
        #REMOVE THE STOP WORDS
        stop_words=set(stopwords.words('english'))
        filtered_tokens=[token for token in tokens if token not in stop_words]


        # Split the content into lines and print each line aligned with the headline
    ##    content_lines = content.split('\n')
    ##    for line in content_lines:
    ##        print(f"{line.strip():<60}")

        print(filtered_tokens)
        print("\n")  # Add an empty line between articles

else:
    print("Failed to retrieve the page")