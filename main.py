import streamlit as st
import pandas as pd
import datetime
import random

st.set_page_config(page_title="AI競艇資金マネージャー", layout="wide")

# 初期化
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "結果", "収支"])

if "balance" not in st.session_state:
    st.session_state.balance = 10000

# 日本時間の表示（最上部）
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.markdown(f"### 🕒 日本時間：**{now.strftime('%Y/%m/%d %H:%M:%S')}**")

# ダミーAI予想（本来はAIで出力）
def generate_predictions():
    predictions = []
    for _ in range(5):
        race_no = random.randint(1, 12)
        odds = round(random.uniform(1.5, 10.0), 2)
        prediction = {
            "競艇場": random.choice(["大村", "住之江", "平和島", "蒲郡", "丸亀"]),
            "レース": f"{race_no}R",
            "式別": random.choice(["単勝", "複勝", "3連単"]),
            "艇番": random.choice(["1-2-3", "2-1-3", "3-1-2"]),
            "オッズ": odds
        }
        predictions.append(prediction)
    return predictions

st.markdown("## 🧠 AI予想（的中率・勝率重視 上位5件）")
for pred in generate_predictions():
    st.markdown(
        f"- 競艇場：{pred['競艇場']}｜レース：{pred['レース']}｜式別：{pred['式別']}｜艇番：{pred['艇番']}｜オッズ：{pred['オッズ']}倍"
    )

# 統計表示
df = st.session_state.df
hit_count = df[df["結果"] == "的中"].shape[0]
total = df.shape[0]
hit_rate = (hit_count / total) * 100 if total > 0 else 0
win_rate = hit_rate
recovery_rate = (df["収支"].sum() / df["賭金"].sum()) * 100 if df.shape[0] > 0 and df["賭金"].sum() > 0 else 0

st.markdown("## 📊 統計データ")
st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 📉 累積収支：{df['収支'].sum()}円  
- 🎯 的中率：{hit_rate:.1f}%  
- 🏆 勝率：{win_rate:.1f}%  
- 💸 回収率：{recovery_rate:.1f}%
""")

# 勝敗入力フォーム
st.markdown("## 🎲 勝敗入力")
col1, col2, col3 = st.columns(3)

with col1:
    place = st.selectbox("競艇場", ["大村", "住之江", "平和島", "蒲郡", "丸亀"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)

bet = st.number_input("賭金", min_value=100, step=100)
result = st.radio("結果", ["的中", "不的中"])
submit = st.button("記録する")

# 記録処理
if submit:
    profit = round((odds * bet) - bet) if result == "的中" else -bet
    new_row = pd.DataFrame([{
        "日付": now.strftime('%Y/%m/%d %H:%M:%S'),
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": bet,
        "結果": result,
        "収支": profit
    }])
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)
    st.session_state.balance += profit
    st.experimental_rerun()

# 勝敗履歴表示
st.markdown("## 📘 勝敗履歴")
st.dataframe(st.session_state.df)

# 制作者名
st.markdown("---")
st.markdown("#### 制作者：小島崇彦")
