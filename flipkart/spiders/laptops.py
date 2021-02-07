import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which
from scrapy.selector import Selector
from time import sleep

#github scrapy_seleinum is installed now.
from scrapy_selenium import SeleniumRequest
counter = 24 

class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/search?q=laptops&otracker=searchhttps%3A%2F%2Fwww.flipkart.com%2Fsearch%3Fq%3Dlaptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=2']
    
    # def __init__(self):
    #     #inside it we do everything releated to selenium
    #     # chrome_options = Options()
    #     # chrome_options.add_argument("--headless")   # to prevent chrome from launching
    #     options = webdriver.ChromeOptions()
    #     options.add_argument('--ignore-certificate-errors')
    #     options.add_argument('--ignore-ssl-errors')
    #     # driver = webdriver.Chrome(chrome_options=options)

    #     chrome_path = which("chromedriver")
    #     driver = webdriver.Chrome(executable_path= chrome_path)
    #     # driver.get("http://www.flipkart.com")
    #     sleep(10)
    #     driver.implicitly_wait(10)
    #     # driver = webdriver.Chrome(executable_path= chrome_path, options=chrome_options)
    #     login_box = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
    #     login_box.click()
    #     sleep(5)

    #     search_input = driver.find_element_by_xpath("//div[@class='_3OO5Xc']")
    #     search_input.send_keys("laptop")


    #     search_btn = driver.find_element_by_xpath("//button[@class='L0Z3Pu']")
    #     search_btn.click()

       
    #     sleep(5)
    #     self.html = driver.page_source
    #     # driver.close()
    #     print(self.html)

    
    
    def parse(self, response):
        global counter
        # resp = Selector(text = self.html)
        for product in response.xpath("//div[@class='_13oc-S']"):
            counter = counter+1
            

            yield{
                'counter' : counter ,
                'product_name' : product.xpath(".//div[@class='_4rR01T']/text()").get(),
                'price' : product.xpath(".//div[@class='_30jeq3 _1_WHN1']/text()").get(),
                # 'url' : product.xpath(".//a[@class='_1fQZEK']/@href").get(),
                'url' : response.urljoin(product.xpath(".//a[@class='_1fQZEK']/@href").get()),
                'star' : product.xpath(".//div[@class='_3LWZlK']/text()").get(),
                'rating' : product.xpath(".//span[@class='_2_R_DZ']/span/span[1]/text()").get(),
                'reviews' : product.xpath(".//span[@class='_2_R_DZ']/span/span[3]/text()").get(),
                

            }

        # to scrape multiple pages
        # rel_url = response.xpath("//a[@class = 'page-link' and @rel ='next']/@href").get()
        next_page = response.urljoin(product.xpath("//a[@class = '_1LKTO3'][2]/@href").get())

        #check if the next page exist or not?
        if next_page:
            yield scrapy.Request(url = next_page, callback=self.parse)








            #we can't define the callback method into the seleinum
            #so this parse method simply not work
            #so we pass the self.html to parse method
            #but self.html is a string object so we can't directely pass it.
            #for that we use selector object
            # from scrapy.selector import Selector
            # resp = Selector(text = self.html)
            # now resp is a selector object so we can execute xpath against it
            # so we change response.xpath -> resp.xpath


