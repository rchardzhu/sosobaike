from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from sosobaike.items import SosobaikeItem

class SosobkSpider(BaseSpider):
    name = "sosobk"
    allowed_domains = ["soso.com"]
    start_urls = []
#    start_urls = (
#        'http://www.soso.com/',
#        )

    def __init__(self):
        for i in range(0, 5000):
            url = "http://baike.soso.com/Search.e?sp=S&sp=F&sp=S%E4%BA%BA%E7%89%A9&p=" + str(i)
            #url = "http://baike.soso.com/Search.e?sp=S&sp=F&sp=S%E4%BA%92%E8%81%94%E7%BD%91&p=" + str(i)
            self.start_urls.append(url)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        urllist = hxs.select("//div[@class='newscont wh_550']/font/a/@href").extract()
        items = []
        for url in urllist:
            item = SosobaikeItem()
            item['url'] = 'http://baike.soso.com' + url
            items.append(item)

        return items
