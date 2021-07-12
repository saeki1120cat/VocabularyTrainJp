import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def train_jpy(keyword_str):
    global ans
    url = 'https://dict.asia/jc/' + keyword_str

    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        ans = "調べたい言葉は {}".format(keyword_str)
        if re.match("\n未找到该日语单词", soup.find("div", attrs={"id": ["jp_Resunt_panel"]}).text):

            find_url = soup.find("div", attrs={"id": ["jp_Resunt_panel"]}).find("a").get("href")
            res2 = requests.get(find_url, headers=headers)
            soup2 = BeautifulSoup(res2.text, 'html.parser')

            cn_url = 'https://dict.asia' + soup2.find("span", attrs={"class": ["commentItem"]}).find("a").get("href")
            res3 = requests.get(cn_url, headers=headers)
            soup3 = BeautifulSoup(res3.text, 'html.parser')

            jp_comment3 = soup3.find_all("div", attrs={"id": ["jp_comment"]}, limit=5)
            for jp in jp_comment3:
                jpword = jp.find("span", attrs={"class": ["jpword"]}).text
                yomikata = jp.find("span", attrs={"class": ["trs_jp bold"]}).text
                wordtype = jp.find("span", attrs={"class": ["commentItem"]}).text.replace("】", "】\n").replace("\u3000",
                                                                                                              "\n   •").replace(
                    "（", "\n（").replace("《", "\n《").replace("【", "\n【")
                ans = ans + "\n\n《≪ {} ≫》\n\n• 読み方: {}{}\n".format(jpword, yomikata, wordtype)


        else:
            if re.match("\n没找到", soup.find("div", attrs={"id": ["jp_Resunt_panel"]}).text):
                ans = ans + "\nお探しの情報は見つかりませんでした。"

            else:
                jp_comment = soup.find_all("div", attrs={"id": ["jp_comment"]}, limit=5)
                for jp in jp_comment:
                    jpword = jp.find("span", attrs={"class": ["jpword"]}).text
                    yomikata = jp.find("span", attrs={"class": ["trs_jp bold"]}).text
                    wordtype = jp.find("span", attrs={"class": ["commentItem"]}).text.replace("】", "】\n").replace(
                        "\u3000", "\n   •").replace("（", "\n（").replace("【", "\n【")
                    ans = ans + "\n\n《≪ {} ≫》\n\n• 読み方: {}{}\n".format(jpword, yomikata, wordtype)

    except:
        ans = ans + "\nお探しの情報は見つかりませんでした。"