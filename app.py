from flask import Flask, render_template
from RecommendationEngine import recommend_courses_for_article, thn_articles, cybrary_courses

app = Flask(__name__)

# Generate recommendations using the RecommendationEngine.py script for all articles
recommendations_list = []

for article_index, (article_title, _) in enumerate(thn_articles):
    recommended_courses = recommend_courses_for_article(article_index)
    recommendations_list.append((article_title, recommended_courses))

@app.route('/')
def index():
    return render_template('index.html', recommendations=recommendations_list, cybrary_courses=cybrary_courses)

if __name__ == '__main__':
    app.run(debug=True)
