# -*- coding: utf-8 -*-

spiderConfig = {
                "baseSeSpider":{
                     'allowedDomains':[],
                     'startUrls':['http://www.baidu.com'],
                     'seUrlFormat':[{'seName':'sosoBlog',
                                     'format':'http://blog.soso.com/qz.q?sc=qz&pid=qz.s.res&ty=blog&st=r&op=blog.blog&sd=0&w=%s&pg=%s',#搜索格式
#                                     'sePageNum':5,
                                     'encode':'GBK',
                                     'resultItemLinkXpath':'//div[2]/div[2]/div[2]/ol/li/a/@href',
                                     'nextPageLinkXpath':'//div[@class="page"]/div[@class="pg"]/a/@href',
                                     'totalRecordXpath':'//div[@id="sNum"]/text()',
                                     'totalRecordRegex':r'[\d|,]+',
                                     'nextPagePattern':'http://blog.soso.com/qz.q?w=keyWord&sc=qz&ty=blog&sd=0&st=r&cid=&op=blog.blog&pid=qz.s.res&pg=pageNum',#无法通过xpath获得js动态生成的下一页区域，使用模板
                                     'homePage':'http://blog.soso.com'                                  
                                     }],
                    'seXpath':{
                               "sosoBlog":{
                                    r'title':r'//ol/li/h3/a',
                                    r'publishDate':r'//ol/li/h3/text()',
                                    r'content':None,
                                    r'abstract':r'//ol/li'
                                    }
                               },
                     #普通list页正则表达式
                     'normalRegex':[
                                    "http://blog.soso.com/qz\.q"
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[]
                     },
		     
                "daodaoSpider":{
                     'allowedDomains':["daodao.com"],
                     'startUrls':['http://www.daodao.com/Attractions-g294211-Activities-China.html'],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'Tourism-g\d+-.*-Vacations\.html$', 'priority':10},
                                    {'regex':r'Attractions-g\d+-Activities-.*\.html$', 'priority':50},
                                    {'regex':r'Tourism-g\d+-c\d+-[^n].*\.html((\?pg=\d+)?|(\?kw=.*&st=8))$', 'priority':50} #包括游记列表、标签
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Attraction','regex':r'Attraction_Review-g\d+-.*-Reviews-.*\.html$', 'priority':600},  #AttractionItem
                                  {'itemCollectionName':'Article','regex':r'Tourism-g\d+-c\d+-n\d+.*\.html$', 'priority':500},              #NoteItem
                                  {'itemCollectionName':'Note','regex':r'Changshi-g\d+-.*\.html$', 'priority':500}                       #CommonSenseItem
                                  ]
                     },

		  #55bbs需要修改
		  "55BBSSpider":{
                     'allowedDomains':["55bbs.com"],
                     'startUrls':['http://bbs.55bbs.com/forumdisplay.php?fid=34&filter=digest&page=1'],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'http://bbs.55bbs.com/forumdisplay\.php\?fid=34&filter=digest', 'priority':1000}
                                   
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Article','regex':r'thread-\d+-\d+-\d+.html', 'priority':600}  #AttractionItem
                                 
                                  ]
                     },

		  "yahooSpider":{
                     'allowedDomains':["travel.cn.yahoo.com" ],
                     'startUrls':[ 
		                   'http://travel.cn.yahoo.com/yxk/category/581/',
				    'http://travel.cn.yahoo.com/yxk/category/586/',
				    'http://travel.cn.yahoo.com/yxk/category/586/',
				    'http://travel.cn.yahoo.com/yxk/category/574/',
				    'http://travel.cn.yahoo.com/yxk/category/562/',
				    'http://travel.cn.yahoo.com/yxk/category/557/',
				    'http://travel.cn.yahoo.com/',
				    'http://travel.cn.yahoo.com/travel_gonglve.html'			  
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://travel.cn.yahoo.com/store/d+/$', 'priority':1000},
				    {'regex':r'^http://travel.cn.yahoo.com/area/\w+\.html$', 'priority':1000},
				    {'regex':r'^http://travel.cn.yahoo.com/yxk/category/\d+/index_\d+.html$', 'priority':1000},
				    {'regex':r'^http://travel.cn.yahoo.com/store/\d+/article-\d+-list.html$', 'priority':1000}
				   		     
                                    
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Article','regex':r'^http://travel.cn.yahoo.com/ypen/\d+/\d+\.html$', 'priority':600},  #Article
                                 {'itemCollectionName':'Article','regex':r'^http://travel.cn.yahoo.com/store/\d+/article-\d+-item.html$', 'priority':600},
				 {'itemCollectionName':'Article','regex':r'^http://travel.cn.yahoo.com/yxk/category/\d+/\w+.html$', 'priority':600},
				 {'itemCollectionName':'Article','regex':r'^http://travel.cn.yahoo.com/newspic/travel/\d+/$', 'priority':600},
				 {'itemCollectionName':'Article','regex':r'^http://travel.cn.yahoo.com/newspic/travel/\d+/\d+/$', 'priority':600}
				  
                                 ]
                     },	

		 
		 "lvrenSpider":{
                     'allowedDomains':["d.lvren.cn"],
                     'startUrls':[ 
		                   'http://d.lvren.cn/guide/',
				   'http://news.lvren.cn'],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://news.lvren.cn/plus/list.php\?tid=\d+$', 'priority':1000},
				    {'regex':r'^http://news.lvren.cn/plus/list.php\?tid=\d+&TotalResult=\d+&PageNo=\d+$', 'priority':1000},
				    {'regex':r'^http://d.lvren.cn/youji/\w+/$', 'priority':1000},
				    {'regex':r'^http://d.lvren.cn/youji/\w+_p\d+/$', 'priority':1000}
				   		     
                                    
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Article','regex':r'^http://news.lvren.cn/html/.*\.html$', 'priority':600},  #Article
                                 {'itemCollectionName':'Article','regex':r'http://d.lvren.cn/gonglue/\w+/', 'priority':600},  #Article
				 {'itemCollectionName':'Article','regex':r'http://d.lvren.cn/youji/\w+_\d+/', 'priority':600}				
                                 ]
                     },

		   "sozhenSpider":{
                     'allowedDomains':["sozhen.com"],
                     'startUrls':[ 
		                   'http://www.sozhen.com/'
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://www.sozhen.com/\w+/$', 'priority':1000},
				    {'regex':r'^http://www.sozhen.com/default/chinatown_\d+.html$', 'priority':1000},
				    {'regex':r'^http://www.sozhen.com/default/townarticle_\d+.html$', 'priority':1000},
				    {'regex':r'^http://www.sozhen.com/default/newsarticle_\d+_\d+.html$', 'priority':1000}
				   		     
                                    
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Article','regex':r'^http://www.sozhen.com/default/\w+con_\d+_\d+.html$', 'priority':600},  #Article
                                 		
                                 ]
                     },

		   "21cnSpider":{
                     'allowedDomains':["travel.21cn.com"],
                     'startUrls':[ 'http://travel.21cn.com/'],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'http://travel.21cn.com/.*/list\d+.shtml', 'priority':1000}
                                   
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Article','regex':r'http://travel\.21cn\.com/\w+/\w+/\d+/\d+/\d+/\d+\.shtml', 'priority':600},  #Article
                                  {'itemCollectionName':'Article','regex':r'http://travel\.21cn\.com/\w+/\w+/\d+/\d+/\d+/\d+_\d+.shtml', 'priority':600}  #Article
                                  ]
                     },
		 
		 
		
		 "meishiSpider":{
                     'allowedDomains':["meishiditu.com" ],
                     'startUrls':[ 		                   
				    'http://www.meishiditu.com/'			  
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://www.meishiditu.com/food/foodlist.php\?area=\w+&page=\d+$', 'priority':1000}
				   
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
                                  {'itemCollectionName':'Article','regex':r'^http://www.meishiditu.com/food/showpage.php\?id=\d+$', 'priority':600}  #Article
                                 ]
                     },	

		"hexunSpider":{
                     'allowedDomains':["travel.hexun.com" ],
                     'startUrls':[ 		                   
				    'http://travel.hexun.com'			  
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://travel.hexun.com/[^//]+/index(-\d+)*.html$', 'priority':1000}
				   
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
                                  {'itemCollectionName':'Article','regex':r'^http://travel.hexun.com/\d{4}-\d{2}-\d{2}/\d+(_\d+)*.html$', 'priority':600}  #Article
                                 ]
                     },	


		"peopleSpider":{
                     'allowedDomains':["travel.people.com.cn" ],
                     'startUrls':[ 		                   
				    'http://travel.people.com.cn'			  
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://travel.people.com.cn/GB/(\d+/)+index\d*.html$', 'priority':1000}
				   
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
                                  {'itemCollectionName':'Article','regex':r'^http://travel.people.com.cn/GB/(\d+/)*\d+.html$', 'priority':600}  #Article
                                 ]
                     },	


		 "sinaSpider":{
                     'allowedDomains':["travel.sina.com.cn" ],
                     'startUrls':[ 		                   
				    'http://travel.sina.com.cn'			  
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://travel.sina.com.cn/.*/index.html$', 'priority':1000},
				    {'regex':r'^http://travel.sina.com.cn/.*/$', 'priority':1000},
				    {'regex':r'^http://travel.sina.com.cn/.*/list.html$', 'priority':1000}
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Article','regex':r'^http://travel.sina.com.cn/.*/\d+-\d+-\d+/\d+(_\d+)*.shtml$', 'priority':600},  #Article
                                  {'itemCollectionName':'Article','regex':r'^http://blog.sina.com.cn/s/blog_\w+.html', 'priority':600}  #Article
                                 ]
                     },	

		 "lvyou114Spider":{
                     'allowedDomains':["www.lvyou114.com" ],
                     'startUrls':[ 		                   
				    'http://www.lvyou114.com/Youji/'			  
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://www.lvyou114.com/Youji/[Cc]lass.asp\?[Cc]lassID=\d+(&page=\d+)*$', 'priority':1000}
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[{'itemCollectionName':'Article','regex':r'^http://www.lvyou114.com/Youji/\d+/\d+.html$', 'priority':600},  #Article
                                 
                                 ]
                     },	

		 "bbkerSpider":{
                     'allowedDomains':["www.bbker.com" ],
                     'startUrls':[ 		                   
				    'http://www.bbker.com'			  
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://www.bbker.com/bbker/\w+(/doclist/)*(\w+.html)*$', 'priority':1000},
				    #{'regex':r'^http://www.bbker.com/tag/[%\w\d]+.html$', 'priority':1000},
				    #{'regex':r'^http://www.bbker.com/tag/doc/[%\w\d]+/(\d+.html)*$', 'priority':1000},
				    {'regex':r'^http://www.bbker.com/bbker/\w+/doclist/volumn/[%\w\d]+/$', 'priority':1000}

                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
		                  {'itemCollectionName':'Article','regex':r'^http://www.bbker.com/D\w+.html$', 'priority':600}  #Article                                 
                                 ]
                     },	
		
		
		 "sohuSpider":{
                    'allowedDomains':["travel.sohu.com" ,"jingqu.travel.sohu.com","outdoor.travel.sohu.com"],
                     'startUrls':[ 		                   
				    'http://jingqu.travel.sohu.com',
				    'http://travel.sohu.com'	
				   ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'^http://travel.sohu.com/.*$', 'priority':1000},
				    {'regex':r'^http://jingqu.travel.sohu.com/.*$', 'priority':1000},
				    {'regex':r'^http://outdoor.travel.sohu.com/.*$', 'priority':1000}

                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
		                  {'itemCollectionName':'Article','regex':r'^http://travel.sohu.com/2\d{7}/n\d+(_\d+)*.shtml$', 'priority':600},  #Article  
				  {'itemCollectionName':'Article','regex':r'^http://outdoor.travel.sohu.com/2\d{7}/n\d+(_\d+)*.shtml$', 'priority':600},  #Article  
				  {'itemCollectionName':'POI','regex':r'^http://jingqu.travel.sohu.com/\w+-\d+.shtml$', 'priority':600},  #POI
				  {'itemCollectionName':'PICS','regex':r'^http://pic.travel.sohu.com/group-\d+.shtml$', 'priority':600} ,#Article 
				  {'itemCollectionName':'PICS','regex':r'^ http://travel.sohu.com/\d+/\d+/travel_article\d+.shtml$', 'priority':600}  #Article 
                                 ]
                     },	
		
		 "lotourSpider":{
                    
                     'allowedDomains':["d.lotour.com","abroad.lotour.com" ,"outdoor.lotour.com","leisure.lotour.com","chn.lotour.com","bjaround.lotour.com","sharound.lotour.com","gdaround.lotour.com","scaround.lotour.com","news.lotour.com","golden.lotour.com"],
                     'startUrls':[                  
				   "http://www.lotour.com/sitemap.html"				   
				   ],
                     #普通list页正则表达式
                     'normalRegex':[		                   
                                    {'regex':r'^http://\w+\.lotour\.com/\w+/index_\d+.shtml$', 'priority':1000},
				    {'regex':r'^http://\w+\.lotour\.com/\w+/*$', 'priority':1000},
				    {'regex':r'^http://\w+\.lotour\.com/*$', 'priority':1000}
				   
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
		                      {'itemCollectionName':'POI','regex':r'^http://d.lotour.com/\w+/*$', 'priority':1000} , #Article 
				      {'itemCollectionName':'Article','regex':r'^http://\w+.lotour.com/\w+/20\d{6}/\w+\.shtml$', 'priority':600},  #Article 
				      {'itemCollectionName':'Article','regex':r'^http://www.lotour.com/snapshot/\d+-\d+-\d+/snapshot(_\d+)+.shtml$', 'priority':300}  #Article 

		                 ]                     
                     },	
		

		 "9tourSpider":{
                    
                     'allowedDomains':["www.9tour.cn"],
                     'startUrls':[                  
				   "http://www.9tour.cn/info/"				   
				   ],
                     #普通list页正则表达式
                     'normalRegex':[		                   
                                    {'regex':r'^http://www.9tour.cn/info/news_0_\d+_\d+/$', 'priority':1000}
				   
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[              
				    
				      {'itemCollectionName':'Article','regex':r'^http://www.9tour.cn/info/\d+/\d+(_\d+)*.shtml$', 'priority':300}  #Article 

		                 ]                     
                     },	

		 "17uSpider":{
                     'allowedDomains':["www.17u.com"],
                     'startUrls':[ 		                   
				   "http://www.17u.com",
				   "http://www.17u.com/blog/",
				   ],
                     #普通list页正则表达式
                     'normalRegex':[		                   
                                    {'regex':r'^http://www.17u.com/news/newslist_\d+_\d+_\d+_c.html$', 'priority':1000},
				    {'regex':r'^http://www.17u.com/blog/scenery/1951(_0/\d+)*$', 'priority':1000},
				    {'regex':r'^http://www.17u.com/blog/\d+(/\d+)*$', 'priority':1000},
				    {'regex':r'^http://www.17u.com/blog/cata/\d+$', 'priority':1000},		
				    {'regex':r'^http://www.17u.com/blog/\w+/$', 'priority':1000},
				   
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
		                      {'itemCollectionName':'POI','regex':r'^http://www.17u.com/destination/(scenery|city|province|country)_\d+.html$', 'priority':1000} , #Article 
				      {'itemCollectionName':'Article','regex':r'^http://www.17u.com/news/shownews\w+\.html$', 'priority':600},  #Article 
				      {'itemCollectionName':'Article','regex':r'^http://www.17u.com/blog/article/\d+.html$', 'priority':300}  #Article 
		                 
				
				 
				 ]         
                     },	


		
		 "mafengwoSpider":{
                     'allowedDomains':["www.mafengwo.cn"],
                     'startUrls':[ 		                   
				   "http://www.mafengwo.cn"				   
				   ],
                     #普通list页正则表达式
                     'normalRegex':[		                   
                                    {'regex':r'^http://www.mafengwo.cn/mdd/smap.php\?mddid=\d+$', 'priority':1000},
				    {'regex':r'^http://www.mafengwo.cn/mdd/detail.php\?mddid=\d+&sort=&start=\d+$', 'priority':1000}
				  
				
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
		                      {'itemCollectionName':'POI','regex':r'^http://www.mafengwo.cn/travel-scenic-spot/mafengwo/\d+.html$', 'priority':1000} , #Article 
				      {'itemCollectionName':'PROFILE','regex':r'^http://www.mafengwo.cn/u/\d+.html$', 'priority':1000} , #Article
				      {'itemCollectionName':'Article','regex':r'^http://www.mafengwo.cn/i/\d+.html$', 'priority':600},  #Article 
				                    
				
				 
				 ]
                     },	


		"bytravelSpider":{
                     'allowedDomains':["bytravel.cn"],
                     'startUrls':[ 		                   
				   "http://www.bytravel.cn"				   
				   ],
                     #普通list页正则表达式
                     'normalRegex':[		                   
                                  {'regex':r'^http://\w+.bytravel.cn/{0,1}$', 'priority':1000},
				  {'regex':r'^http://\w+.bytravel.cn/v/index\d+.html$', 'priority':1000},
				  {'regex':r'^http://\w+.bytravel.cn/v/\d+/$', 'priority':1000},
                                  {'regex':r'^http://\w+.bytravel.cn/Scenery/[\w\d]+/(\d+/)*$', 'priority':1000},
                                   ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
		                      {'itemCollectionName':'ARTICLE','regex':r'^http://\w+.bytravel.cn/art/[\d\w-]+/[\d\w\-\%\(\)\!]+/(index\d+.html)*$', 'priority':1000} , #Article
				      {'itemCollectionName':'ARTICLE','regex':r'^http://\w+.bytravel.cn/(art|Scenery)/(.*).html$', 'priority':1000} , #Article				      
				      {'itemCollectionName':'ARTICLE','regex':r'^http://shop.bytravel.cn/produce/[\w\d]+/$', 'priority':1000} , #Article				     
				 ]
                     },	


		 "QQBlogSpider":{
                     'allowedDomains':["blog.qq.com","user.qzone.qq.com","user.qzone.qq.com"],
                     'startUrls':['http://blog.qq.com/travel/',
				  'http://bbs.blog.qq.com/b-1001026847/l-1.html',
				],
                     #普通list页正则表达式
                     'normalRegex':[
                                  
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
                                  {'itemCollectionName':'Article','regex':r'http://user.qzone.qq.com/\d+/blog/\d+', 'priority':500},   #ArticleItem
			          {'itemCollectionName':'Article','regex':r'http://bbs.blog.qq.com/b-\d+/\d+\.htm', 'priority':500},   #ArticleItem
				  {'itemCollectionName':'Article','regex':r'http://blog.qq.com/qzone/\d+/\d+\.htm', 'priority':500},   #ArticleItem
                                  ]
                     },
		   
                "lvpingSpider":{
                     'allowedDomains':["lvping.com"],
                     'startUrls':[
                                  'http://www.lvping.com/NorthAmericaNavigation.aspx',
                                  'http://www.lvping.com/EuropeNavigation.aspx',
                                  'http://www.lvping.com/AsiaNavigation.aspx',
                                  'http://www.lvping.com/ChinaNavigation.aspx',
                                  'http://www.lvping.com/OceaniaNavigation.aspx',
                                  'http://www.lvping.com/southAmericaNavigation.aspx',
                                  'http://www.lvping.com/AfricaNavigation.aspx',

#                                  #游记攻略
                                  'http://www.lvping.com/Journals.aspx?type=1',
                                  'http://www.lvping.com/Journals.aspx?selecttype=2',
                                  'http://www.lvping.com/Journals.aspx'
                                   
                                  ],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'(http://www.lvping.com/)?(tourism)+-g\d+-\w+\.html$', 'priority':200}, #国家
                                    {'regex':r'(http://www.lvping.com/)?(attractions-)+d\d+-\w+\.html$', 'priority':400}, #景点列表
                                    {'regex':r'(http://www.lvping.com/)?(attractions-)+d\d+-s\d+-[r]+\w+\d+/\w+:\w+\.html$', 'priority':500}, #景点列表
                                    {'regex':r'(http://www.lvping.com/)?(attractions-)+g\d+-\w+\.html$', 'priority':400}, #景点列表
                                    {'regex':r'(http://www.lvping.com/)?(attractions-)+g\d+-[r]+\w+\d+-\w+\.html$', 'priority':450}, #景点列表
                                    
#                                    {'regex':r'(http://www.lvping.com/)?(journals-)+d\d+-s\d+-p\d+-g/\w+\.html$', 'priority':1}, #攻略列表
                                    {'regex':r'(http://www.lvping.com)?(/members/)+(\w/)+journals$', 'priority':700},# 会员游记列表
                                    {'regex':r'(http://www.lvping.com)?/Journals.aspx\?.*selecttype=0.*', 'priority':700},# 游记列表
                                    {'regex':r'(http://www.lvping.com)?/Journals.aspx\?.*selecttype=2.*', 'priority':700},# 攻略列表
                                    {'regex':r'(http://www.lvping.com/)?(travel-)+d\d+-\w+\.html$', 'priority':400},    #常识列表页1
                                    {'regex':r'(http://www.lvping.com/)?(travel-)+d\d+-\w+:brochure\.html#\w+', 'priority':400} #常识列表页2
                                    ],
                     #item页正则表达式 type对应item存放的数据表名
                     'itemRegex':[
                                  {'itemCollectionName':'Note','regex':r'(http://www.lvping.com/)?(travel)+-d\d+-s\w?\d+/\w+:+\w+.*\.html$', 'priority':1000},  #国家介绍 概况、气候等常识
                                  {'itemCollectionName':'Article','regex':r'(http://www.lvping.com/)?(travel-)+d1-+s\d+/\w+:\w+\.html$', 'priority':1000}, #短文攻略(类别 内容 目的地)
                                  {'itemCollectionName':'Article','regex':r'(http://www.lvping.com/)?(showjournal-)+d\d+-r\d+-journals+\.html$', 'priority':1000}, #攻略 作者 发表时间 浏览次数 评论次数
                                  {'itemCollectionName':'Article','regex':r'(http://www.lvping.com/)?journals/AllSingleJournals.aspx\?Writing=\d+$', 'priority':1000}, #第二种攻略游记情况 http://www.lvping.com/journals/AllSingleJournals.aspx?Writing=1322380
                                  {'itemCollectionName':'MemberInfo','regex':r'(http://www.lvping.com/)?(members/)+\w+$', 'priority':1}, #用户
#                                  {'itemCollectionName':'MemberTrack','regex':r'(http://www.lvping.com/)?(members/)+(\w)+(/travelmap-public)+$', 'priority':1}, #足迹
                                  {'itemCollectionName':'MemberFriend','regex':r'(http://www.lvping.com/)?(members/)+(\w)+(/friends)+$', 'priority':1}, #好友
                                  {'itemCollectionName':'MemberNoteList','regex':r'(http://www.lvping.com/)?(members/)+(\w)+(/journals)+$', 'priority':1},  #游记MemberNoteList','regex':r'(http://www.lvping.com/)?(members/)+(\w)+(/journals)+$', 'priority':1},  #游记
                                  
                                  {'itemCollectionName':'Attraction','regex':r'(http://www.lvping.com/)?(attraction_review-)+d\d+-s\d+-[(detail)(attraction)]+\.html$', 'priority':1000}, #景点
                                  {'itemCollectionName':'Region', 'regex':r'(http://www.lvping.com)?(/tourism-)+d\d+-\w+\.html$', 'priority':300}, #城市景区
                                  ],
                     'imageXpath':['//div[@class="yjDetail cf"]//img/@src']
                     },
                "bbsSpider":{
                     'homePage':'http://www.go2eu.com/bbs/', #后面要加 /
                     'allowedDomains':["go2eu.com"],
                     'startUrls':['http://www.19lou.com/forum-1174-filter-type-typeid-566-1.html'],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'forumdisplay.php\?fid=\d+.*page=\d+$|forum-\d+-\d+.html$', 'priority':700},
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
                                  {'itemCollectionName':'Article','regex':r'viewthread.php\?.*tid=\d+.*$|thread-\d+-\d+-\d+.html$'},
                                  ],
                     'firstPageItemRegex':'viewthread.php\?(tid=\d+)?((?!page=).)*$|thread-\d+-1-\d+.html$',
                     'maxPageNumXpath':'//span[@class="threadpages"]/a[last()]/@href',
                     'maxPageNumRegex':None,
                     'pagePattern':{'page=(\d+)':'page=%s', '-(\d)+-':'-%s-'},
                     'itemPriority':1100
                     },


	      "55bbsSpider":{
                     'homePage':'http://bbs.55bbs.com/', #后面要加 /
                     'allowedDomains':["bbs.55bbs.com"],
                     'startUrls':['http://bbs.55bbs.com/forum-34-1.html'],
                     #普通list页正则表达式
                     'normalRegex':[
                                    {'regex':r'forumdisplay.php\?fid=\d+.*page=\d+$|forum-\d+-\d+.html$', 'priority':700},
                                    ],
                     #item页正则表达式 itemCollectionName对应item存放的数据表名
                     'itemRegex':[
                                  {'itemCollectionName':'Article','regex':r'viewthread.php\?.*tid=\d+.*$|thread-\d+-\d+-\d+.html$'},
                                  ],
                     'firstPageItemRegex':'viewthread.php\?(tid=\d+)?((?!page=).)*$|thread-\d+-1-\d+.html$',
                     'maxPageNumXpath':'//span[@class="threadpages"]/a[last()]/@href',
                     'maxPageNumRegex':None,
                     'pagePattern':{'page=(\d+)':'page=%s', '-(\d)+-':'-%s-'},
                     'itemPriority':1100
                     },

}