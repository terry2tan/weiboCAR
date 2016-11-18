# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class CommentItem(Item):
    """ 微博评论 """
    weiboID = Field()
    userId = Field() #评论者ID
    userName = Field() #评论者
    userUrl = Field()  #评论者首页
    commentLike = Field() #评论被点赞数
    commentText = Field() #评论内容
    commentTime = Field() #发布时间

class AttitudeItem(Item):
    """ 微博点赞 """
    weiboID = Field()
    userName = Field() #点赞者
    userUrl = Field()  #评论者首页
    attitudeTime = Field() #发布时间

class RepostItem(Item):
    """ 微博转发 """
    weiboID = Field()
    userName = Field() #转发者
    userUrl = Field()  #评论者首页
    repostText = Field() #转发内容
    repostLike = Field() #点赞数
    repostTime = Field() #发布时间
    
    
