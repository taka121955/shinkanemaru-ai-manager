import streamlit as st
import pandas as pd
from utils.ecp import get_next_bet_amount, reset_ecp

st.set_page_config(page_title="新金丸法 × ECP × AI 資金マネージャー", layout="centered")

# --- 初期化 ---
if "records" not in st.session_state:
    st.session_state.records = []
if "ecp" not in st.session_state:
    st.session_state.ecp = reset_ecp()
if "initial" not in st.session_state:
    st.session_state.initial = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000

# --- タイトル ---
st.title("💰 新金丸法 × ECP × AI 資金マネージャー")

# --- 初期資金と目標金額 ---
col1, col2 = st.columns(2)
with col1:
    st.session_state.initial = st.number_input("初期資金（円）", 0, step=100, value=st.session_state.initial)
with col2:
    st.session_state.goal = st.number_input("目標金額（円）", 0, step=100, value=st.session_state.goal)

# --- AI予想ロジック（仮） ---
def ai_predict_next_bet(records):
    if not records:
        return {"競艇場": "住之江", "レース": "1R", "理由": "初戦"}
    latest = records[-1]
    if latest["結果"] == "不的中":
        return {"競艇場": "大村", "レース": "3R", "理由": "前回負けたのでナイター切替"}
    else:
        return {"競艇場": "住之江", "レース": "4R", "理由": "継続"}

# --- AI予想表示 ---
ai = ai_predict_next_bet(st.session_state.records)
st.subheader("🔮 AI予想")
st.markdown(f"**🏟️：{ai['競艇場']}　🎯：{ai['レース']}　🧠理由：{ai['理由']}**")

# --- 入力フォーム ---
st.subheader("🎯 ベット記録入力")
col1, col2 = st.columns(2)
with col1:
    stadium = st.text_input("競艇場名", value=ai['競艇場'])
with col2:
    race_number = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)], index=int(ai['レース'].replace("R", "")) - 1)

bet_amount = get_next_bet_amount(st.session_state.ecp)
odds = st.number_input("オッズ（例：1.5）", min_value=1.0, step=0.1, value=1.5)
result = st.radio("結果", ["的中", "不的中"])

if st.button("✅ 記録する"):
    profit = int(bet_amount * (odds - 1)) if result == "的中" else -bet_amount
    st.session_state.records.append({
        "競艇場": stadium,
        "レース": race_number,
        "賭け金": bet_amount,
        "オッズ": odds,
        "結果": result,
        "収支": profit
    })

    # ECP更新
    st.session_state.ecp["loss"].append(result == "不的中")
    if result == "的中":
        st.session_state.ecp["base"] = bet_amount
        st.session_state.ecp["loss"] = []

# --- 表示 ---
st.subheader("📊 決算表と統計")

if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    df["累積収支"] = df["収支"].cumsum() + st.session_state.initial
    st.dataframe(df, use_container_width=True)

    total_profit = df["収支"].sum()
    current_balance = st.session_state.initial + total_profit
    hit_count = len(df[df["結果"] == "的中"])
    hit_rate = hit_count / len(df) * 100
    win_rate = (df["収支"] > 0).sum() / len(df) * 100
    recovery_rate = df[df["結果"] == "的中"]["収支"].sum() / df["賭け金"].sum() * 100 if df["賭け金"].sum() > 0 else 0

    st.markdown(f"💼 **現在の残高： {int(current_balance)} 円**")
    st.markdown(f"📈 **累積損益： {int(total_profit)} 円**")
    st.markdown(f"🎯 **的中率： {hit_rate:.1f} %**")
    st.markdown(f"🏆 **勝率： {win_rate:.1f} %**")
    st.markdown(f"💸 **回収率： {recovery_rate:.1f} %**")
    st.markdown(f"🧠 **次回推奨ベット額（ECP） ： {get_next_bet_amount(st.session_state.ecp)} 円**")

    if current_balance >= st.session_state.goal:
        st.success("🎉 目標金額に到達しました！")
    elif current_balance <= 0:
        st.error("💀 資金が尽きました…")

else:
    st.info("まだ記録がありません。入力して記録してください。")

# --- リセット機能 ---
if st.button("🔁 1からスタート（記録リセット）"):
    st.session_state.records = []
    st.session_state.ecp = reset_ecp()
    st.success("記録をすべてリセットしました。")
