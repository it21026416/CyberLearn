import requests
import nltk
import schedule
import time
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import urllib.parse

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# URLs
thn_url = "https://thehackernews.com/search/label/Cyber%20Attack"
cybrary_url = "https://www.cybrary.it/catalog"

def tokenize_and_filter(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    return " ".join(filtered_tokens)

def scrape_data():
    # Scrape and process articles from The Hacker News
    thn_articles = []
    response = requests.get(thn_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("div", class_="clear home-right")
        for article in articles:
            headline = article.find("h2", class_="home-title").text.strip()
            content = article.find("div", class_="home-desc").text.strip()
            processed_content = tokenize_and_filter(content)
            thn_articles.append((headline, processed_content))
    else:
        print(f"Error {response.status_code}: Failed to retrieve THN articles")

    # Scrape and process Cybrary course descriptions
    cybrary_courses = []
    response = requests.get(cybrary_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        courses = soup.find_all("div", class_="card-component_list is-3 w-dyn-items")
        for course in courses:
            course_title = course.find("h3", class_="heading-style-h5").text.strip()
            content = course.find("div", class_="text-size-small w-richtext").text.strip()
            relative_url = course.find("a", class_="card-component_link-wrapper w-inline-block")["href"]
            absolute_url = urllib.parse.urljoin(cybrary_url, relative_url)
            processed_content = tokenize_and_filter(content)
            cybrary_courses.append((course_title, processed_content, absolute_url))
    else:
        print(f"Error {response.status_code}: Failed to retrieve Cybrary courses")

    return thn_articles, cybrary_courses

def recommend_courses_for_article(thn_articles, cybrary_courses, article_index):
    all_text_data = [article[1] for article in thn_articles] + [course[1] for course in cybrary_courses]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_text_data)
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    similarity_scores = list(enumerate(cosine_similarities[article_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_similar_indices = [i for i, _ in similarity_scores if i >= len(thn_articles)]
    return [(cybrary_courses[i - len(thn_articles)][0], cybrary_courses[i - len(thn_articles)][2]) for i in top_similar_indices]

def run_recommendation_engine():
    thn_articles, cybrary_courses = scrape_data()
    for article_index, (article_title, _) in enumerate(thn_articles):
        recommended_courses = recommend_courses_for_article(thn_articles, cybrary_courses, article_index)
        print(f"Cyber Attack News: {article_title}")
        if recommended_courses:
            print("Recommended Courses:")
            for course_title, absolute_url in recommended_courses:
                print(f"{course_title}: {absolute_url}")
        else:
            print("No recommended courses found.")
        print()

# Schedule the task
schedule.every().hour.do(run_recommendation_engine)

if __name__ == "__main__":
    # Run once at the start
    run_recommendation_engine()

    # Then keep running based on the schedule
    while True:
        schedule.run_pending()
        time.sleep(1)
