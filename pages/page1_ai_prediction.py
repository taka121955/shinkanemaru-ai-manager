import streamlit as st
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import random

def show_ai_prediction():
    st.markdown("### 🎯 本日のAI予想（的中率重視）")

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
                return title_tag.text.replace("ボートレース", "").replace("レース一覧", "").strip()
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

    race_urls = fetch_today_race_urls()
    top_predictions = random.sample(race_urls, 5)

    for idx, (jcd_str, url) in enumerate(top_predictions, 1):
        title = extract_race_info(jcd_str, url)
        式別, 予想, 的中率 = generate_fake_prediction()
        st.markdown(f"**{idx}. {title}｜{式別}：{予想}（的中率：{的中率}％）**")

    st.caption("🔧 現在は仮のAI予想です。本番モデルは順次連携予定です。")
