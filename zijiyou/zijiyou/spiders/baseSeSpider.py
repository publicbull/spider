# -*- coding: utf-8 -*-
'''
Created on 2011-3-28

@author: shiym
'''
from scrapy import log
from scrapy.exceptions import NotConfigured
from scrapy.selector import HtmlXPathSelector
from zijiyou.items.itemLoader import ZijiyouItemLoader
from zijiyou.items.zijiyouItem import ResponseBody, Note
from zijiyou.spiders.baseCrawlSpider import BaseCrawlSpider
from zijiyou.spiders.spiderConfig import spiderConfig
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import datetime
import re
import time
import urllib


class BaseSeSpider(BaseCrawlSpider):
    '''
    Spider for www.daodao.com
    '''
    name ="baseSeSpider"
    
    #搜索引擎格式
    seUrlFormat=[]
    searchPageNum=5
    itemPriority=1000
    config=None
    seResultList=[]
    crawlUrl='CrawlUrl'
    
    def __init__(self,*a,**kw):
        super(BaseSeSpider,self).__init__(*a,**kw)
        
        self.config=spiderConfig[self.name]
        if not 'seUrlFormat' in self.config:
            log.msg("baseSeSpider的配置文件没有seUrlFormat!", level=log.ERROR)
            raise NotConfigured        
        self.seUrlFormat=self.config['seUrlFormat']
        self.functionDic['baseParse'] = self.baseParse
        dispatcher.connect(self.onSeSpiderClosed, signal=signals.spider_closed)
        
    def onSeSpiderClosed(self):
        '''清空数据库中的SeSpider中的搜索页列表'''
        log.msg('开始清空数据库中的SeSpider中的搜索页列表，长度：%s' %len(self.seResultList), level=log.INFO)
        if len(self.seResultList)>0:
            whereJson={}
            for url in self.seResultList :
                whereJson['url']=url
                self.mongoApt.remove(self.crawlUrl,whereJson)
                print '删除url:%s' % url
        self.seResultList=[]
        
    def makeRequestByKeywordForSEs(self):
        print '生成关键字搜索请求'
        log.msg("生成关键字搜索请求", level=log.INFO)
        '''
        由关键字创建SE的请求
        '''
        #load关键字
        reqs=[]
        keyWords=self.mongoApt.findByDictionaryAndSort('KeyWord', {}, 'priority')
        if not keyWords and len(keyWords)<1:
            log.msg("没有关键字！", level=log.ERROR)
            return []        
        for keyWord in keyWords:
            for v in self.seUrlFormat:
                for i in range(1, v['sePageNum']+1):
                    format=v['format']
                    encodeType=v['encode']
                    encodeWords=urllib.quote(keyWord['keyWord'].encode(encodeType))
                    pagePriority=keyWord['priority']
                    url=format % (encodeWords, i)
#                    print url
                    meta={'type':keyWord['type'],
                          'sePageNum':v['sePageNum'],
                          'resultItemLinkXpath':v['resultItemLinkXpath'],
                          'nextPageLinkXpath':v['nextPageLinkXpath'],
                          'seName':v['seName'],
                          'homePage':v['homePage']}
                    request=self.makeRequestWithMeta(url,callBackFunctionName='baseParse',meta=meta,priority=pagePriority)
                    reqs.append(request)
                    
                    self.seResultList.append(url)
        log.msg('生成了%s个关键字搜索请求' % len(reqs), level=log.INFO)
        return reqs
    
    def baseParse(self,response):
        print '解析搜索引擎结果'
        log.msg("解析搜索引擎结果", level=log.INFO)
        log.msg('解析link: %s' % response.url, level=log.INFO)
        reqs = []
        
        if not self.hasInit:
            self.hasInit=True
            if self.pendingRequest and len(self.pendingRequest)>0:
                reqs.extend(self.pendingRequest)
                log.msg('从数据库查询的url开始crawl，len(pendingRequest)= %s' % len(self.pendingRequest), log.INFO)
            else:
                log.msg('没有从数据库获得合适的url，将从stat_url开始crawl' , level=log.INFO)
            seReqs=self.makeRequestByKeywordForSEs()
            if seReqs and len(seReqs)>0:
                reqs.extend(seReqs)
            else:
                log.msg('关键字没有生成任何Request!，请检查配置文件spiderConfig中baseSeSpider的url格式或数据库关键字表',level=log.ERROR)
        #拦截
        if len(reqs)>0:
            log.msg('拦截Request。url： %s' % response.url, log.INFO)
            return reqs
        
        if not (response.meta and len(response.meta)>0):
            log.msg("没有meta的Response，无法进行目标页和下一页的定位：%s" % response.url, level=log.ERROR)
            return reqs
        meta=response.meta
