from scrapy import Spider
from fdcrawler.items import DetailsItem


class DetailSpider(Spider):
    name = 'details'
    allowed_domains = ['epicure.co.kr']
    start_urls = [
        'https://www.epicure.co.kr/shop/introduce_detail.html?no=7000',
        'https://www.epicure.co.kr/shop/introduce_detail.html?no=42',
    ]
    #start_urls = ('https://www.epicure.co.kr/shop/introduce_detail.html?no={}'.format(i) for i in range(1, 2))

    def parse(self, response):
        #using xpath
        item = DetailsItem()

        try:
            #header-restaurant
            item['title'] = response.xpath('//td[@height=\"40\"]/p/text()[normalize-space()]').extract_first().strip()
            item['category'] = response.xpath('//td[@height=\"25\"]/text()').extract_first().replace(' ', '').replace('\n', '')
            item['scoreByFoodie'] = response.xpath('//td[@width=\"170\"]/text()').extract_first().strip()
            item['scoreByTaste'] = response.xpath('//td[@width=\"320\"]/table/tr[2]/td[1]/text()').extract_first().strip()

            #about-restaurant
            sel = response.xpath('//td[@width=\"310\"]/table')

            item['address'] = response.xpath('//span[2]/text()').extract_first().strip()
            item['tel'] = response.xpath('//td/b/text()').extract_first().strip()
            item['mainDish'] = response.xpath('//table/tr[1]/td[2]/a/text()').extract_first().strip()
            item['direction'] = sel.xpath('tr[2]/td/table/tr/td[2]/text()').extract_first().strip()
            item['openTime'] = sel.xpath('tr[3]/td/table/tr[1]/td[2]/text()').extract_first().strip()
            item['offDay'] = sel.xpath('tr[3]/td/table/tr[2]/td[2]/text()').extract_first().strip()
            item['reservation'] = sel.xpath('tr[4]/td/table/tr[2]/td[2]/text()').extract_first().strip()
            item['parking'] = sel.xpath('tr[4]/td/table/tr[3]/td[2]/text()').extract_first().strip()
            item['cost'] = sel.xpath('tr[4]/td/table/tr[4]/td[2]/a/text()').extract_first().strip()
            item['delivery'] = '없음'
            item['url'] = sel.xpath('tr[5]/td/table/tr[2]/td[2]/a/text()').extract_first().strip()

            # history-section
            item['history'] = response.xpath('//table[2]/tr[2]/td/p/text()').extract_first().strip()
            item['menu'] = response.xpath('//td[@height=\"70\"]/table/tr[2]/td[3]/text()').extract_first().strip()
            item['surtax'] = response.xpath('//td[@height=\"70\"]/table/tr[3]/td[3]/text()').extract_first().strip()

        except AttributeError as e:
            return

        yield item
