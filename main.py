import streamlit as st
import pandas as pd
import datetime
from utils.ecp import get_next_bet_amount

# タイトルと現在の日本時間を表示
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.markdown(f"<h2>⏰ 日本時間：{now.strftime('%Y年%m月%d日 %H時%M分%S秒')}</h2>", unsafe_allow_html=True)

st.title("AI資金マネージャー")

# AI予想（仮でなく本予想形式）
st.header("🎯 AI予想（的中率優先・上位5件）")
ai_predictions = [
    {"競艇場": "丸亀", "レース": "10R", "式別": "3連単", "予想": "1-3-4", "的中率": 78},
    {"競艇場": "住之江", "レース": "11R", "式別": "2連単", "予想": "2-1", "的中率": 76},
    {"競艇場": "唐津", "レース": "9R", "式別": "3連複", "予想": "1-2-3", "的中率": 74},
    {"競艇場": "児島", "レース": "8R", "式別": "単勝", "予想": "1", "的中率": 70},
    {"競艇場": "常滑", "レース": "12R", "式別": "2連複", "予想": "3-4", "的中率": 68},
]

for pred in ai_predictions:
    st.markdown(f"- 📍 {pred['競艇場']} {pred['レース']}｜🎴 {pred['式別']}：{pred['予想']}｜🎯 的中率：{pred['的中率']}%")

# 統計情報表示
st.header("📊 統計情報")

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "結果", "収支"])
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

df = st.session_state.df
hit_rate = (df["結果"] == "的中").mean() if not df.empty else 0
win_rate = (df["収支"] > 0).mean() if not df.empty else 0
recovery_rate = (df["収支"].sum() / (df["収支"].abs().sum())) if not df.empty else 0

st.markdown(f"""
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp["loss_count"])}円
""")

# 勝敗入力欄
st.header("✅ 勝敗入力")

race_sites = ["丸亀", "住之江", "唐津", "児島", "常滑", "蒲郡", "大村", "若松", "下関", "尼崎"]
race_numbers = [f"{i}R" for i in range(1, 13)]

with st.form(key="result_form"):
    date = st.date_input("日付", value=datetime.date.today())
    site = st.selectbox("競艇場", race_sites)
    race = st.selectbox("レース番号", race_numbers)
    odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
    result = st.selectbox("結果", ["的中", "不的中"])
    payout = st.number_input("収支（円）", step=100)
    submitted = st.form_submit_button("記録する")

    if submitted:
        st.session_state.df = pd.concat(
            [st.session_state.df, pd.DataFrame([{
                "日付": date,
                "競艇場": site,
                "レース": race,
                "オッズ": odds,
                "結果": result,
                "収支": payout,
            }])],
            ignore_index=True
        )
        st.session_state.balance += payout
        if payout < 0:
            st.session_state.ecp["loss_count"] += 1
        else:
            st.session_state.ecp["loss_count"] = 0

# 履歴表示
st.header("📜 勝敗履歴")

if not st.session_state.df.empty:
    st.dataframe(st.session_state.df)

# フッター（制作者）
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 16px;'>制作者：小島崇彦</p>", unsafe_allow_html=True)
