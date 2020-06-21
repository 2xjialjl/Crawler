from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from selenium import webdriver
import pyautogui
import requests
import datetime
#  jacker
def get_data_jacker():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    # chromeOptions.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
    driver.get('https://www.pixnet.net/tags/%E6%BD%94%E5%AE%A2%E5%B9%AB?filter=articles&sort=related')
    time.sleep(3)
    for j in range(15):
        time.sleep(0.5)
        pyautogui.press('pgdn') # 按 PgDn
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    find_date = soup.find_all('p', class_='sc-15yfh73-8 fQudZ')
    date_list = []
    for h in find_date:
        date_list.append(h.text)
    find_title = soup.find_all('h2', class_='sc-1hu2j4t-2 fCYIqq')
    title_list = []
    for m in find_title:
        title_list.append(m.text)
    find_link = soup.find_all('section')
    clean_link_list = []
    for w in find_link:
        clean_link = str(w.get('data-gtm-label'))
        link = clean_link.replace('None', '')
        clean_link_list.append(link)
    dataframe1 = pd.DataFrame({'link': clean_link_list})
    dataframe1.to_excel('D:\網路聲量分析\data\pixnet\\jacker\\tra\clean_link.xlsx', index=False)
    df = pd.read_excel('D:\網路聲量分析\data\pixnet\\jacker\\tra\clean_link.xlsx')
    df.dropna(inplace=True)
    df.to_excel('D:\網路聲量分析\data\pixnet\\jacker\\tra\clean_link.xlsx', index=False)
    dc = pd.read_excel('D:\網路聲量分析\data\pixnet\\jacker\\tra\clean_link.xlsx')
    li = dc['link']
    link_list = []
    for c in li:
        link_list.append(c)
    dataframe2 = pd.DataFrame({'date': date_list, 'title': title_list, 'link': link_list})
    dataframe2.to_excel('D:\網路聲量分析\data\pixnet\\jacker\\trash\\rowdata.xlsx', index=False)
    driver.close()
get_data_jacker()
def chose_time_jacker():
    df = pd.read_excel('D:\網路聲量分析\data\pixnet\\jacker\\trash\\rowdata.xlsx')
    year = str(time.strftime("%Y", time.localtime()))
    year_1 = str(int(year)-1)
    year_2 = str(int(year)-2)
    df = df[~df['date'].str.contains(year_2)]
    df = df[~df['date'].str.contains(year_1)]
    month = str(datetime.date.today().month)
    day = month+'月'
    ch = df.loc[df['date'].str.contains(day)]
    ch.to_excel('D:\網路聲量分析\data\\pixnet\\jacker\\this_month.xlsx', index=False)
chose_time_jacker()
def get_all_jacker():
    df = pd.read_excel('D:\網路聲量分析\data\\pixnet\\jacker\\this_month.xlsx')
    df_count = len(df.index)
    for j in range(df_count):
        url = df['link'][j]
        r = requests.get(url)
        r.encoding = 'zh-TW'
        soup = BeautifulSoup(r.text, "html.parser")
        find_all = soup.select('div.article-content')
        all_list = []
        for i in find_all:
            all_list.append(i.text.replace('\n', '').replace('\xa0', '').replace('\x08', ''))
            print(all_list)
        place_list = ['痞客邦']
        date_list = df['date'][j]
        title_list = df['title'][j]
        link_list = df['link'][j]
        dataframe = pd.DataFrame({'source': place_list, 'date': date_list, 'title': title_list, 'all': all_list, 'link': link_list})
        dataframe.to_excel('D:\網路聲量分析\data\\pixnet\\jacker\\tr\\date'+str(j)+'.xlsx', index=False)
get_all_jacker()
def mix_al_jacker():
    ds = pd.read_excel('D:\網路聲量分析\data\\pixnet\\jacker\\this_month.xlsx')
    df_count = len(ds.index)
    dfs = []
    for i in range(df_count):
        dfs.append(pd.read_excel('D:/網路聲量分析/data/pixnet/jacker/tr//' + str(i) + '.xlsx'))
    try:
        df = pd.concat(dfs)
        df.to_excel('D:/網路聲量分析/data/pixnet/jacker/jacker.xlsx', index=False)
    except:
        a = []
        b = []
        c = []
        d = []
        e = []
        df_hoho = pd.DataFrame({'source': a, 'date': b, 'title': c, 'all': d, 'link': e})
        df_hoho.to_excel('D:/網路聲量分析/data/pixnet/jacker/jacker.xlsx', index=False)
mix_al_jacker()

