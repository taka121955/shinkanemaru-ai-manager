import streamlit as st
import pandas as pd
from utils.ecp import get_next_bet_amount, reset_ecp

st.set_page_config(page_title="AI予想 × 新金丸法 × 資金マネージャー", layout="wide")
st.title("🔮AI予想 × 新金丸法 × 資金マネージャー")

# セッション初期化
if "bets" not in st.session_state:
    st.session_state.bets = []
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "ecp" not in st.session_state:
    st.session_state.ecp = reset_ecp()

# 仮のAI予想（的中率×勝率スコア上位5件）
ai_predictions = [
    {"競艇場": "住之江", "レース": "9R", "式別": "3連単", "艇番": "1-2-3", "スコア": 0.86},
    {"競艇場": "住之江", "レース": "11R", "式別": "2連単", "艇番": "1-3", "スコア": 0.77},
    {"競艇場": "住之江", "レース": "1R", "式別": "単勝", "艇番": "1", "スコア": 0.70},
    {"競艇場": "大村", "レース": "4R", "式別": "3連複", "艇番": "2-3-4", "スコア": 0.65},
    {"競艇場": "唐津", "レース": "5R", "式別": "2連複", "艇番": "1-4", "スコア": 0.63}
]

st.subheader("📊AI予想（的中率×勝率 スコア上位5レース）")
for pred in ai_predictions:
    st.markdown(f"{pred['競艇場']}：{pred['レース']}（{pred['式別']} {pred['艇番']}） スコア：{pred['スコア']}")

# ベット記録入力
st.subheader("🎯ベット記録入力")
with st.form("bet_form"):
    col1, col2 = st.columns(2)
    with col1:
        place = st.selectbox("競艇場", ["住之江", "大村", "唐津", "戸田", "多摩川"])
    with col2:
        race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])

    amount = st.number_input("賭け金（円）", min_value=100, step=100)
    odds = st.number_input("オッズ（1.0以上）", min_value=1.0, step=0.1)
    result = st.selectbox("結果", ["的中", "不的中"])

    submitted = st.form_submit_button("登録する")
    if submitted:
        payout = int(amount * odds) if result == "的中" else -int(amount)
        st.session_state.bets.append({
            "競艇場": place,
            "レース": race,
            "賭け金": amount,
            "オッズ": odds,
            "結果": result,
            "収支": payout
        })
        st.session_state.balance += payout
        if result == "的中":
            st.session_state.ecp["loss_count"] = 0
        else:
            st.session_state.ecp["loss_count"] += 1
        st.success("記録が追加されました。")

# 決算表示
st.subheader("📋決算表")
df = pd.DataFrame(st.session_state.bets)
st.dataframe(df)

# 統計情報の計算
if not df.empty:
    cumulative_profit = int(df["収支"].sum())
    hit_rate = round((df["結果"] == "的中").sum() / len(df) * 100, 1)
    win_rate = round((df["収支"] > 0).sum() / len(df) * 100, 1)
    total_bet = df["賭け金"].sum()
    total_return = df["収支"].where(df["収支"] > 0, 0).sum()
    recovery_rate = round(total_return / total_bet * 100, 1) if total_bet > 0 else 0.0
else:
    cumulative_profit = 0
    hit_rate = 0.0
    win_rate = 0.0
    recovery_rate = 0.0

next_bet = get_next_bet_amount(st.session_state.ecp.get("loss_count", 0))

st.markdown("### 📊 統計情報")
st.markdown(
    f"現在の残高：{st.session_state.balance}円  \n"
    f"目標金額：{st.session_state.goal}円  \n"
    f"累積損益：{cumulative_profit}円  \n"
    f"的中率：{hit_rate}%  \n"
    f"勝率：{win_rate}%  \n"
    f"回収率：{recovery_rate}%  \n"
    f"次回推奨ベット額（ECP方式）：{next_bet}円"
)

if st.button("🔁 1からスタート"):
    st.session_state.bets = []
    st.session_state.balance = 10000
    st.session_state.ecp = reset_ecp()
    st.experimental_rerun()
