import scrapy

url = 'https://divar.ir/v/-/{token}'

token_file = open('...', 'r', encoding='utf8')
tokens = token_file.read().split(',')
token_file.close()

class DivarSpider(scrapy.Spider):
    name = 'divar'
    start_urls = [url.format(token=token) for token in tokens]

    def parse(self,response):
        informations = response.css('div span.kt-group-row-item__value::text')

        area = int(informations[0].extract())
        construction = int(informations[1].extract())
        rooms = int(informations[2].extract())

        warehouse = False if 'ندارد' in informations[3].extract() else True
        parking = False if 'ندارد' in informations[4].extract() else True
        elevator = False if 'ندارد' in informations[5].extract() else True

        address = response.css('div div.kt-page-title__subtitle--responsive-sized::text').extract()
        price = response.css('div p.kt-unexpandable-row__value::text').extract_first()
        
        yield {
            'Area': area,
            'Construction': construction,
            'Room': rooms,
            'Warehouse': warehouse,
            'Parking': parking,
            "Elevator": elevator,
            'Address': address,
            'Price': price
        }

