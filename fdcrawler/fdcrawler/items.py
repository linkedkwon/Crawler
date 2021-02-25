# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class DetailsItem(scrapy.Item):
    # headar-restaurant
    title = scrapy.Field()
    category = scrapy.Field()
    scoreByFoodie = scrapy.Field()
    scoreByTaste = scrapy.Field()

    #about-restaurant
    address = scrapy.Field()
    tel = scrapy.Field()
    direction = scrapy.Field()
    openTime = scrapy.Field()
    offDay = scrapy.Field()
    mainDish = scrapy.Field()
    reservation = scrapy.Field()
    parking = scrapy.Field()
    cost = scrapy.Field()
    delivery = scrapy.Field()
    url = scrapy.Field()

    #history-section
    history = scrapy.Field()
    menu = scrapy.Field()
    surtax = scrapy.Field()


