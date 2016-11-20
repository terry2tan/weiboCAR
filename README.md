# weiboCAR


##安装环境

1.python 2.7

2.win7(暂时未在OS系统里测试过，不过应该没有什么问题)



##依赖包

1.scrapy（安装：pip install scrapy）

2.beautifulSoup（安装：pip install beautifulsoup）



##使用方法：

1.在cookies.py里填上微博账号和密码；

```python
myWeiBo = [
    {'no': '用户名1填这里', 'psw': '密码1填这里'},
    {'no': '用户名2填这里', 'psw': '密码2填这里'},
]
```

2.在settings里WEIBO_IDS填上要抓的微博的ID;

```python
WEIBO_IDS = ["Ehf8SdHyq"]   #微博ID填在这里
```

>什么叫微博ID，比如http://weibo.com/1932835417/Ei8uMnP44?ref=home&rid=0_0_8_2596589918405690045, 在这个微博链接里，微博ID是 Ei8uMnP44

3、在文件夹路径下，执行

```
scrapy crawl weiboCAR -a methon=*
```

>*可以为repost(只抓转发)，comment（只抓评论），attitude（只抓点赞），all（前面三种都抓）。

如：

```
scrapy crawl weiboCAR -a methon=all
```
