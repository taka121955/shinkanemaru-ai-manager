import streamlit as st
import pandas as pd
import datetime
from utils.ecp import get_next_bet_amount

st.set_page_config(page_title="新金丸法 AI資金マネージャー", layout="centered")

if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 15000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

st.title("🎯 新金丸法 × AI資金マネージャー")

# 現在時刻（日本時間）
japan_time = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
st.markdown(f"### 🕒 現在時刻（日本時間）：**{japan_time.strftime('%Y/%m/%d %H:%M:%S')}**")

st.markdown("#### 💼 現在のステータス")
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "的中", "収支"])

df = st.session_state.df

# 統計
total_bet = df["賭金"].sum() if not df.empty else 0
total_return = df["収支"].sum() + total_bet if not df.empty else 0
hit_count = df["的中"].sum() if not df.empty else 0
win_count = len(df[df["収支"] > 0]) if not df.empty else 0
recovery_rate = (total_return / total_bet) if total_bet else 0
hit_rate = (hit_count / len(df)) if not df.empty else 0
win_rate = (win_count / len(df)) if not df.empty else 0

# 統計表示
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

st.markdown("---")
st.markdown("### 🎫 勝敗入力")

with st.form("result_form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.text_input("競艇場名")
        race = st.text_input("レース番号")
        odds = st.number_input("オッズ", min_value=1.0, step=0.1)
    with col2:
        bet = st.number_input("賭け金額", min_value=100, step=100)
        result = st.selectbox("結果", ["的中", "不的中"])
        submitted = st.form_submit_button("記録する")

    if submitted:
        hit = 1 if result == "的中" else 0
        profit = bet * odds - bet if hit else -bet

        new_data = {
            "日付": japan_time.strftime("%Y-%m-%d %H:%M:%S"),
            "競艇場": place,
            "レース": race,
            "オッズ": odds,
            "賭金": bet,
            "的中": hit,
            "収支": profit,
        }

        st.session_state.df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        st.session_state.balance += profit

        # ECP方式ロジック更新
        if hit:
            st.session_state.ecp["loss_count"] = 0
        else:
            st.session_state.ecp["loss_count"] += 1

        st.experimental_rerun()

st.markdown("### 📊 過去の結果")
st.dataframe(st.session_state.df)

st.markdown("---")
if st.button("🔄 1からスタート（全データ削除）"):
    st.session_state.df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "的中", "収支"])
    st.session_state.balance = 10000
    st.session_state.goal = 15000
    st.session_state.ecp = {"loss_count": 0}
    st.success("リセットしました。")
    st.experimental_rerun()
