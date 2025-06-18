# utils/scraper_boatrace.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re

# 競艇場コードと名称の対応表
BOAT_PLACES = {
    '01': '桐生', '02': '戸田', '03': '江戸川', '04': '平和島', '05': '多摩川',
    '06': '浜名湖', '07': '蒲郡', '08': '常滑', '09': '津', '10': '三国',
    '11': 'びわこ', '12': '住之江', '13': '尼崎', '14': '鳴門', '15': '丸亀',
    '16': '児島', '17': '宮島', '18': '徳山', '19': '下関', '20': '若松',
    '21': '芦屋', '22': '福岡', '23': '唐津', '24': '大村'
}

def get_today_date():
    """今日の日付（日本時間）をYYYYMMDD形式で取得"""
    jst = datetime.utcnow().astimezone()
    return jst.strftime('%Y%m%d')

def get_race_data(jcd):
    """指定した競艇場コードの出走表（1〜12R）を取得"""
    today = get_today_date()
    all_races = []

    for rno in range(1, 13):  # 1R〜12R
        url = f"https://www.boatrace.jp/owpc/pc/race/racedata?hd={today}&jcd={jcd}&rno={rno}"
        res = requests.get(url)
        if res.status_code != 200:
            continue

        soup = BeautifulSoup(res.content, "html.parser")
        table = soup.find("table", class_="is-tableFixed__3rdadd")

        if table is None:
            continue

        rows = table.find_all("tr")[1:]  # ヘッダー除く
        race_data = []
        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 5:
                continue
            try:
                player_name = cols[1].get_text(strip=True)
                grade = cols[2].get_text(strip=True)
                motor = cols[3].get_text(strip=True)
                exhibition = cols[4].get_text(strip=True)
                race_data.append([rno, player_name, grade, motor, exhibition])
            except:
                continue

        df = pd.DataFrame(race_data, columns=["レース", "選手", "級", "モーター2連対率", "展示タイム"])
        all_races.append(df)

    return all_races

def get_today_boat_places():
    """本日開催中の競艇場一覧（コード＋名前）"""
    today = get_today_date()
    available = []

    for jcd, name in BOAT_PLACES.items():
        url = f"https://www.boatrace.jp/owpc/pc/race/index?hd={today}&jcd={jcd}"
        res = requests.get(url)
        if res.status_code == 200 and "レース一覧" in res.text:
            available.append((jcd, name))

    return available
