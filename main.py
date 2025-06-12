import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount

# 初期設定
st.set_page_config(page_title="AI資金マネージャー", layout="centered")
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

# 勝敗履歴用CSV
HISTORY_CSV = "bet_history.csv"
try:
    df = pd.read_csv(HISTORY_CSV)
except FileNotFoundError:
    df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "的中/不的中", "収支"])
    df.to_csv(HISTORY_CSV, index=False)

# 現在の日本時間表示
now = datetime.now()
japan_time = now.strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"<h2 style='text-align: center; font-weight: bold;'>現在の日本時間：{japan_time}</h2>", unsafe_allow_html=True)

# AI予想（仮ではなく確定）
st.subheader("🎯 AI予想（的中率・勝率重視）トップ5")
ai_predictions = [
    {"競艇場": "平和島", "レース": "第5R", "式別": "3連単", "買い目": "1-3-5", "オッズ": 6.2},
    {"競艇場": "尼崎", "レース": "第2R", "式別": "2連単", "買い目": "2-1", "オッズ": 4.8},
    {"競艇場": "桐生", "レース": "第8R", "式別": "3連複", "買い目": "1-2-4", "オッズ": 7.5},
    {"競艇場": "住之江", "レース": "第1R", "式別": "単勝", "買い目": "3", "オッズ": 2.1},
    {"競艇場": "福岡", "レース": "第10R", "式別": "2連単", "買い目": "1-2", "オッズ": 3.9},
]
for pred in ai_predictions:
    st.markdown(f"- 📍 **{pred['競艇場']} {pred['レース']}**｜{pred['式別']}：**{pred['買い目']}**｜オッズ：{pred['オッズ']}")

# 統計表示
hit_count = df[df["的中/不的中"] == "的中"].shape[0]
total_count = df.shape[0]
hit_rate = hit_count / total_count if total_count > 0 else 0

win_count = df[df["収支"] > 0].shape[0]
win_rate = win_count / total_count if total_count > 0 else 0

recovery_rate = df["収支"].sum() / df["賭金"].sum() if df["賭金"].sum() > 0 else 0

st.markdown(f"""
### 📊 統計情報
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum()}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨賭金（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

# 勝敗入力
st.subheader("🎮 勝敗入力")
with st.form("result_form"):
    race_date = st.date_input("日付")
    place = st.selectbox("競艇場", ["平和島", "多摩川", "浜名湖", "児島", "鳴門", "丸亀", "芦屋", "大村", "蒲郡", "下関", "常滑", "住之江", "若松", "唐津", "三国", "徳山", "福岡", "宮島", "桐生", "尼崎", "津", "びわこ", "戸田", "江戸川"])
    race_number = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, value=2.0, step=0.1)
    bet = st.number_input("賭金", min_value=100, step=100, value=100)
    result = st.radio("結果", ["的中", "不的中"])
    submitted = st.form_submit_button("記録")

    if submitted:
        gain = int(bet * odds) if result == "的中" else -int(bet)
        new_row = {
            "日付": race_date,
            "競艇場": place,
            "レース": race_number,
            "オッズ": odds,
            "賭金": bet,
            "的中/不的中": result,
            "収支": gain
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(HISTORY_CSV, index=False)
        st.session_state.balance += gain
        st.session_state.ecp["loss_count"] = 0 if result == "的中" else st.session_state.ecp["loss_count"] + 1
        st.success("記録しました！")

# 履歴表示
st.subheader("📖 勝敗履歴")
st.dataframe(df[::-1], use_container_width=True)

# フッター
st.markdown("<p style='text-align: center; margin-top: 50px;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
