import streamlit as st
import pandas as pd
import random
from utils.ecp import get_next_bet_amount

st.title("AI予想 × 新金丸法 × 資金マネージャー")

# 初期状態の定義
if "records" not in st.session_state:
    st.session_state.records = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "target" not in st.session_state:
    st.session_state.target = 20000

# AI予想（上位3つのレースをスコア付きで表示）
races = [{"place": "住之江", "race": f"{r}R", "score": round(random.uniform(0.7, 0.9), 2)} for r in [1, 9, 11]]
races_sorted = sorted(races, key=lambda x: x["score"], reverse=True)

st.subheader("AI予想（的中率 × 勝率 スコア上位3レース）")
for r in races_sorted:
    st.write(f"{r['place']}：{r['race']}（スコア：{r['score']}）")

# 入力フォーム
st.subheader("ベット記録入力")
with st.form("bet_form"):
    col1, col2 = st.columns(2)
    place = col1.selectbox("競艇場", ["住之江", "大村", "戸田", "浜名湖"])
    race = col2.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    odds = st.number_input("オッズ（1.0以上）", min_value=1.0, value=1.5, step=0.1)
    result = st.selectbox("結果", ["的中", "不的中"])

    if st.form_submit_button("登録する"):
        bet = get_next_bet_amount(st.session_state.records)
        payout = int(bet * odds) if result == "的中" else -bet
        st.session_state.balance += payout
        st.session_state.records.append({
            "競艇場": place,
            "レース": race,
            "賭け金": bet,
            "オッズ": odds,
            "結果": result,
            "収支": payout,
            "累積収支": st.session_state.balance
        })
        st.success("記録が追加されました。")

# 統計
df = pd.DataFrame(st.session_state.records)
if not df.empty:
    wins = df[df["結果"] == "的中"].shape[0]
    total = df.shape[0]
    accuracy = wins / total * 100
    recovery = df["収支"].sum() / df["賭け金"].sum() * 100
    win_rate = accuracy
    profit = df["収支"].sum()
else:
    accuracy = recovery = win_rate = profit = 0

# 結果表示
st.subheader("統計情報")
st.markdown(f"""
- 現在の残高：{st.session_state.balance}円  
- 目標金額：{st.session_state.target}円  
- 累積利益：{profit}円  
- 的中率：{accuracy:.1f}%  
- 勝率：{win_rate:.1f}%  
- 回収率：{recovery:.1f}%
""")

# 次回ベット額表示
next_bet = get_next_bet_amount(st.session_state.records)
st.markdown(f"次回推奨ベット額（ECP方式）：{next_bet}円")

# 決算表
if not df.empty:
    st.subheader("決算表")
    st.dataframe(df)

# リセット
if st.button("1からスタート"):
    st.session_state.records = []
    st.session_state.balance = 10000
    st.success("初期状態にリセットされました。")
