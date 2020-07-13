# URLs
MAIN_PAGE = 'https://truyenyy.com/'
BASE_URL = 'https://truyenyy.com/truyen/{}/danh-sach-chuong?nf=yes'

# Book's info
BOOK_URL = '//a[starts-with(@href,"/truyen/")]/@href'
BOOK_LAST_CHAPTER_PATH = "//table[contains(@class,'table table-dark')]/tbody/tr[1]/td[1]/a/@href"
PREMIUM_TAG_PATH = "//a[contains(@href,'/chuong-vip')and @class='btn btn-warning']"

# Chapter's content
CHAPTER_URL = 'https://truyenyy.com/truyen/{0}/chuong-{1}.html'


# Top book urls
TOP_BOOK_URLS = '//*[contains(@class, "books-list")]/li/a/@href'
TOP_BOOK_TIME_URL = 'https://truyenyy.com/kim-thanh-bang/?year={0}&month={1}&page={2}'

# Genre
GENRE_URL = '//a[@class="genre" and starts-with(@href,"/truyen-")]/@href'
GENRE_PAGE_URL = 'https://truyenyy.com/{0}/danh-sach/?page={1}'
GENRE_LIST_URL = 'https://truyenyy.com/{0}/danh-sach/'
GENRE_LIST_PAGINATION_PATH = "//ul[contains(@class,'pagination')]//a[@class='page-link']/@href"
