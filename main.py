import streamlit as st
import pandas as pd
from datetime import datetime
import pytz
from utils.ecp import get_next_bet_amount

# 初期化
if "data" not in st.session_state:
    st.session_state.data = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 15000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

st.set_page_config(page_title="AI資金マネージャー", layout="centered")

st.title("💰 新金丸式 × AI資金マネージャー")

# 現在の日本時間を表示（太字・大きめ）
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst).strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"### 🕒 日本時間：**{now}**")

# 勝敗記録入力
st.subheader("🎯 勝敗記録入力")

col1, col2, col3 = st.columns(3)
with col1:
    stadium = st.selectbox("競艇場名", [
        "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑",
        "津", "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島",
        "宮島", "徳山", "下関", "若松", "芦屋", "福岡", "唐津", "大村"
    ])
with col2:
    race_no = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)

col4, col5 = st.columns(2)
with col4:
    result = st.radio("結果", ["的中", "不的中"])
with col5:
    amount = st.number_input("賭け金額（円）", min_value=100, step=100)

if st.button("✅ 登録"):
    if amount > st.session_state.balance:
        st.error("残高が不足しています。")
    else:
        gain = int(amount * odds) if result == "的中" else 0
        profit = gain - amount
        st.session_state.balance += profit
        if result == "不的中":
            st.session_state.ecp["loss_count"] += 1
        else:
            st.session_state.ecp["loss_count"] = 0

        st.session_state.data.append({
            "時間": now,
            "競艇場": stadium,
            "R": race_no,
            "オッズ": odds,
            "結果": result,
            "金額": amount,
            "払戻": gain,
            "収支": profit,
        })
        st.success("記録しました！")

# データ表示
df = pd.DataFrame(st.session_state.data)

if not df.empty:
    st.subheader("📊 勝敗履歴")
    st.dataframe(df)

    # 統計情報
    total = len(df)
    hit = len(df[df["結果"] == "的中"])
    win = len(df[df["収支"] > 0])
    hit_rate = hit / total if total > 0 else 0
    win_rate = win / total if total > 0 else 0
    total_invested = df["金額"].sum()
    total_return = df["払戻"].sum()
    recovery_rate = total_return / total_invested if total_invested > 0 else 0

    st.markdown(f"""
    - 💼 現在の残高：{st.session_state.balance}円  
    - 🎯 目標金額：{st.session_state.goal}円  
    - 📉 累積損益：{df['収支'].sum()}円  
    - 🎯 的中率：{round(hit_rate * 100, 1)}%  
    - 🏆 勝率：{round(win_rate * 100, 1)}%  
    - 💸 回収率：{round(recovery_rate * 100, 1)}%  
    - 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
    """)

# AI予想（仮でないバージョンが別途必要なら次で対応）
st.subheader("🧠 AI予想（的中率 × 勝率 重視）")
# ダミーデータ表示（本物予想は別途処理）
predictions = [
    {"競艇場": "住之江", "R": "3R", "式別": "3連単", "買い目": "1-3-4"},
    {"競艇場": "尼崎", "R": "5R", "式別": "2連単", "買い目": "2-1"},
    {"競艇場": "福岡", "R": "7R", "式別": "3連単", "買い目": "3-1-2"},
    {"競艇場": "徳山", "R": "9R", "式別": "3連複", "買い目": "1-2-3"},
    {"競艇場": "唐津", "R": "12R", "式別": "2連単", "買い目": "1-2"},
]

for p in predictions:
    st.markdown(f"- {p['競艇場']} {p['R']}｜{p['式別']}｜🎯 {p['買い目']}")
    
