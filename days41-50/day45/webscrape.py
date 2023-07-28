from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, features="lxml")

article_titles = []
article_links = []

article_spans = soup.select("span.titleline > a")
for article in article_spans:
    try:
        if article.parent.span.a.text  != 'ycombinator.com':
            article_link = article.get('href')
            article_title = article.text
            article_titles.append(article_title)
            article_links.append(article_link)
    except AttributeError: 
        article_link = article.get('href')
        article_title = article.text
        article_titles.append(article_title)
        article_links.append(article_link)
article_upvotes = [int(upvotes.text.split()[0]) for upvotes in soup.find_all("span", class_="score")]

# print(article_upvotes)
# print(article_links)
# print(article_titles)
max_upvoted_article_index = article_upvotes.index(max(article_upvotes))
max_upvoted_article_title = article_titles[max_upvoted_article_index]
max_upvoted_article_link = article_links[max_upvoted_article_index]

print(max_upvoted_article_title,"\n", max_upvoted_article_link)
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'lxml')
# # print(soup.title.string)
# # print(soup.prettify())
# a_anchor_tags = soup.find_all('a')
# # print(a_anchor_tags)
# for tag in a_anchor_tags:
#     print(tag.get("href"))

# heading = soup.find(name="h1")
# print(heading)

# specific_a = soup.select_one("p a")
# print(specific_a)