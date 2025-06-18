import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")

    # --- 現在時刻表示 ---
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"## 🟢 今日のステータス")
    st.markdown(f"#### 🕒 現在時刻（日本時間）： `{now}`")

    # --- Googleスプレッドシート連携設定 ---
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("your_google_credentials.json", scope)
    client = gspread.authorize(creds)

    # --- データ読み込み（シート2） ---
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/edit")
    worksheet = spreadsheet.get_worksheet(1)  # 0=シート1, 1=シート2
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)

    # --- 的中率でソートして上位10件を抽出 ---
    df["的中率"] = df["的中率"].str.replace('%', '').astype(float)
    df = df.sort_values("的中率", ascending=False).head(10)
    df["的中率"] = df["的中率"].astype(str) + "%"

    df.insert(0, "番号", range(1, len(df) + 1))

    # --- 表示 ---
    st.markdown("### 🔟 本日のAI予想（的中率 上位10件）")
    st.dataframe(df, use_container_width=True)
