from GoogleNews import GoogleNews
import csv
import pandas as pd
import pymysql
import datetime
import Database
from dotenv import load_dotenv
import os

load_dotenv()
host = os.environ.get('host')
user = os.environ.get('user')
password = os.environ.get('password')
db = os.environ.get('db')
googlenews = GoogleNews()
db_name = 'GoogleNews'
db_table = 'GoogleNews'
conn = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=db,)
# googlenews = GoogleNews(lang='en')


def news_scraper(Keyword):
    # googlenews.get_news(Keyword)
    # print(googlenews.results())
    googlenews.search(Keyword)
    # print(googlenews.results())
    googlenews.get_page(2)
    # googlenews.results()
    news_texts = googlenews.get_texts()
    news_links = googlenews.results()
    # for news in news_texts:
    #     print(news)
    #     print('\n')
    # print(News_texts)
    # print(news_links)
    return news_links


if __name__ == '__main__':
    news_final_list = []
    Search = 'covid-19'
    news_list = news_scraper(Search)
    print('news texts:')
    for txt in news_list:
        print(txt)
    csv_columns = pd.DataFrame(news_list, columns=['title', 'desc', 'date', 'curr_time', 'link', 'img', 'media', 'site'])
    csv_columns.to_csv('news.csv'.format(Search), sep=',', index=False)
    # test()
    # database_conn()
    for i in range(0, len(news_list)):
        news_tup = ()
        # print(type(news_tup))
        temp_list = list(news_tup)
        # print(i)
        title = news_list[i]['title']

        temp_list.append(title)
        media = str(news_list[i]['media'])
        temp_list.append(media)
        published_date = news_list[i]['date']
        temp_list.append(published_date)
        # print(published_date)
        description = news_list[i]['desc']
        temp_list.append(description)
        link = news_list[i]['link']
        temp_list.append(link)
        img = news_list[i]['img']
        temp_list.append(img)
        created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(created_at)
        temp_list.append(created_at)
        news_tup = tuple(temp_list)
        news_final_list.append(news_tup)
        print(news_tup)
    print(news_final_list)
    # print(mews_set)
    query = f'INSERT INTO {db_table} (title, media, published_date, description, link, img, created_at) values (%s,%s,%s,%s,%s,%s,%s)'
    print(query)

    with conn.cursor() as cursor:
        cursor.executemany(query=query, args=news_final_list)
        conn.commit()
    print('Session Saved')
    print(cursor.rowcount)
    print(cursor)
    googlenews.clear()


