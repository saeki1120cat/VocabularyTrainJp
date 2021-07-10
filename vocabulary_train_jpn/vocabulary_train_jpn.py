import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def train_jpy(keyword_str):
    global ans
    url = 'https://dict.asia/jc/' + keyword_str

    ua = UserAgent()
    headers = {'User-Agent':ua.random}
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        jp_comment = soup.find("div", attrs={"id":["jp_comment"]})
        yomikata = jp_comment.find("span", attrs={"class":["trs_jp bold"]}).text
        wordtype = jp_comment.find("span", attrs={"class":["commentItem"]}).text.replace("】","】\n").replace("\u3000","\n   •").replace("（","\n（").replace("《","\n《").replace("【","\n【")
        ans = "調べたい言葉は {}\n\n読み方: {}\n{}\n".format(keyword_str, yomikata, wordtype)
    except:
        ans = "お探しの情報は見つかりませんでした。"