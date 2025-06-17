import streamlit as st
import pandas as pd
import datetime

def show_page():
    st.markdown("## ⑤ 出走表 🏁")

    # 日付選択（デフォルトは今日）
    today = datetime.date.today()
    selected_date = st.date_input("📅 表示する日付を選択", value=today)

    # 仮のデータ（サンプル用）
    race_data = {
        "競艇場": ["住之江", "蒲郡", "若松", "丸亀", "児島", "唐津"],
        "レース番号": [1, 2, 3, 4, 5, 6],
        "出走時間": ["15:10", "15:35", "16:00", "16:25", "16:50", "17:15"],
        "1号艇": ["A選手", "B選手", "C選手", "D選手", "E選手", "F選手"],
        "2号艇": ["G選手", "H選手", "I選手", "J選手", "K選手", "L選手"],
        "3号艇": ["M選手", "N選手", "O選手", "P選手", "Q選手", "R選手"]
    }

    df_race = pd.DataFrame(race_data)

    st.markdown(f"### 📅 {selected_date} の出走表")
    st.dataframe(df_race, use_container_width=True)

    st.caption("※ 実際のデータ取得は今後自動連携予定（現在はサンプル表示）")
