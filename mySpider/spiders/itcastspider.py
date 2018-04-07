import scrapy
from mySpider.items import ItcastItem
"""
爬取传智播客师资库老师信息
"""
class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowd_domains = ["http://www.itcast.cn/"]
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]

    def parse(self, response):
        # with open("teacher.html","wb") as f:
        #     f.write(response.body)
        teacher_list = response.xpath('//div[@class="li_txt"]')
        #teacherItem = []
        for each in teacher_list:
            item  = ItcastItem()
            #.extract() 将匹配出来的对象转换为Unicode字符串，不过好像不用也可以
            #老师名称
            name = each.xpath('./h3/text()').extract()
            #老师职称
            title = each.xpath('./h4/text()').extract()
            #老师过往经历
            info = each.xpath('./p/text()').extract()
            item['name'] = name[0]
            item['title'] =title[0]
            item['info'] =info[0]

            #teacherItem.append(item )
            yield item    #将获取的数据交给pipelines
        #return teacherItem    #不将获取的数据交给pipelines