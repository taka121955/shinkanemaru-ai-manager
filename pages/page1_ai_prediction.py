import streamlit as st
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import random

def fetch_today_race_urls():
    base_url = "https://www.boatrace.jp/owpc/pc/race/racelist"
    today = datetime.now().strftime("%Y%m%d")
    race_urls = []
    for jcd in range(1, 25):
        jcd_str = f"{jcd:02}"
        url = f"{base_url}?jcd={jcd_str}&hd={today}"
        race_urls.append((jcd_str, url))
    return race_urls

def extract_race_info(jcd_str, url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        title_tag = soup.find("title")
        if title_tag:
            return title_tag.text.strip().replace("ボートレース", "").replace("レース一覧", "").strip()
        else:
            return f"競艇場 {jcd_str}"
    except:
        return f"競艇場 {jcd_str}（取得失敗）"

def generate_fake_prediction():
    式別 = random.choice(["3連単", "2連単", "単勝"])
    if 式別 == "3連単":
        予想 = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
    elif 式別 == "2連単":
        予想 = f"{random.randint(1,6)}-{random.randint(1,6)}"
    else:
        予想 = f"{random.randint(1,6)}"
    的中率 = random.randint(70, 95)
    return 式別, 予想, 的中率

def show_page():
    st.title("① AI予想（本物処理準備中）")

    jst = datetime.utcnow().astimezone()
    st.markdown(f"🕒 現在時刻（日本時間）：**{jst.strftime('%Y/%m/%d %H:%M:%S')}**")

    st.markdown("### 🎯 本日のAI予想（的中率重視）")

    race_urls = fetch_today_race_urls()
    top_predictions = []

    selected_races = random.sample(race_urls, 5)

    for jcd_str, url in selected_races:
        title = extract_race_info(jcd_str, url)
        式別, 予想, 的中率 = generate_fake_prediction()
        top_predictions.append({
            "競艇場": title,
            "式別": 式別,
            "予想": 予想,
            "的中率": f"{的中率}％"
        })

    for idx, p in enumerate(top_predictions, 1):
        st.markdown(
            f"**{idx}. {p['競艇場']}｜{p['式別']}：{p['予想']}（的中率：{p['的中率']}）**"
        )

    st.caption("※ 現在は仮予想ロジック。近日中に正式AIモデルを接続予定。")
