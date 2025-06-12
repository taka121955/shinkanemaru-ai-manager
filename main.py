import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="勝敗記録アプリ", layout="centered")

st.title("📝 勝敗入力")

# 競艇場とレースの選択肢
places = ["住之江", "大村", "若松", "丸亀", "児島"]
races = [f"{i}R" for i in range(1, 13)]

# 入力欄
place = st.selectbox("競艇場", places)
race = st.selectbox("レース番号", races)
odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
bet_amount = st.number_input("賭金", min_value=100, step=100)
result = st.radio("的中／不的中", ["的中", "不的中"])
record_button = st.button("記録")

# セッション初期化
if "data" not in st.session_state:
    st.session_state.data = []

# 記録保存
if record_button:
    profit = int(bet_amount * odds) - bet_amount if result == "的中" else -bet_amount
    st.session_state.data.append({
        "日付": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": bet_amount,
        "結果": result,
        "収支": profit
    })
    st.success("✅ 記録を保存しました。")

# 履歴表示
st.subheader("📊 勝敗履歴")
df = pd.DataFrame(st.session_state.data)
if not df.empty:
    st.dataframe(df)

    # 統計情報
    hit_count = len(df[df["結果"] == "的中"])
    total = len(df)
    hit_rate = hit_count / total * 100
    win_rate = hit_rate  # 同値で扱う
    recovery_rate = df["収支"].sum() / df["賭金"].sum() * 100 if df["賭金"].sum() > 0 else 0
    profit_sum = df["収支"].sum()

    st.markdown("### 📊 統計情報")
    st.markdown(f"""
    - 💼 現在の残高：{10000 + profit_sum}円  
    - 🎯 目標金額：20000円  
    - 📉 累積損益：{profit_sum}円  
    - 🎯 的中率：{hit_rate:.1f}%  
    - 🏆 勝率：{win_rate:.1f}%  
    - 💸 回収率：{recovery_rate:.1f}%
    """)
else:
    st.info("まだ記録がありません。")