#        print meta
        #item页链接请求
        itemsReq=[]
        homePage=meta['homePage']
        print homePage
        resultItemLinkXpath=meta['resultItemLinkXpath']
        hxs=HtmlXPathSelector(response)
        links=hxs.select(resultItemLinkXpath).extract()
        if links and len(links)>0:
            for link in links:
                link = homePage + link
                log.msg("%s"%link, log.INFO)
                req=self.makeRequestWithMeta(link, callBackFunctionName='parseItem', meta=meta,priority=self.itemPriority)
                itemsReq.append(req)
        else:
            log.msg("没有抓取到任何目标页链接！resultItemLinkXpath：%s；url：%s" % (resultItemLinkXpath,response.url), level=log.ERROR)
        reqs.extend(itemsReq)
        log.msg("%s parse 产生item页的Request数量：%s" % (response.url, len(itemsReq)), level=log.INFO)

        return reqs
    
    def parseItem(self,response):
        '''解析搜索目标页'''
        print '解析搜索目标页'
        log.msg("解析搜索目标页", level=log.INFO)
        items=[]
        
        meta=response.meta
        if not ('type' in meta and meta['type']):
            log.msg("没有type的item页！不能确定保存到那张表。url：%s" % response.url, level=log.ERROR)
            return items
        
        type=meta['type']
        log.msg("保存item页，类型:%s"%str(type) , level=log.INFO)
        #ResponseBody
        loader = ZijiyouItemLoader(ResponseBody(),response=response)
        loader.add_value('spiderName', self.name)
        loader.add_value('pageUrl', response.url)
        loader.add_value('type', type)
        loader.add_value('content', response.body_as_unicode())
        loader.add_value('dateTime', datetime.datetime.now())
        responseBody = loader.load_item()
        items.append(responseBody)
        
        #解析搜索引擎NoteItem
        noteItem = self.parseNoteItem(response)    
        if noteItem:
            items.append(noteItem)
        
        return items
    
    def parseNoteItem(self, response):
        '''解析搜索引擎NoteItem'''
        log.msg("解析搜索引擎NoteItem", level=log.INFO)
        #判断配置是否正确
        if not ('seXpath' in self.config and response.meta['seName'] in self.config['seXpath']):
            log.msg("配置文件中缺少seXpath配置或seXpath中缺少%s的配置" % response.meta['seName'], level=log.ERROR)
            return
        
        xpathItems = self.config['seXpath'][response.meta['seName']]
        hxs=HtmlXPathSelector(response)
        loader = ZijiyouItemLoader(Note(),response=response)
        for k,v in xpathItems.items():
            values = hxs.select(v).extract()
            value=("-".join("%s" % p for p in values)).encode("utf-8")
            if value:
                if(k == 'date'):
                    value = re.search(r"\d{4}年\d{2}月\d{2}日$", value)
                    if value:
                        loader.add_value(k, value.group(0))
                    else:
                        loader.add_value(k, time.strftime("%Y年%m月%d日"))
                else:
                    loader.add_value(k, value)
        loader.add_value('pageUrl', response.url)
        noteItem = loader.load_item()
        return noteItem
        
    
SPIDER = BaseSeSpider()