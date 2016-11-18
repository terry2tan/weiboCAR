# encoding=utf-8

from scrapy.spiders import CrawlSpider
from weiboCAR.items import CommentItem, AttitudeItem, RepostItem
from scrapy.http import Request
from bs4 import BeautifulSoup
from weiboCAR import settings

class WeiboCAR(CrawlSpider):
    host = "http://weibo.cn"
    name = "weiboCAR"
    allowed_domains = ["weibo.cn"]
    start_urls = settings.WEIBO_IDS
    weiboIDs = set(start_urls)

    def start_requests(self):
        
        method = getattr(self, 'method', None)        
        
        for weiboID in self.start_urls:
            comment_url = "http://weibo.cn/comment/%s?page=1" %weiboID
            attitude_url = "http://weibo.cn/attitude/%s?page=1" %weiboID
            repost_url = "http://weibo.cn/repost/%s?page=1" %weiboID
        if method is not None:
            if method == "attitude":
                yield Request(url=attitude_url, callback=self.parseA, meta={"weiboID":weiboID})
            elif method == "comment":
                yield Request(url=comment_url, callback=self.parseC, meta={"weiboID":weiboID})
            elif method == "repost":
                yield Request(url=repost_url, callback=self.parseR, meta={"weiboID":weiboID})
            else:
                yield Request(url=comment_url, callback=self.parseC, meta={"weiboID":weiboID})
                yield Request(url=repost_url, callback=self.parseR, meta={"weiboID":weiboID})
                yield Request(url=attitude_url, callback=self.parseA, meta={"weiboID":weiboID})
        else:
            print "请输入参数method，可能的取值为comment(只抓评论)，repost(只抓转发)，attitude(只抓点赞)，all(三种都抓)"
                
            

    def parseC(self,response):
        """ 提取评论信息 """
        html = response.text
        soup = BeautifulSoup(html,"html.parser",from_encoding="utf8")
        comments = soup.find_all("div",{"class":"c"})
         
        for c in comments:
            try:
                item = CommentItem()
                item["weiboID"] = response.meta["weiboID"]
                item["userId"] = str(c.get("id"))
                item["userName"] = c.find("a").text
                item["userUrl"] = c.find("a").get("href")
                item["commentLike"] = c.find("span",{"class":"cc"}).find("a").text
                item["commentText"] = c.find("span",{"class":"ctt"}).text
                item["commentTime"] = c.find("span",{"class":"ct"}).text.strip()
                yield item
            except:
                pass
            
            next_url = None
            try:
                next_url = soup.find("div",{"id":"pagelist"}).find("form").find("a",text=r'下页').get("href")
            except:
                pass

        if next_url:
        	yield Request(url=self.host+next_url, callback=self.parseC,meta={"weiboID":response.meta["weiboID"]})
        else:
        	pass

    def parseA(self,response):
            """ 提取点赞信息 """
            html = response.text
            soup = BeautifulSoup(html,"html.parser",from_encoding="utf8")
            comments = soup.find_all("div",{"class":"c"})
             
            for c in comments:
                try:
                    item = AttitudeItem()
                    item["weiboID"] = response.meta["weiboID"]
                    item["userName"] = c.find("a").text
                    item["userUrl"] = c.find("a").get("href")
                    item["attitudeTime"] = c.find("span",{"class":"ct"}).text.strip()
                    yield item
                except:
                    pass
                
                next_url = None
                try:
                    next_url = soup.find("div",{"id":"pagelist"}).find("form").find("a",text=r'下页').get("href")
                except:
                    pass
    
            if next_url:
            	yield Request(url=self.host+next_url, callback=self.parseA,meta={"weiboID":response.meta["weiboID"]})
            else:
            	pass

    def parseR(self,response):
            """ 提取转发信息 """
            html = response.text
            soup = BeautifulSoup(html,"html.parser",from_encoding="utf8")
            comments = soup.find_all("div",{"class":"c"})
            print len(comments)
            for c in comments:
                try:
                    item = RepostItem()
                    item["weiboID"] = response.meta["weiboID"]
                    item["userName"] = c.find("a").text
                    item["userUrl"] = c.find("a").get("href")
                    texts = c.find_all(text=True)
                    texts = [t.strip() for t in texts if t.strip() != ""]
                    item["repostText"] = "".join(texts[1:-2])
                    item["repostTime"] = c.find("span",{"class":"ct"}).text.strip()
                    item["repostLike"] = c.find("span",{"class":"cc"}).find("a").text
                    yield item
                except:
                    pass
                
                next_url = None
                try:
                    next_url = soup.find("div",{"id":"pagelist"}).find("form").find("a",text=r'下页').get("href")
                except:
                    pass
    
            if next_url:
            	yield Request(url=self.host+next_url, callback=self.parseR,meta={"weiboID":response.meta["weiboID"]})
            else:
            	pass







