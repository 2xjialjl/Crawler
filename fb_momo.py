from selenium import webdriver
import time
import pyautogui
from bs4 import BeautifulSoup
import pandas as pd
import datetime
def get_data():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
    driver.get("https://www.facebook.com/pg/momotvshopping/posts/")
    for j in range(2):
        time.sleep(0.5)
        pyautogui.press('pgdn')
    time.sleep(2)
    driver.find_element_by_id('expanding_cta_close_button').click()
    for j in range(120):
        time.sleep(0.5)
        pyautogui.press('pgdn')
    soup = BeautifulSoup(driver.page_source)
    posts = soup.find_all('div', class_='clearfix y_c3pyo2ta3')
    link_list = []
    for i in posts:
        link_list.append('https://www.facebook.com' + i.find('a', {'class': '_5pcq'}).attrs['href'].split('?', 2)[0])
    dataframe1 = pd.DataFrame({'link': link_list})
    dataframe1.to_excel('D:\網路聲量分析\data\\fb_momo\link.xlsx', index=False)
    driver.close()
get_data()
def clean_link():
    df = pd.read_excel('D:\網路聲量分析\data\\fb_momo\link.xlsx')
    drop_word = df.loc[~df['link'].str.contains('%E5%BE%97%E7%8D%8E%E5%85%AC%E4%BD%88')]
    drop_word.to_excel('D:\網路聲量分析\data\\fb_momo\link.xlsx', index=False)
clean_link()
def get_all():
    df = pd.read_excel('D:\網路聲量分析\data\\fb_momo\link.xlsx')
    df_count = len(df.index)
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
    for i in range(df_count):
        url = df['link'][i]
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source)
        find_date = soup.find_all('span', class_='fsm fwn fcg')
        date_list = []
        for e in find_date:
            da = e.find('abbr')
            date = da.get('title')[:10]
            date_list.append(date)
        find_all = soup.find_all('div', class_='_5pbx userContent _3576')
        all_list = []
        for j in find_all:
            all_list.append(j.text)
        link = df['link'][i]
        source = 'fb_momo購物'
        dataframe1 = pd.DataFrame({'source': source, 'date': date_list[0], 'title': all_list, 'all': all_list, 'link': link})
        dataframe1.to_excel('D:\網路聲量分析\data\\fb_momo\\trash\\'+str(i)+'.xlsx', index=False)
get_all()
def mix_all():
    ds = pd.read_excel('D:\網路聲量分析\data\\fb_momo\link.xlsx')
    df_count = len(ds.index)
    dfs = []
    for i in range(df_count):
        dfs.append(pd.read_excel('D:\網路聲量分析\data\\fb_momo\\trash\\'+str(i)+'.xlsx'))
        df = pd.concat(dfs)
    df.to_excel('D:\網路聲量分析\data\\fb_momo\\result.xlsx', index=False)
mix_all()
def chose_time():
    df = pd.read_excel('D:\網路聲量分析\data\\fb_momo\\result.xlsx')
    year = str(time.strftime("%Y", time.localtime()))
    month = str(datetime.date.today().month)
    day = year+'年'+month+'月'
    ch = df.loc[df['date'].str.contains(day)]
    ch.to_excel('D:\網路聲量分析\data\\fb_momo\\result.xlsx', index=False)
chose_time()
def key_word():
    df = pd.read_excel('D:\網路聲量分析\data\\fb_momo\\result.xlsx')
    hoho = df.loc[df['all'].str.contains('')]# 想找的關鍵字
    jacker = df.loc[df['all'].str.contains('')]# 想找的關鍵字
    spc = df.loc[df['all'].str.contains('')]# 想找的關鍵字
    hoho.to_excel('D:\網路聲量分析\data\\fb_momo\\hoho.xlsx', index=False)
    jacker.to_excel('D:\網路聲量分析\data\\fb_momo\\jacler.xlsx', index=False)
    spc.to_excel('D:\網路聲量分析\data\\fb_momo\\spc.xlsx', index=False)
    print('============')
    print(hoho)
    print('============')
    print(jacker)
    print('============')
    print(spc)
key_word()