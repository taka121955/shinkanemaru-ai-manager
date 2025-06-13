import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calc_ecp import calculate_next_bet
from utils.ai_predictor import get_ai_predictions

st.set_page_config(page_title="新金丸AIマネージャー", layout="wide")

DATA_PATH = "data/records.csv"

st.title("📊統計データ")

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    df = pd.DataFrame(columns=["日付", "場", "レース", "オッズ", "賭金", "的中", "払戻", "収支"])
    df.to_csv(DATA_PATH, index=False)

# 統計計算
total_bet = df["賭金"].sum() if not df.empty else 0
total_return = df["払戻"].sum() if not df.empty else 0
total_profit = df["収支"].sum() if not df.empty else 0
win_count = df[df["的中"] == "的中"].shape[0]
total_count = df.shape[0]
hit_rate = win_count / total_count * 100 if total_count > 0 else 0
return_rate = (total_return / total_bet) * 100 if total_bet > 0 else 0
next_bet = calculate_next_bet(df)

st.markdown(f"""
- 💼 現在の残高：{10000 + total_profit}円  
- 🎯 目標金額：20000円  
- 📈 累積損益：{total_profit}円  
- 🎯 的中率：{hit_rate:.1f}%  
- 💰 回収率：{return_rate:.1f}%  
- 🧠 次回推奨 賭金（ECP方式）：{next_bet}円
""")

# 勝敗入力
st.header("📝勝敗入力")
with st.form("form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.selectbox("競艇場", ["住之江", "大村", "丸亀", "蒲郡", "平和島"])
        race = st.text_input("レース番号", value="1R")
    with col2:
        odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
        bet = st.number_input("賭金（円）", min_value=100, step=100)

    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録する")

    if submitted:
        refund = int(bet * odds) if result == "的中" else 0
        profit = refund - bet
        new_record = {
            "日付": datetime.now().strftime("%Y-%m-%d"),
            "場": place[-1],
            "レース": race,
            "オッズ": odds,
            "賭金": bet,
            "的中": result,
            "払戻": refund,
            "収支": profit,
        }
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)
        st.success("✅記録しました！")
        st.experimental_rerun()

# 履歴表示
st.header("📚勝敗履歴")
st.dataframe(df)

# AI予想表示
st.header("🧠AI予想（的中率×勝率重視）")
predictions = get_ai_predictions()
for pred in predictions:
    st.markdown(
        f"📍{pred['場']} 第{pred['レース']}R | 式別：{pred['式別']} | 艇番：{pred['艇番']} | オッズ：{pred['オッズ']}倍"
    )
