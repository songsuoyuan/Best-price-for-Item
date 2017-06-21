# -*- coding=utf-8 -*-

try:
    import csv
    import time
    import random
    import requests
    import warnings
    from bs4 import BeautifulSoup
except ImportError:
    print 'One or more modules can not be imported! Check FAQ in README.md for solutions.'

# Close all warnings
warnings.filterwarnings('ignore')

# Get cookies and headers
from config_headers import cookies_and_headers

# Get price limits
from price_limits import csgo_dotamax_limit

# Map exterior to exterior_id
exterior_show_dict = {u'(久经沙场)':601, u'(破损不堪)':595, u'(略有磨损)':615, u'(战痕累累)':609, u'(崭新出厂)':589, u'(无涂装)':728}

def unicode_csv_reader(utf_8_csv_data):
    '''
    Read utf-8 csv file and return unicode data
    '''
    csv_reader = csv.reader(utf_8_csv_data)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

def best_price_from_igxe():
    with open('data/csgo_price.csv', 'rb') as csv_file:
        reader = unicode_csv_reader(csv_file)
        csgo_price = dict(reader) 
    # IGXE entry
    igxe_url = 'http://www.igxe.cn/csgo/search/0_0'
    # IGXE parameters for csgo items
    igxe_params = {
        'search_page_no':1,
        'search_relate_price':'',
        'search_is_sticker':0,
        'search_price_gte':'',
        'search_price_lte':'',
        'search_rarity_id':'',
        'search_exterior_id':'',
        'search_is_stattrak':0,
        'search_sort_key':2,
        'search_sort_rule':0
        }
    total_success = 0
    for k, v in csgo_price.items():
        v = float(v)
        this_igxe_params = igxe_params  
        time.sleep(2*random.random())
        for ek in exterior_show_dict.keys():
            if ek in k:
                name = k.replace(ek, '')
                this_igxe_params['search_exterior_id'] = exterior_show_dict[ek]
                this_igxe_params['keyword'] = name
                try:
                    igxe_headers = cookies_and_headers['igxe']['headers']
                    igxe_cookies = cookies_and_headers['igxe']['cookies']
                    r = requests.get(igxe_url, params=this_igxe_params, headers=igxe_headers, cookies=igxe_cookies, timeout=5, verify=False)
                except:
                    print 'Error when fetch {0} with price {1}, skip...'.format(k.encode('gb2312'), csgo_price[k])
                    time.sleep(10*random.random())
                    continue
                soup = BeautifulSoup(r.text, 'html.parser')
                item = soup.find('div', {'class':'mod-hotEquipment-bd'})
                if item:
                    first_price = float(item.find('div', {'class':'s3'}).span.strong.text)
                    total_success = total_success + 1
                    for indx in range(len(csgo_dotamax_limit[0])):
                        if v > csgo_dotamax_limit[0][indx] and first_price / v < csgo_dotamax_limit[1][indx]:
                            print k.encode('gb2312'), v, first_price, 'dotamax ratio:', first_price / v
                        break
                break
    print 'total items:', len(csgo_price), '; total success:', total_success, '; percentage: ', 1.*(len(csgo_price)-total_success)/len(csgo_price)	

if __name__ == "__main__":
    best_price_from_igxe()
