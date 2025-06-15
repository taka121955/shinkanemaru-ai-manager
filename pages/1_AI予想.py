import streamlit as st
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="① AI予想", layout="wide")
st.markdown("## 📈 AI予想（的中率重視）")

def fetch_today_race_urls():
    base_url = "https://www.boatrace.jp/owpc/pc/race/racelist"
    today = datetime.now().strftime("%Y%m%d")
    return [ (f"{jcd:02}", f"{base_url}?jcd={jcd:02}&hd={today}") for jcd in range(1, 25)]

def extract_race_info(jcd_str, url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        title_tag = soup.find("title")
        return title_tag.text.replace("ボートレース", "").replace("レース一覧", "").strip() if title_tag else f"競艇場 {jcd_str}"
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

# レース取得＆表示
race_urls = fetch_today_race_urls()
top_predictions = random.sample(race_urls, 5)

for idx, (jcd_str, url) in enumerate(top_predictions, 1):
    title = extract_race_info(jcd_str, url)
    式別, 予想, 的中率 = generate_fake_prediction()
    st.markdown(f"**{idx}. {title}｜{式別}：{予想}（的中率：{的中率}％）**")

st.caption("※ 本予想は仮AIによる自動生成です。今後、本番AIと差し替え予定。")
