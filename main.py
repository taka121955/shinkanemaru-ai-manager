import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount
from utils.ai_predictor import get_ai_predictions

st.set_page_config(page_title="新金丸法 × AI予想マネージャー", layout="wide")

# セッション初期化
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}
if "records" not in st.session_state:
    st.session_state.records = []

# 📅 日本時間表示
now_japan = datetime.utcnow().astimezone().strftime("%Y年%m月%d日 %H:%M:%S")
st.markdown(f"<h2 style='font-size:28px; font-weight:bold;'>🕒 日本時間：{now_japan}</h2>", unsafe_allow_html=True)

# 🧠 AI予想
st.subheader("🧠AI予想（的中率 × 勝率重視）")
ai_preds = get_ai_predictions()
for pred in ai_preds:
    try:
        st.markdown(f"🏟️ {pred['場']} 🎯{pred['レース']}R 💡{pred['式別']} 🎯{pred['買い目']} 💡スコア：{pred['score']}")
    except KeyError:
        pass

# 📊 統計情報
df = pd.DataFrame(st.session_state.records)
if not df.empty:
    df["収支"] = df.apply(
        lambda row: row["賭金"] * row["オッズ"] if row["結果"] == "的中" else -row["賭金"], axis=1
    )

hit_count = len(df[df["結果"] == "的中"]) if not df.empty else 0
win_count = hit_count
total_count = len(df) if not df.empty else 0

hit_rate = hit_count / total_count if total_count else 0
win_rate = win_count / total_count if total_count else 0
recovery_rate = df["収支"].sum() / df["賭金"].sum() if not df.empty and df["賭金"].sum() != 0 else 0

next_bet = 100 if df["収支"].sum() >= 0 else get_next_bet_amount(st.session_state.ecp["loss_count"])

st.markdown(f"""
### 📈統計情報
- 💼現在の残高：{st.session_state.balance}円
- 🎯目標金額：{st.session_state.goal}円
- 📉累積損益：{df["収支"].sum() if not df.empty else 0}円
- 🎯的中率：{round(hit_rate*100, 1)}%
- 🏆勝率：{round(win_rate*100, 1)}%
- 💸回収率：{round(recovery_rate*100, 1)}%
- 🧠次回推奨ベット額（ECP方式）：{next_bet}円
""")

# 📝 勝敗入力
st.subheader("✏️ 勝敗入力")
col1, col2, col3, col4, col5 = st.columns(5)
place = col1.selectbox("競艇場", ["住之江", "丸亀", "芦屋", "若松", "蒲郡", "大村", "平和島"])
race_number = col2.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
odds = col3.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
amount = col4.number_input("賭金", min_value=100, step=100)
result = col5.radio("的中／不的中", ["的中", "不的中"])
if st.button("記録"):
    st.session_state.records.append({
        "日付": now_japan,
        "競艇場": place,
        "レース": race_number,
        "オッズ": odds,
        "賭金": amount,
        "結果": result
    })
    if result == "不的中":
        st.session_state.balance -= amount
        st.session_state.ecp["loss_count"] += 1
    else:
        st.session_state.balance += amount * odds
        st.session_state.ecp["loss_count"] = 0
    st.rerun()

# 📋 勝敗履歴
st.subheader("📊 勝敗履歴")
if not df.empty:
    df["収支"] = df.apply(
        lambda row: row["賭金"] * row["オッズ"] if row["結果"] == "的中" else -row["賭金"],
        axis=1
    )
    st.dataframe(df)
else:
    st.info("記録がまだありません。")

# 🧹 リセット機能
if st.button("1からスタート"):
    st.session_state.records = []
    st.session_state.balance = 10000
    st.session_state.ecp["loss_count"] = 0
    st.rerun()

# 👤 制作者表記
st.markdown("---")
st.markdown("制作：**小島崇彦**")
