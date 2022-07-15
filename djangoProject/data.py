from selenium import webdriver
from lxml import etree
import time, sqlite3


def main():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    web = webdriver.Chrome(executable_path='chromedriver')
    url = "https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%e5%a5%b3%e8%a3%85&clk1=8f8360fa53736d8510d09d49b78feecd&upsId=8f8360fa53736d8510d09d49b78feecd"
    web.get(url=url)
    data = web.page_source
    web.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    t = etree.HTML(data)
    time.sleep(10)
    source = t.xpath('//*[@id="mx_5"]/ul/li')

    for i in source:
        price = i.xpath('a/div[2]/span[3]/text()')
        num = i.xpath('a/div[4]/div[2]/text()')
        name = i.xpath('a/div[1]/span/text()')
        print(price[0].split('¥')[1], num[0].split('月销 ')[1].split('+')[0], name[0])
        sql = '''insert into testing_taobao(name,price,num) values ("%s","%0.2f","%d")
        ''' % (name[0], float(price[0].split('¥')[1]), int(num[0].split('月销 ')[1].split('+')[0]))
        data = c.execute(sql)
        print(data)
        conn.commit()
    conn.close()
    web.close()
    web.quit()
