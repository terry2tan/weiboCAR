# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from weiboCAR.items import CommentItem, AttitudeItem, RepostItem

class saveTxtPipeline(object):

    def process_item(self, item, spider):
        f = item["weiboID"]
        if isinstance(item, CommentItem):
            line = ""
            for v in item.values():
                line = line + v.encode("utf8") + "\t"
            with open(f+"_comment.txt","a") as outfile:
            	outfile.write(line+"\n")
        elif isinstance(item, AttitudeItem):
            line = ""
            for v in item.values():
                line = line + v.encode("utf8") + "\t"
            with open(f+"_attitude.txt","a") as outfile:
            	outfile.write(line+"\n")
        elif isinstance(item, RepostItem):
            line = ""
            for v in item.values():
                line = line + v.encode("utf8") + "\t"
            with open(f+"_repost.txt","a") as outfile:
            	outfile.write(line+"\n")
        else:
    		pass
        return item
            
