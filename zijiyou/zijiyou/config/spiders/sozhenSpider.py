# -*- coding: utf-8 -*-
sozhenSpider={
        'allowedDomains':["sozhen.com"],
        'startUrls':[
                     'http://www.sozhen.com/default/newsarticle.html', #古镇新闻
                     'http://www.sozhen.com/default/townarticle_2.html',
                     'http://www.sozhen.com/default/townarticle_3.html',
                     'http://www.sozhen.com/default/townarticle_6.html',
                     'http://www.sozhen.com/default/townarticle_24.html',
                     'http://www.sozhen.com/default/townarticle_43.html',
                     'http://www.sozhen.com/default/townarticle_45.html',
                     'http://www.sozhen.com/default/townarticle_46.html',
                     'http://www.sozhen.com/default/townarticle_47.html',
                     'http://www.sozhen.com/default/townarticle_48.html',
                     'http://www.sozhen.com/default/townarticle_51.html',
                     'http://www.sozhen.com/default/townarticle_52.html',
                     'http://www.sozhen.com/default/townarticle_53.html',
                     'http://www.sozhen.com/default/townarticle_54.html',
                     'http://www.sozhen.com/default/townarticle_55.html',
                     'http://www.sozhen.com/default/townarticle_56.html',
                     'http://www.sozhen.com/default/townarticle_57.html',
                     'http://www.sozhen.com/default/townarticle_58.html',
                     'http://www.sozhen.com/default/townarticle_59.html',
                     'http://www.sozhen.com/default/townarticle_60.html',
                     'http://www.sozhen.com/default/townarticle_61.html',
                     'http://www.sozhen.com/default/townarticle_88.html',
                     'http://www.sozhen.com/default/townarticle_89.html',
                     'http://www.sozhen.com/default/townarticle_98.html',
                     'http://www.sozhen.com/default/townarticle_155.html',
                     ],
        #普通list页正则表达式
        'normalRegex':[
                       #古镇攻略下一页
                       {
                        'regex':r'townarticle.*html',
                        'region':r'//div[2]/div[2]/div[2]/div[2]/div[37]/div',
                        'priority':1000
                       },
                       {
                       #古镇新闻列表：分页，如：http://www.sozhen.com/default/newsarticle_0_10.html
                        'regex':r'^newsarticle_0_\d+\.html$',
                        'priority':1000
                        },
                       {
                       #某个客栈游记攻略列表（含分页），如：
                        'regex':r'^/default/towninn_\d+(_\d+)?\.html$',
                        'priority':1000
                        },
                       ],
        #item页正则表达式 itemCollectionName对应item存放的数据表名
        'itemRegex':[
                     #Article
                     {
                      #文章内容，如：http://www.sozhen.com/default/townarticlecon_12_52358.html
                      'itemCollectionName':'Article',
                      'region':'//div[2]/div[2]/div[2]/div[2]',
                      'regex':r'/default/\w+con_\d+_\d+\.html$',
                      'priority':600
                      },  
                     ]
                    }