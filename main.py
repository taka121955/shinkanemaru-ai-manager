import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.ecp import get_next_bet_amount
from utils.ai_predictor import get_ai_predictions

# ページ設定
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>📊統計情報</h1>", unsafe_allow_html=True)

# セッションステート初期化
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}
if "history" not in st.session_state:
    st.session_state.history = []

# 現在の日本時間表示（大きめ・太字）
jst = datetime.utcnow() + timedelta(hours=9)
st.markdown(f"<h2>🕰️現在の日本時間</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='font-size: 36px; font-weight: bold;'>{jst.strftime('%Y/%m/%d %H:%M:%S')}</h1>", unsafe_allow_html=True)

# AI予想表示（仮ではなく本実装）
st.subheader("🧠AI予想（中率 × 勝率重視）")
ai_data = get_ai_predictions()
for pred in ai_data[:5]:
    st.markdown(f"🏁 {pred['場']} 🎯 {pred['レース']}R {pred['式別']}【{pred['艇番']}】🧠 スコア：{pred['score']}")

# 勝敗履歴 DataFrame
df = pd.DataFrame(st.session_state.history)

# 勝率・的中率・回収率計算
hit_count = len(df[df["的中"] == "的中"]) if not df.empty and "的中" in df.columns else 0
win_count = hit_count
total_count = len(df)
hit_rate = hit_count / total_count if total_count > 0 else 0
win_rate = win_count / total_count if total_count > 0 else 0
recovery_rate = (df["収支"].sum() / df["収支"].abs().sum()) if not df.empty and df["収支"].abs().sum() > 0 else 0

# 次回賭金（収支がプラスなら100円固定）
next_bet = 100 if df["収支"].sum() >= 0 if not df.empty else 100 else get_next_bet_amount(st.session_state.ecp["loss_count"])

# 統計表示
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%
- 🧠 次回推奨ベット額（ECP方式）：{next_bet}円
""")

# 勝敗入力
st.subheader("✏️勝敗入力")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    place = st.selectbox("競艇場", ["住之江", "若松", "丸亀", "芦屋", "大村"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=1.5, step=0.1)
with col4:
    bet_amount = st.number_input("賭金", min_value=100, step=100, value=next_bet)
with col5:
    result = st.radio("的中／不的中", ["的中", "不的中"])

# 記録ボタン
if st.button("記録"):
    income = int(bet_amount * odds) - bet_amount if result == "的中" else -bet_amount
    st.session_state.balance += income
    st.session_state.ecp["loss_count"] = 0 if result == "的中" else st.session_state.ecp["loss_count"] + 1
    new_record = {
        "日付": jst.strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": bet_amount,
        "的中": result,
        "収支": income
    }
    st.session_state.history.append(new_record)
    st.success("✅記録を保存しました。")

# 勝敗履歴表示
if not df.empty:
    st.subheader("📊勝敗履歴")
    st.dataframe(df)

# 制作者表記
st.markdown("---")
st.markdown("<p style='text-align: center;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
