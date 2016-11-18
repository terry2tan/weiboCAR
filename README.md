# weiboCAR


##安装环境
python 2.7
win7

##依赖包
scrapy
beautifulSoup

使用方法：
1、在cookies.py里填上微博账号和密码；

2、在settings里WEIBO_IDS填上要抓的微博的ID

什么叫微博ID，比如http://weibo.com/1932835417/Ei8uMnP44?ref=home&rid=0_0_8_2596589918405690045, 在这个微博链接里，微博ID是 Ei8uMnP44

3、在文件夹路径下，执行 scrapy crawl weiboCAR -a methon=*

*可以为repost(只抓转发)，comment（只抓评论），attitude（只抓点赞），all（前面三种都抓）。
