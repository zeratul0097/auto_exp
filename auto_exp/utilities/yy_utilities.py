import re


def get_last_chapter(text):
    return re.split('[.\\-]', text)[-2]


def get_book_name_from_url(url):
    return [x for x in url.split('/') if x][1]
