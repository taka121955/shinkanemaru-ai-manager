import streamlit as st
import pandas as pd
import datetime
from utils.ecp import get_next_bet_amount

st.set_page_config(page_title="新金丸AI資金マネージャー", layout="centered")

st.title("🎯 新金丸法 × ECP × AI予想 資金マネージャー")

# 現在の日本時間を大きく太字で表示
now_japan = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.markdown(f"<h3><b>🕒 日本時間：{now_japan.strftime('%Y/%m/%d %H:%M:%S')}</b></h3>", unsafe_allow_html=True)

# セッション初期化
if "history" not in st.session_state:
    st.session_state.history = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

# リセットボタン
if st.button("🔁 1からスタート（履歴削除）"):
    st.session_state.history = []
    st.session_state.balance = 10000
    st.session_state.ecp = {"loss_count": 0}
    st.success("データをリセットしました。")

# 入力フォーム
st.subheader("📥 勝敗入力")

col1, col2, col3 = st.columns(3)
with col1:
    result = st.selectbox("結果", ["的中", "不的中"])
with col2:
    odds = st.number_input("オッズ", min_value=1.0, step=0.1, value=1.5)
with col3:
    amount = st.number_input("賭け金額（円）", min_value=100, step=100, value=get_next_bet_amount(st.session_state.ecp["loss_count"]))

if st.button("✅ 入力確定"):
    profit = int(amount * odds) - amount if result == "的中" else -amount
    st.session_state.balance += profit
    st.session_state.history.append({
        "日時": now_japan.strftime("%Y/%m/%d %H:%M:%S"),
        "結果": result,
        "オッズ": odds,
        "賭け金": amount,
        "収支": profit
    })
    if result == "的中":
        st.session_state.ecp["loss_count"] = 0
    else:
        st.session_state.ecp["loss_count"] += 1
    st.success("記録しました。")

# データフレーム化
df = pd.DataFrame(st.session_state.history)

# 統計
if not df.empty:
    hit_count = df[df["結果"] == "的中"].shape[0]
    win_count = df[df["収支"] > 0].shape[0]
    total_count = df.shape[0]
    total_bet = df["賭け金"].sum()
    total_profit = df["収支"].sum()

    hit_rate = hit_count / total_count * 100
    win_rate = win_count / total_count * 100
    recovery_rate = (total_profit + total_bet) / total_bet * 100 if total_bet > 0 else 0
else:
    hit_rate = win_rate = recovery_rate = 0
    total_profit = 0

st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{total_profit}円  
- 🎯 的中率：{round(hit_rate, 1)}%  
- 🏆 勝率：{round(win_rate, 1)}%  
- 💸 回収率：{round(recovery_rate, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

# 履歴表示
st.subheader("📜 勝敗履歴")
if not df.empty:
    st.dataframe(df[::-1], use_container_width=True)
else:
    st.info("履歴がまだありません。")
