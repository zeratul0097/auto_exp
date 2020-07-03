# -*- coding: utf-8 -*-
from os import getenv
from scrapy import Request, Spider
from scrapy.http.response import Response
from scrapy.loader import ItemLoader
from dotenv import load_dotenv

from auto_exp.items import BookInfo
from auto_exp.constants.common_constants import LAST_CHAPTER, SHORT_NAME, CHAPTER_INDEX
from auto_exp.constants.yy_constants import *
from auto_exp.utilities.yy_utilities import get_book_name_from_url


load_dotenv(dotenv_path='.env')
COOKIE = getenv('COOKIE')


class YYSpider(Spider):
    name = 'yy'

    custom_settings = {
        'LOG_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'accept': '*/*',
            'cookie': COOKIE,
            'upgrade-insecure-requests': 1,
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        }
    }

    def start_requests(self):
        # Crawl all books in main page
        yield Request(
            url=MAIN_PAGE,
            callback=self.parse_main_page
        )
        # Crawl all top-book time
        for year in range(2018, 2021):
            for month in range(1, 13):
                for page in range(1, 41):
                    yield Request(
                        url=TOP_BOOK_TIME_URL.format(year, month, page),
                        callback=self.parse_top_books
                    )

    def parse_top_books(self, response):
        url_lists = response.xpath(TOP_BOOK_URLS)
        for url in url_lists:
            short_name = [x for x in url.get().split('/') if x][-1]
            yield Request(
                url=BASE_URL.format(short_name),
                callback=self.parse_book_info,
                cb_kwargs=dict(short_name=short_name)
            )

    def parse_main_page(self, response: Response):
        book_urls = response.xpath(BOOK_URL)
        genre_urls = response.xpath(GENRE_URL)
        for url in book_urls:
            short_name = get_book_name_from_url(url.get())
            yield Request(
                url=BASE_URL.format(short_name),
                callback=self.parse_book_info,
                cb_kwargs=dict(short_name=short_name)
            )
        genre_urls = [x.get() for x in genre_urls]
        genres = list(set([x.replace('/', '') for x in genre_urls]))
        for k in range(len(genres)):
            yield Request(
                url=response.urljoin(genre_urls[k]),
                callback=self.parse_books_in_page
            )
            for i in range(1, 250):
                yield Request(
                    url=GENRE_PAGE_URL.format(genres[k], i),
                    callback=self.parse_top_books
                )

    def parse_books_in_page(self, response):
        book_urls = response.xpath(BOOK_URL)
        for url in book_urls:
            short_name = get_book_name_from_url(url)
            yield Request(
                url=BASE_URL.format(short_name),
                callback=self.parse_book_info,
                cb_kwargs=dict(short_name=short_name)
            )

    def parse_book_info(self, response, short_name):
        # Get book's full name and author
        loader = ItemLoader(item=BookInfo(), response=response)
        # Find elements
        loader.add_xpath(LAST_CHAPTER, BOOK_LAST_CHAPTER_PATH)

        # Extracting data
        page = loader.load_item()
        last_chapter = int(page.get(LAST_CHAPTER))
        for i in range(1, last_chapter + 1):
            yield Request(
                url=CHAPTER_URL.format(short_name, i),
                callback=self.parse_chapter,
                cb_kwargs=dict(short_name=short_name, chapter_index=i),
                dont_filter=True
            )

    def parse_chapter(self, response, short_name, chapter_index):
        yield {
            SHORT_NAME: short_name,
            CHAPTER_INDEX: chapter_index
        }
