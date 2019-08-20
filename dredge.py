import urllib
import urllib.request as urllib2 
import random
import zlib
import re

#---------------------------------------------------------
#中文汉字转阿拉伯数字
common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, 
                            '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,'十': 10, 
                            '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
    common_used_numerals[key] = common_used_numerals_tmp[key]
 
 
def chinese2digits(uchars_chinese):
    total = 0
    r = 1  # 表示单位：个十百千...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals.get(uchars_chinese[i])
        if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val
    return total
 
 
num_str_start_symbol = ['一', '二', '两', '三', '四', '五', '六', '七', '八', '九','十']
more_num_str_symbol = ['零', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '亿']
 
def changeChineseNumToArab(oriStr):
    lenStr = len(oriStr)
    aProStr = ''
    if lenStr == 0:
        return aProStr
 
    hasNumStart = False
    numberStr = ''
    for idx in range(lenStr):
        if oriStr[idx] in num_str_start_symbol:
            if not hasNumStart:
                hasNumStart = True
 
            numberStr += oriStr[idx]
        else:
            if hasNumStart:
                if oriStr[idx] in more_num_str_symbol:
                    numberStr += oriStr[idx]
                    continue
                else:
                    numResult = str(chinese2digits(numberStr))
                    numberStr = ''
                    hasNumStart = False
                    aProStr += numResult 
            aProStr += oriStr[idx]
            pass 
    if len(numberStr) > 0:
        resultNum = chinese2digits(numberStr)
        aProStr += str(resultNum) 
    return aProStr
#---------------------------------------------------------
def getLastContent(cUrl):
    #防止被网站封了，用多种类型的浏览器
    user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ',
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    ]
    #随机选择一个
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent , 'Accept-Encoding': 'gzip, deflate'}

    #要爬的内容
    url = cUrl

    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    html = zlib.decompress(content, 16+zlib.MAX_WBITS)#解压网页
    html = html.decode("utf-8")
    #pattern = re.compile('<span class="last">.*?最新章节.*?</span>',re.S)
    pattern = re.compile('<div id="content" class="showtxt">(.*?)</div>',re.S)
    items = re.findall(pattern,html)
    import html
    # item = html.escape(items[0])
    return items[0]



#---------------------------------------------------------
def getLastDocument():
    #防止被网站封了，用多种类型的浏览器
    user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ',
    'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    ]
    #随机选择一个
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent , 'Accept-Encoding': 'gzip, deflate'}

    #要爬的内容
    url = 'http://www.shuquge.com/txt/8400/index.html'

    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()
    html = zlib.decompress(content, 16+zlib.MAX_WBITS)#解压网页
    html = html.decode("utf-8")
    #pattern = re.compile('<span class="last">.*?最新章节.*?</span>',re.S)
    pattern = re.compile('<span class="last">更新时间：(.*?)</span>.*?<span class="last">最新章节：<a href="(.*?)">第(.*?)章 (.*?)</a></span>',re.S)
    items = re.findall(pattern,html)

    statusCode = "202"
    item = items[0]
    redic = {
        "statuscode" : statusCode,
        "message" : "m",
        "data": {
            "releaseTime" : item[0],
            "chapterCN" : item[2],
            "chapterArab" : changeChineseNumToArab(item[2]),
            "URL" : item[1],
            "title" : item[3],
            "content" : getLastContent(item[1])
        }
    }    
    #tstr = u"第%s章(%s):%s\t发布时间:%s\t%s" %(item[2],changeChineseNumToArab(item[2]),item[3],item[0],item[1])
    return redic

# redic = getLastDocument()
# rint(redic)