#  hoho
def get_data_hoho():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    # chromeOptions.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
    driver.get('https://www.pixnet.net/tags/hoho')
    time.sleep(1)
    for j in range(10):
        time.sleep(0.5)
        pyautogui.press('pgdn') # 按 PgDn
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    find_date = soup.find_all('p', class_='sc-15yfh73-8 fQudZ')
    date_list = []
    for h in find_date:
        date_list.append(h.text)
    find_title = soup.find_all('h2', class_='sc-1hu2j4t-2 fCYIqq')
    title_list = []
    for m in find_title:
        title_list.append(m.text)
    find_link = soup.find_all('section')
    clean_link_list = []
    for w in find_link:
        clean_link = str(w.get('data-gtm-label'))
        link = clean_link.replace('None', '')
        clean_link_list.append(link)
    dataframe1 = pd.DataFrame({'link': clean_link_list})
    dataframe1.to_excel('D:\網路聲量分析\data\pixnet\\hoho\\tra\clean_link.xlsx', index=False)
    df = pd.read_excel('D:\網路聲量分析\data\pixnet\\hoho\\tra\clean_link.xlsx')
    df.dropna(inplace=True)
    df.to_excel('D:\網路聲量分析\data\pixnet\\hoho\\tra\clean_link.xlsx', index=False)
    dc = pd.read_excel('D:\網路聲量分析\data\pixnet\\hoho\\tra\clean_link.xlsx')
    li = dc['link']
    link_list = []
    for c in li:
        link_list.append(c)
    dataframe2 = pd.DataFrame({'date': date_list, 'title': title_list, 'link': link_list})
    dataframe2.to_excel('D:\網路聲量分析\data\pixnet\\hoho\\trash\\rowdata.xlsx', index=False)
    driver.close()
get_data_hoho()
def chose_time_hoho():
    df = pd.read_excel('D:\網路聲量分析\data\pixnet\\hoho\\trash\\rowdata.xlsx')
    year = str(time.strftime("%Y", time.localtime()))
    year_1 = str(int(year)-1)
    year_2 = str(int(year)-2)
    year_3 = str(int(year)-3)
    year_4 = str(int(year)-4)
    year_5 = str(int(year)-5)
    df = df[~df['date'].str.contains(year_5)]
    df = df[~df['date'].str.contains(year_4)]
    df = df[~df['date'].str.contains(year_3)]
    df = df[~df['date'].str.contains(year_2)]
    df = df[~df['date'].str.contains(year_1)]
    month = str(datetime.date.today().month)
    day = month+'月'
    ch = df.loc[df['date'].str.contains(day)]
    ch.to_excel('D:\網路聲量分析\data\\pixnet\\hoho\\this_month.xlsx', index=False)
chose_time_hoho()
def get_all_hoho():
    df = pd.read_excel('D:\網路聲量分析\data\\pixnet\\hoho\\this_month.xlsx')
    df_count = len(df.index)
    for j in range(df_count):
        url = df['link'][j]
        r = requests.get(url)
        r.encoding = 'zh-TW'
        soup = BeautifulSoup(r.text, "html.parser")
        find_all = soup.select('div.article-content')
        all_list = []
        for i in find_all:
            all_list.append(i.text.replace('\n', '').replace('\xa0', '').replace('\x08', ''))
            print(all_list)
        place_list = ['痞客邦']
        date_list = df['date'][j]
        title_list = df['title'][j]
        link_list = df['link'][j]
        dataframe = pd.DataFrame({'source': place_list, 'date': date_list, 'title': title_list, 'all': all_list, 'link': link_list})
        dataframe.to_excel('D:\網路聲量分析\data\\pixnet\\hoho\\tr\\date'+str(j)+'.xlsx', index=False)
get_all_hoho()
def mix_al_hoho():
    ds = pd.read_excel('D:\網路聲量分析\data\\pixnet\\hoho\\this_month.xlsx')
    df_count = len(ds.index)
    dfs = []
    for i in range(df_count):
        dfs.append(pd.read_excel('D:/網路聲量分析/data/pixnet/hoho/tr//' + str(i) + '.xlsx'))
    try:
        df = pd.concat(dfs)
        df.to_excel('D:/網路聲量分析/data/pixnet/hoho/hoho.xlsx', index=False)
    except:
        a = []
        b = []
        c = []
        d = []
        e = []
        df_hoho = pd.DataFrame({'source': a, 'date': b, 'title': c, 'all': d, 'link': e})
        df_hoho.to_excel('D:/網路聲量分析/data/pixnet/hoho/hoho.xlsx', index=False)
mix_al_hoho()

