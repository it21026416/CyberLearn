import sqlite3
import Scrap_THN_main

conn = sqlite3.connect('Course_Recommendation.db')

##To interact with the db using sql command
c = conn.cursor()

#table in our database 
# create columns and data types in them 
#c.execute('''CREATE TABLE THN(news_title TEXT, news_content TEXT, tablenumber INT)''')

#defines a function to insert scraped data into the database 
#def insert_data(news_title, news_content, tablenumber):
    #c.execute("INSERT INTO THN (News_title, News_content, tablenumber) VALUES (?, ?, ?)",
     #         (news_title, news_content, tablenumber))
    #conn.commit()



c.execute('''SELECT * FROM THN ''')
results = c.fetchall()
print(results)

