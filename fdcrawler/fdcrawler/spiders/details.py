from scrapy import Spider
from fdcrawler.items import DetailsItem
import re

class DetailSpider(Spider):
    name = 'details'
    allowed_domains = ['epicure.co.kr']
    start_urls = ('https://www.epicure.co.kr/shop/introduce_detail.html?no={}'.format(i) for i in range(1, 100))

    def parse(self, response):
        """
        #xpath based scrapping
        #section1. text data sets
        """
        item = DetailsItem()

        #header-restaurant
        #Handling pages that data aren't stored
        item['title'] = response.xpath('//td[@height=\"40\"]/p/text()').extract()[0].strip()
        if len(item['title']) is 0:
            return

        item['category'] = response.xpath('//td[@height=\"25\"]/text()').extract()[0].replace('\n', '').replace(' ', '')
        item['scoreByFoodie'] = response.xpath('//td[@width=\"170\"]/text()').extract()[0].strip()
        item['scoreByTaste'] = response.xpath('//td[@width=\"320\"]/table/tr[2]/td[1]/text()').extract()[0].strip()

        #about-restaurant
        sel = response.xpath('//td[@width=\"310\"]/table')

        item['address'] = response.xpath('//span[2]/text()').extract()[0].strip()
        item['tel'] = response.xpath('//td/b/text()').extract()
        item['mainDish'] = response.xpath('//table/tr[1]/td[2]/a/text()').extract()[0].strip()
        item['direction'] = sel.xpath('tr[2]/td/table/tr/td[2]/text()').extract()[0].strip()
        item['openTime'] = sel.xpath('tr[3]/td/table/tr[1]/td[2]/text()').extract()
        item['offDay'] = sel.xpath('tr[3]/td/table/tr[2]/td[2]/text()').extract()
        item['reservation'] = sel.xpath('tr[4]/td/table/tr[2]/td[2]/text()').extract()
        item['parking'] = sel.xpath('tr[4]/td/table/tr[3]/td[2]/text()').extract()
        item['cost'] = sel.xpath('tr[4]/td/table/tr[4]/td[2]/a/text()').extract()[0].strip()
        item['delivery'] = '없음'
        item['url'] = sel.xpath('tr[5]/td/table/tr[2]/td[2]/a/text()').extract()

        # history-section
        item['history'] = re.sub('<.+?>', '', response.xpath('//table[2]/tr[2]/td[1]').extract()[0]).strip()

        #menu section
        item['menu'] = response.xpath('//td[@height=\"70\"]/table/tr[2]/td[3]/text()').extract()
        item['surtax'] = response.xpath('//td[@height=\"70\"]/table/tr[3]/td[3]/text()').extract()[0].strip()

        yield item

