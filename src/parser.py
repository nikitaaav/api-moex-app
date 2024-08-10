import requests
import json
import pandas as pd
from bs4 import BeautifulSoup as bs
from src.database import get_info_from_db


sess = requests.Session()
def get_info(tkr):
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json"
    answer = dict()
    response = sess.get(url)
    data = json.loads(response.text)
    data = data["securities"]
    df = pd.DataFrame(data["data"], columns=data["columns"])
    tkr.upper()
    answer["shortname"] = df[df.SECID == tkr].SHORTNAME.to_string(index=False)
    answer["prev"] = df[df.SECID == tkr].PREVPRICE.to_string(index=False)
    answer["fullname"] = df[df.SECID == tkr].SECNAME.to_string(index=False)
    answer["ticker"] = tkr
    # const
    trading_view_parse = get_info_from_db(tkr)
    answer["logo"] = trading_view_parse[2]
    answer["webpage"] = trading_view_parse[1]

    return answer

def get_scrp_from_trdview(tkr):
    try:
        url = f"https://ru.tradingview.com/symbols/MOEX-{tkr}/"
        r = requests.get(url)
        soup = bs(r.text, "html.parser")
        logo = soup.find_all("img", class_="tv-circle-logo-PsAlMQQF")
        webpage = soup.find_all("a", class_="apply-overflow-tooltip apply-overflow-tooltip--check-children link-GgmpMpKr")[8]["href"]

        return {
            "logo": logo[0]["src"],
            "webpage": webpage,
        }
    except:
        return {
            "logo": "",
            "webpage": "",
        }


def get_stock_tkrs():
    url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json"
    response = sess.get(url)
    data = json.loads(response.text)
    data = data["securities"]
    df = pd.DataFrame(data["data"], columns=data["columns"])
    answer = df["SECID"].tolist()
    for i in range(len(answer)):
        answer[i] = str(answer[i])

    return answer


sess.close()