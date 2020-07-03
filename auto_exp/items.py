# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader.processors import Join, MapCompose
from auto_exp.utilities.yy_utilities import get_last_chapter


class BookInfo(Item):
    last_chapter = Field(
        input_processor=MapCompose(get_last_chapter),
        output_processor=Join()
    )
