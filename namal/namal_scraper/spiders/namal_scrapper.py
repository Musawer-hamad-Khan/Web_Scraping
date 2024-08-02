
import scrapy

class NamalScrapperSpider(scrapy.Spider):
    name = "namal_scrapper"
    allowed_domains = ["namal.edu.pk"]
    start_urls = ["https://namal.edu.pk/faculty"]

    def parse(self, response):
        for profile_link in response.css('.neumorphic--pressed a::attr(href)').getall():
            yield response.follow(profile_link,callback=self.get_profile_info)
    def get_profile_info(self,response):
        prof_info=[]
        for li in response.css('.contact-info li'):
            if li.css('span::text').get():
                prof_info.append(li.css('span::text').get())
            else:
                prof_info.append(' ')        
        prof_dic_keys=['dept','contact','email']
        prof_info_dict={}
        prof_info_dict['name']= response.css('h2.font-weight-bold::text').get().strip()
        for index in range(len(prof_info)):
            prof_info_dict[prof_dic_keys[index]]=prof_info[index].strip()
        print(prof_info_dict)
        yield prof_info_dict
        
        

