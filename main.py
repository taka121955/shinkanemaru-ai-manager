import streamlit as st
import pandas as pd
from datetime import datetime
from utils.ecp import get_next_bet_amount, update_ecp
from utils.ai_predictor import get_ai_predictions

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# 日本時間表示
st.markdown("### 🕓現在の日本時間")
japan_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"## {japan_time}")

# ===== AI予想 =====
st.markdown("## 🧠AI予想（的中率 × 勝率重視）")

try:
    ai_predictions = get_ai_predictions()
    if not ai_predictions:
        st.info("現在の予想はありません。")
    else:
        for pred in ai_predictions:
            race_place = pred.get("競艇場", "不明")
            race_no = pred.get("レース", "不明")
            style = pred.get("式別", "不明")
            combo = pred.get("艇番", "不明")
            odds = pred.get("オッズ", "不明")
            score = pred.get("score", 0)
            st.markdown(
                f"📍**{race_place} 第{race_no}R**｜{style}：**{combo}**｜オッズ：{odds}｜🧠スコア：{score}"
            )
except Exception as e:
    st.error(f"予想表示中にエラーが発生しました：{e}")

# ===== 統計情報 =====
st.markdown("## 📊統計情報")

if "history" not in st.session_state:
    st.session_state.history = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

df = pd.DataFrame(st.session_state.history)

total_bets = len(df)
wins = df[df["的中／不的中"] == "的中"].shape[0] if not df.empty else 0
hit_rate = (wins / total_bets) * 100 if total_bets > 0 else 0
win_rate = hit_rate
recovery_rate = (df["収支"].sum() / df["収支"].abs().sum()) * 100 if not df.empty and df["収支"].abs().sum() > 0 else 0

next_bet = 100 if df["収支"].sum() >= 0 else get_next_bet_amount(
    st.session_state.ecp["loss_count"], st.session_state.balance
)

st.markdown(f"- 💼現在の残高：{st.session_state.balance}円")
st.markdown(f"- 🎯目標金額：{st.session_state.goal}円")
st.markdown(f"- 📉累積損益：{df['収支'].sum() if not df.empty else 0}円")
st.markdown(f"- 🎯的中率：{hit_rate:.1f}%")
st.markdown(f"- 🏆勝率：{win_rate:.1f}%")
st.markdown(f"- 💸回収率：{recovery_rate:.1f}%")
st.markdown(f"- 🧠次回推奨賭金（ECP方式） ：{int(next_bet)}円")

# ===== 勝敗入力 =====
st.markdown("## 🎮勝敗入力")

today = datetime.now().strftime("%Y/%m/%d")
date = st.date_input("日付", value=datetime.strptime(today, "%Y/%m/%d"))
place = st.selectbox("競艇場", ["住之江", "大村", "若松", "桐生", "平和島"])
race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
odds = st.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
bet = st.number_input("賭金", min_value=100, step=100)
result = st.radio("結果", ["的中", "不的中"])

if st.button("記録"):
    income = int(bet * odds) if result == "的中" else 0
    profit = income - bet
    new_row = {
        "日付": date.strftime("%Y-%m-%d"),
        "競艇場": place,
        "レース": race,
        "オッズ": odds,
        "賭金": bet,
        "的中／不的中": result,
        "収支": profit
    }
    st.session_state.history.insert(0, new_row)
    st.session_state.balance += profit
    update_ecp(result, st.session_state.ecp)
    st.success("✅記録しました！")

# ===== 勝敗履歴 =====
st.markdown("## 📖勝敗履歴")

if not df.empty:
    st.dataframe(df)
else:
    st.info("まだ記録がありません。")

# ===== 制作者情報 =====
st.markdown("制作者：小島崇彦")
