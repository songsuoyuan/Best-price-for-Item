# Set up cookies and headers for HttpRequests.

# Author:		obliv[io]us
# Created:		20 June 2017
# Version:		1.0

# Change the cookies_xxxxx_str accordingly. 
# Press F12 in Chrome to get the cookie string.

# Dotamax
cookies_dotamax_str = '__cfduid=d3586e69e11bffd52e84bb4ccd7755f481496802874; csrftoken=LsM6zjRIDdx1Rs8Yw8LRu0mJhvHpcAVl; pkey=MTQ5NzMzNDUyOC41OW9ibGl2aW91c18yc3Zrc3lrZHVsc3h1cHB2bw____; _ga=GA1.2.47418504.1484560971; _gid=GA1.2.675387774.1497155838; _gat=1; cookie="gAJ9cQFVD2RqYW5nb190aW1lem9uZVUOQXNpYS9Ib25nX0tvbmdzLg:1dKfDp:hxEktCTxF9BNhyDPTzTcukYz5Pk"; Hm_lvt_575895fe09d48554a608faa5ef059555=1495544581,1497188172; Hm_lpvt_575895fe09d48554a608faa5ef059555=1497335194'
headers_dotamax = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.dotamax.com',
    'Referer':'http://www.dotamax.com/bets/index/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

# Dota188
# for future development
cookies_dota188_str = 'DJSP_UUID=159a6be8b0c3fe1f2d885b77; Hm_lvt_b98e37a9ca5149b7006d81d8272ab72c=1494400581,1496034032; _ga=GA1.2.236165336.1488250420; DJSP_USER=5FKPbO9h3ssv9%2BTC1SrpVXEUvr2oTb2pIBvMRaxk5TWkpi4z1RyyvxfwEd0E20maw0HdYYeEltsndlNZgu6N7S0vCfjTnvwYdx%2Fz1QL0Fg9hu26NSec9ZpuoFcYtabRo; aliyungf_tc=AQAAANaAYwke0w0AjhRZjyvNYXocMuqL; JSESSIONID=1683E83E4F1FC4F7F1487CEBA52A9033; Hm_lvt_ff262caaed5bb7cfac5248071122e9ed=1494736519,1495544586,1495702973,1497188166; Hm_lpvt_ff262caaed5bb7cfac5248071122e9ed=1497253192; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; SYSTEM_STYLE=gray'
headers_dota188 = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
    'Connection':'keep-alive',
    'Content-Length':'0',
    'Host':'www.dota188.com',
    'Origin':'http://www.dota188.com',
    'Referer':'http://www.dota188.com/user/bag/edit.do',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
    }

# C5GAME
cookies_c5game_str = 'C5Machines=HXjF%2BIxezs9xXFnlgmX2LA%3D%3D; C5Appid=570; C5Lang=zh; C5SessionID=leq1jmgsif0oojrav5fifipcn0; C5Sate=80ad38f9f9680ae76b13e2fbd7e65147202bc510a%3A4%3A%7Bi%3A0%3Bs%3A7%3A%222849904%22%3Bi%3A1%3Bs%3A15%3A%22steam_139045316%22%3Bi%3A2%3Bi%3A259200%3Bi%3A3%3Ba%3A0%3A%7B%7D%7D; C5Token=593f83fbe5db4; C5Login=2849904; Hm_lvt_86084b1bece3626cd94deede7ecf31a8=1495514563,1495642224,1497188061; Hm_lpvt_86084b1bece3626cd94deede7ecf31a8=1497335628'
headers_c5game = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
    'Connection':'keep-alive',
    'Host':'www.c5game.com',
    'Referer':'https://www.c5game.com/dota.html?quality=&hero=&type=',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

# IGXE
cookies_igxe_str = '__cfduid=d8b057d45fc899191d106f70da38cc9ff1482458512; _qddaz=QD.8dfysz.ml4jin.ix1iazo1; looyu_id=e547dcb1d44fc2b9a1c94b52064ff7f00d_35810%3A4; c_is_menu_old=2; aliyungf_tc=AQAAALKC0DBS+gQAwNv2d3YHsJT/hdz9; csrftoken=dWOVJd5vAoXNQtIU4Hye2CZh2stxAb5O; _ga=GA1.2.1091404023.1482458513; _gid=GA1.2.277971558.1497257650; Hm_lvt_fe0238ac0617c14d9763a2776288b64b=1497060321,1497065089,1497092678,1497257651; Hm_lpvt_fe0238ac0617c14d9763a2776288b64b=1497260582; sessionid=5abg2nd7zzh6ymnqjos3apa79r8p6jfc'
headers_igxe = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,es;q=0.2',
    'Connection':'keep-alive',
    'Host':'www.igxe.cn',
    'Referer':'http://www.igxe.cn/inventory/igxe/570',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

# Parse the cookies string
# Dotamax
cookies_dotamax_list = cookies_dotamax_str.split('; ')
cookies_dotamax = dict([p.split('=') for p in cookies_dotamax_list])
# Dota188
cookies_dota188_list = cookies_dota188_str.split('; ')
cookies_dota188 = dict([p.split('=') for p in cookies_dota188_list])
# C5GAME
cookies_c5game_list = cookies_c5game_str.split('; ')
cookies_c5game = dict([p.split('=') for p in cookies_c5game_list])
# IGXE
cookies_igxe_list = cookies_igxe_str.split('; ')
cookies_igxe = dict([p.split('=') for p in cookies_igxe_list])

# Write the cookies and headers into dictionary
cookies_and_headers = {
    'dotamax':{
        'cookies':cookies_dotamax,
        'headers':headers_dotamax
    },
    'dota188':{
        'cookies':cookies_dota188,
        'headers':headers_dota188
    },
    'c5game':{
        'cookies':cookies_c5game,
        'headers':headers_c5game
    },
    'igxe':{
        'cookies':cookies_igxe,
        'headers':headers_igxe
    },
}