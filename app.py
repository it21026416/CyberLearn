from flask import Flask, render_template
from RecommendationEngine import recommend_courses_for_article, scrape_data

app = Flask(__name__)

# Get the data from the RecommendationEngine
thn_articles, cybrary_courses = scrape_data()

@app.route('/')
def index():
    recommendations_list = []
    for article_index, article in enumerate(thn_articles):
        if article_index == 7: break
        recommended_courses = recommend_courses_for_article(article, cybrary_courses, article_index)
        recommendations_list.append((article, recommended_courses))

    return render_template('index.html', recommendations=recommendations_list)

if __name__ == '__main__':
    app.run(debug=True)
