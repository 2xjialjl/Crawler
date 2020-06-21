from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd
import time
import os
def get_data():
    for e in range(1, 6):
        url = "https://www.mobile01.com/topiclist.php?f=400&sort=topictime&p="+str(e)
        r = Request(url)
        r.add_header("user-agent", "Mozilla/5.0")
        response = urlopen(r)
        soup = BeautifulSoup(response)
        find_title = soup.select('div.c-listTableTd__title a.c-link')
        title_list = []
        for i in find_title:
            title_list.append(i.text)
        link_list = []
        for i in find_title:
            link = 'https://www.mobile01.com/'+i.get('href')
            link_list.append(link)
        date_list1 = []
        find_date = soup.select('div.o-fNotes')
        for i in find_date:
            date_list1.append(i.text)
        dataframe1 = pd.DataFrame({'date': date_list1})
        dataframe1.to_excel('D:\網路聲量分析\data\\mobile01\\trash\\date'+str(e)+'.xlsx',index=False)
        df = pd.read_excel('D:\網路聲量分析\data\\mobile01\\trash\\date'+str(e)+'.xlsx')
        date_list = []
        for i in range(0, 60, 2):
            date = df['date'][i]
            date_list.append(date)
        dataframe2 = pd.DataFrame({'date': date_list, 'title': title_list, 'link': link_list})
        dataframe2.to_excel('D:\網路聲量分析\data\\mobile01\\trash\\'+str(e)+'.xlsx', index=False)
get_data()
def mix_all():
    df = pd.read_excel('D:\網路聲量分析\data\\mobile01\\trash\\1.xlsx')
    df1 = pd.read_excel('D:\網路聲量分析\data\\mobile01\\trash\\2.xlsx')
    df2 = pd.read_excel('D:\網路聲量分析\data\\mobile01\\trash\\3.xlsx')
    df3 = pd.read_excel('D:\網路聲量分析\data\\mobile01\\trash\\4.xlsx')
    df4 = pd.read_excel('D:\網路聲量分析\data\\mobile01\\trash\\5.xlsx')
    mix = pd.concat([df, df1, df2, df3, df4])
    mix.to_excel('D:\網路聲量分析\data\\mobile01\\rowdata.xlsx', index=False)
mix_all()
def chose_data():
    df = pd.read_excel('D:\網路聲量分析\data\\mobile01\\rowdata.xlsx')
    year = str(time.strftime("%Y", time.localtime()))
    month = str(time.strftime("%m", time.localtime()))
    day = year + '-' + month
    ch = df.loc[df['date'].str.contains(day)]
    ch.to_excel('D:\網路聲量分析\data\\mobile01\\this_month.xlsx', index=False)
chose_data()
def get_all():
    df = pd.read_excel('D:\網路聲量分析\data\\mobile01\\this_month.xlsx')
    df_count = len(df.index)
    for j in range(df_count):
        url = df['link'][j]
        r = Request(url)
        r.add_header("user-agent", "Mozilla/5.0")
        response = urlopen(r)
        soup = BeautifulSoup(response)
        find_all = soup.select('div.u-gapNextV--md')
        all_list = []
        for i in find_all:
            all_list.append(i.text)
        place_list = ['mobile01_居家房事']
        date = df['date'][j]
        title = df['title'][j]
        link = df['link'][j]
        c = ['source', 'date', 'title', 'all', 'link']
        ds = pd.DataFrame(columns=c)
        s = pd.Series([place_list, date, title, all_list, link], index=c)
        ds = ds.append(s, ignore_index=True)
        ds.to_excel('D:\網路聲量分析\data\\mobile01\\tra\\' + str(j) + '.xlsx', index=False)
get_all()
def mix_al():
    ds = pd.read_excel('D:\網路聲量分析\data\\mobile01\\this_month.xlsx')
    df_count = len(ds.index)
    dfs = []
    for i in range(df_count):
        dfs.append(pd.read_excel('D:/網路聲量分析/data/mobile01/tra//' + str(i)+'.xlsx'))
    try:
        df_spc = pd.concat(dfs)
        df_spc.to_excel('D:/網路聲量分析/data/mobile01/result.xlsx', index=False)
    except:
        a = []
        b = []
        c = []
        d = []
        e = []
        df_save = pd.DataFrame({'source': a, 'date': b, 'title': c, 'all': d, 'link': e})
        df_save.to_excel('D:/網路聲量分析/data/mobile01/result.xlsx', index=False)
    # path = 'D:\網路聲量分析\data\\mobile01\\tra'
    # files = os.listdir(path)
    # dfs = []
    # for i in files:
    #     dfs.append(pd.read_excel('D:/網路聲量分析/data/mobile01/tra//' + str(i)))
    # df = pd.concat(dfs)
    # df.to_excel('D:/網路聲量分析/data/mobile01/result.xlsx', index=False)
mix_al()
def key_word():
    df = pd.read_excel('D:/網路聲量分析/data/mobile01/result.xlsx')
    hoho = df.loc[df['all'].str.contains('hoho')]
    jacker = df.loc[df['all'].str.contains('潔客幫')]
    spc = df.loc[df['all'].str.contains('特力屋好幫手')]
    hoho.to_excel('D:/網路聲量分析/data/mobile01/hoho.xlsx', index=False)
    jacker.to_excel('D:/網路聲量分析/data/mobile01/jacker.xlsx', index=False)
    spc.to_excel('D:/網路聲量分析/data/mobile01/spc.xlsx', index=False)
    print('======hoho======')
    print(hoho)
    print('======jacker======')
    print(jacker)
    print('======spc======')
    print(spc)
key_word()