#  spc
def get_data_spc():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    # chromeOptions.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
    driver.get('https://www.pixnet.net/tags/%E7%89%B9%E5%8A%9B%E5%B1%8B%E5%A5%BD%E5%B9%AB%E6%89%8B')
    time.sleep(1)
    for j in range(10):
        time.sleep(0.5)
        pyautogui.press('pgdn') # 按 PgDn
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    find_date = soup.find_all('p', class_='sc-15yfh73-8 fQudZ')
    date_list = []
    for h in find_date:
        date_list.append(h.text)
    find_title = soup.find_all('h2', class_='sc-1hu2j4t-2 fCYIqq')
    title_list = []
    for m in find_title:
        title_list.append(m.text)
    find_link = soup.find_all('section')
    clean_link_list = []
    for w in find_link:
        clean_link = str(w.get('data-gtm-label'))
        link = clean_link.replace('None', '')
        clean_link_list.append(link)
    dataframe1 = pd.DataFrame({'link': clean_link_list})
    dataframe1.to_excel('D:\網路聲量分析\data\pixnet\\spc\\tra\clean_link.xlsx', index=False)
    df = pd.read_excel('D:\網路聲量分析\data\pixnet\\spc\\tra\clean_link.xlsx')
    df.dropna(inplace=True)
    df.to_excel('D:\網路聲量分析\data\pixnet\\spc\\tra\clean_link.xlsx', index=False)
    dc = pd.read_excel('D:\網路聲量分析\data\pixnet\\spc\\tra\clean_link.xlsx')
    li = dc['link']
    link_list = []
    for c in li:
        link_list.append(c)
    dataframe2 = pd.DataFrame({'date': date_list, 'title': title_list, 'link': link_list})
    dataframe2.to_excel('D:\網路聲量分析\data\pixnet\\spc\\trash\\rowdata.xlsx', index=False)
    driver.close()
get_data_spc()
def chose_time_spc():
    df = pd.read_excel('D:\網路聲量分析\data\pixnet\\spc\\trash\\rowdata.xlsx')
    year = str(time.strftime("%Y", time.localtime()))
    year_1 = str(int(year)-1)
    year_2 = str(int(year)-2)
    year_3 = str(int(year)-3)
    year_4 = str(int(year)-4)
    year_5 = str(int(year)-5)
    df = df[~df['date'].str.contains(year_5)]
    df = df[~df['date'].str.contains(year_4)]
    df = df[~df['date'].str.contains(year_3)]
    df = df[~df['date'].str.contains(year_2)]
    df = df[~df['date'].str.contains(year_1)]
    month = str(datetime.date.today().month)
    day = month+'月'
    ch = df.loc[df['date'].str.contains(day)]
    ch.to_excel('D:\網路聲量分析\data\\pixnet\\spc\\this_month.xlsx', index=False)
chose_time_spc()
def get_all_spc():
    df = pd.read_excel('D:\網路聲量分析\data\\pixnet\\spc\\this_month.xlsx')
    df_count = len(df.index)
    for j in range(df_count):
        url = df['link'][j]
        r = requests.get(url)
        r.encoding = 'zh-TW'
        soup = BeautifulSoup(r.text, "html.parser")
        find_all = soup.select('div.article-content')
        all_list = []
        for i in find_all:
            all_list.append(i.text.replace('\n', '').replace('\xa0', '').replace('\x08', ''))
            print(all_list)
        place_list = ['痞客邦']
        date_list = df['date'][j]
        title_list = df['title'][j]
        link_list = df['link'][j]
        dataframe = pd.DataFrame({'source': place_list, 'date': date_list, 'title': title_list, 'all': all_list, 'link': link_list})
        dataframe.to_excel('D:\網路聲量分析\data\\pixnet\\spc\\tr\\date'+str(j)+'.xlsx', index=False)
get_all_spc()
def mix_al_spc():
    ds = pd.read_excel('D:\網路聲量分析\data\\pixnet\\spc\\this_month.xlsx')
    df_count = len(ds.index)
    dfs = []
    for i in range(df_count):
        dfs.append(pd.read_excel('D:/網路聲量分析/data/pixnet/spc/tr//' + str(i) + '.xlsx'))
    try:
        df = pd.concat(dfs)
        df.to_excel('D:/網路聲量分析/data/pixnet/spc/spc.xlsx', index=False)
    except:
        a = []
        b = []
        c = []
        d = []
        e = []
        df_hoho = pd.DataFrame({'source': a, 'date': b, 'title': c, 'all': d, 'link': e})
        df_hoho.to_excel('D:/網路聲量分析/data/pixnet/spc/spc.xlsx', index=False)
mix_al_spc()


def key_word():
    df_spc = pd.read_excel('D:/網路聲量分析/data/pixnet/spc/spc.xlsx')
    df_hoho = pd.read_excel('D:/網路聲量分析/data/pixnet/hoho/hoho.xlsx')
    df_jacker = pd.read_excel('D:/網路聲量分析/data/pixnet/jacker/jacker.xlsx')
    spc = df_spc.loc[df_spc['all'].str.contains('')]# 想找的關鍵字
    hoho = df_hoho.loc[df_hoho['all'].str.contains('')]# 想找的關鍵字
    jacker = df_jacker[df_jacker['all'].str.contains('')]# 想找的關鍵字
    spc.to_excel('D:/網路聲量分析/data/pixnet/spc.xlsx', index=False)
    hoho.to_excel('D:/網路聲量分析/data/pixnet/hoho.xlsx', index=False)
    jacker.to_excel('D:/網路聲量分析/data/pixnet/jacker.xlsx', index=False)
key_word()
