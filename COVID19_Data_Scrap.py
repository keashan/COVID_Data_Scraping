import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class COVIDData(scrapy.Spider):
    name='COVIDData_Downloader'

    def start_requests(self):
        url='https://www.worldometers.info/coronavirus/'
        yield scrapy.Request(url=url,callback=self.parse_COVIDData)

    def parse_COVIDData(self,response):
        data_header=response.css('table#main_table_countries_today>thead>tr>th')
        data_table=response.css('table#main_table_countries_today>tbody:nth-of-type(1)>tr')
        #data_table_rows=data_table.xpath('//tr')
        table_data=[]
        for row in data_table:
            table_row=row.css('::text').extract()
            clean_table_row=[t.strip() for t in table_row]
            table_data.append(clean_table_row)
        df=pd.DataFrame(table_data)
        clean_data_header=[]
        for data_header_text in data_header:
            col=data_header_text.css(' ::text').extract()
            col_clean=[t.strip() for t in col]
            col_text=''
            for item in col_clean:
                col_text=col_text+' ' + item
            clean_data_header.append(col_text)
        #df.columns=clean_data_header
        print(len(clean_data_header))
        df.to_csv(r'C:\Users\keash\Desktop\Test.csv',index=False)
process=CrawlerProcess()
process.crawl(COVIDData)
process.start()