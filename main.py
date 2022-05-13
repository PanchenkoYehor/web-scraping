from bs4 import BeautifulSoup
import requests
from tqdm import trange
import numpy as np

'''
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    course_cards = soup.find_all('div', class_ = 'card')

    for course in course_cards:
        print(f"\ncourse = {course.h5.text}\n")
'''

headers = []

for page_num in trange(30):
    html_text = requests.get(f'https://tsn.ua/en?page={page_num}').text
    soup = BeautifulSoup(html_text, 'lxml')

    art = list(map(lambda x : x.find("a", {'class': 'c-card__link'}).text, soup.find_all('article')))
    headers = headers + art

print(np.array(headers))