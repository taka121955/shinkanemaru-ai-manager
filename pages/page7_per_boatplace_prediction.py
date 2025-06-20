import streamlit as st
from datetime import datetime
import pytz
import requests

def show_page():
    st.markdown("## ⑦ 本日の全レース")

    # 現在時刻（日本時間）を表示
    japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
    formatted_time = japan_time.strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間） ： <span style='color:green'>{formatted_time}</span>", unsafe_allow_html=True)

    # AI予想の取得（仮のURL使用中）
    try:
        # 本番ではこのURLをあなたのAPIエンドポイントに変更してください
        url = "https://example.com/api/today-races"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # データ表示（形式は調整可能）
        for race in data:
            st.write(race)

    except requests.exceptions.HTTPError as http_err:
        st.error(f"❌ データの取得に失敗しました：HTTP Error {http_err.response.status_code}: {http_err.response.reason}")
    except Exception as e:
        st.error(f"❌ データの取得に失敗しました：{e}")
