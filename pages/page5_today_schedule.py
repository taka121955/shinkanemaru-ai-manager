# pages/page5_boat_results.py

import streamlit as st
import datetime
from utils.scraper_boatrace import get_today_boat_places, get_race_data

def show_page():
    st.markdown("## ⑤ 出走表 🏁")

    # 本日の日付（固定）
    today = datetime.date.today()
    st.markdown(f"### 📅 本日：{today.strftime('%Y年%m月%d日')}")

    # 本日開催中の競艇場を取得
    with st.spinner("開催中の競艇場を確認中..."):
        places = get_today_boat_places()

    if not places:
        st.warning("⚠️ 本日開催中の競艇場データを取得できませんでした。")
        return

    # プルダウンで競艇場選択
    options = {name: code for code, name in places}
    selected_place_name = st.selectbox("🏟️ 競艇場を選択", list(options.keys()))
    selected_code = options[selected_place_name]

    # 出走表取得
    with st.spinner(f"{selected_place_name} の出走表を取得中..."):
        all_races = get_race_data(selected_code)

    if not all_races:
        st.error("❌ 出走表の取得に失敗しました。")
        return

    st.markdown(f"### 🚤 {selected_place_name} の出走表（全12R）")

    # 各レースの出走表を1つのテーブルとして順番に表示
    for df in all_races:
        rno = int(df.iloc[0]["レース"]) if not df.empty else None
        if rno:
            st.markdown(f"#### 🎯 {rno}R 出走表")
            st.dataframe(df, use_container_width=True)
