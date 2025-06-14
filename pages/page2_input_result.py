import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calc_ecp import calculate_next_bet_amount

st.title("② 勝敗入力")

# ファイル名
csv_file = "results.csv"

# 目標金額・初期資金・累積資金の表示
goal = st.session_state.get("goal", 10000)
initial = st.session_state.get("initial", 3000)
total_spent = st.session_state.get("total", 0)

st.markdown(f"🎯 目標金額：{goal} 円　💰 初期資金：{initial} 円　📊 累積資金：{total_spent} 円")

# 自動で次の賭金（ECP方式）
next_bet = calculate_next_bet_amount(csv_file)

# フォーム
with st.form("input_form"):
    st.markdown("### 🎫 新しい勝敗記録を入力")
    
    today = datetime.now().strftime("%Y/%m/%d")
    date = st.text_input("日付", today)
    
    place = st.selectbox("競艇場", ["住之江", "丸亀", "鳴門", "福岡", "戸田", "芦屋"])
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

    # 賭金はECPで自動表示（編集不可）
    bet_amount = st.number_input("賭金（自動）", value=next_bet, step=100, disabled=True)

    # オッズは仮にランダム（将来的に自動取得）
    odds = round(3.0 + (next_bet % 10) * 0.5, 2)
    st.number_input("オッズ（自動）", value=odds, step=0.1, disabled=True)

    result = st.radio("結果", ["的中", "不的中"])

    # 払戻金の自動計算
    payout = int(bet_amount * odds) if result == "的中" else 0

    submitted = st.form_submit_button("✅ 記録")
    if submitted:
        new_record = pd.DataFrame([[date, place, race, bet_amount, payout]],
                                  columns=["日付", "競艇場", "レース", "賭金", "払戻金"])
        try:
            old = pd.read_csv(csv_file)
            updated = pd.concat([old, new_record], ignore_index=True)
        except FileNotFoundError:
            updated = new_record

        updated.to_csv(csv_file, index=False)
        st.success("記録しました！")

# --------------------
# 🔽 ナビゲーション（ページ下部ボタン）
# --------------------
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("① AI予想"):
        st.switch_page("pages/page1_ai_prediction.py")

with col2:
    if st.button("② 勝敗入力"):
        st.switch_page("pages/page2_input_result.py")

with col3:
    if st.button("③ 統計データ"):
        st.switch_page("pages/page3_statistics.py")

with col4:
    if st.button("④ 結果履歴"):
        st.switch_page("pages/page4_record_result.py")

with col5:
    if st.button("⑤ レース結果"):
        st.switch_page("pages/page5_boat_results.py")

# 最下部に制作者名
st.markdown("<p style='text-align: center;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
