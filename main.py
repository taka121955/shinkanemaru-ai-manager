import streamlit as st
import pandas as pd
import random
from utils.ecp import get_next_bet_amount, reset_ecp

st.set_page_config(page_title="新金丸法×ECP AI資金マネージャー", layout="centered")

# 初期化
if "records" not in st.session_state:
    st.session_state.records = []
if "initial_capital" not in st.session_state:
    st.session_state.initial_capital = 10000
if "target_capital" not in st.session_state:
    st.session_state.target_capital = 20000
if "ecp_state" not in st.session_state:
    st.session_state.ecp_state = reset_ecp()

# タイトル
st.title("💹 新金丸法 × ECP × AI 資金マネージャー")

# AI予想（仮の2件をランダム表示）
st.subheader("🔮AIの予想")
ai_predictions = [
    {"競艇場": "住之江", "レース": "1R", "理由": "初戦"},
    {"競艇場": "大村", "レース": "2R", "理由": "連勝中"},
    {"競艇場": "戸田", "レース": "3R", "理由": "波が安定"},
    {"競艇場": "平和島", "レース": "4R", "理由": "高勝率選手"}
]
sample_preds = random.sample(ai_predictions, 2)
for pred in sample_preds:
    st.write(f"🏟️：{pred['競艇場']} 🎯：{pred['レース']} 🧠理由：{pred['理由']}")

# 資金と目標設定
st.sidebar.header("⚙️ 資金設定")
initial_cap = st.sidebar.number_input("初期資金（円）", value=st.session_state.initial_capital, step=100)
target_cap = st.sidebar.number_input("目標金額（円）", value=st.session_state.target_capital, step=100)

# 更新
st.session_state.initial_capital = initial_cap
st.session_state.target_capital = target_cap

# ベット入力
st.subheader("🎯ベット記録入力")
競艇場一覧 = ["住之江", "大村", "戸田", "平和島", "桐生", "蒲郡", "江戸川", "若松"]
place = st.selectbox("競艇場名", 競艇場一覧)
race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
amount = st.number_input("賭け金額（円）", min_value=0, step=100)
odds = st.number_input("オッズ", min_value=1.0, step=0.1)
result = st.radio("結果", ["的中", "不的中"])

# 記録ボタン
if st.button("記録する"):
    profit = int(amount * (odds - 1)) if result == "的中" else -amount
    st.session_state.records.append({
        "競艇場": place,
        "レース": race,
        "賭け金": amount,
        "オッズ": odds,
        "結果": result,
        "収支": profit
    })

# データ表示
if st.session_state.records:
    df = pd.DataFrame(st.session_state.records)
    df["累積収支"] = df["収支"].cumsum() + st.session_state.initial_capital
    st.subheader("📋 決算決算表追")
    st.dataframe(df, use_container_width=True)

    # 成績計算
    total_profit = df["収支"].sum()
    current_balance = st.session_state.initial_capital + total_profit
    wins = df[df["結果"] == "的中"]
    losses = df[df["結果"] == "不的中"]
    total_bets = len(df)
    win_count = len(wins)
    hit_rate = win_count / total_bets * 100
    win_rate = (win_count / total_bets) * 100
    total_investment = df["賭け金"].sum()
    recovery_rate = (df[df["結果"] == "的中"]["収支"].sum() / total_investment * 100) if total_investment else 0

    st.markdown(f"📉 累積損益：{total_profit}円")
    st.markdown(f"🎯 的中率：{hit_rate:.1f}%")
    st.markdown(f"🏆 勝率：{win_rate:.1f}%")
    st.markdown(f"💸 回収率：{recovery_rate:.1f}%")

    # ECP方式の次回ベット額
    if df.iloc[-1]["結果"] == "不的中":
        st.session_state.ecp_state["loss"] += 1
    else:
        st.session_state.ecp_state = reset_ecp()

    next_bet = get_next_bet_amount(
        st.session_state.initial_capital,
        st.session_state.ecp_state["loss"],
        st.session_state.ecp_state["base"]
    )
    st.markdown(f"🧠 次回推奨ベット額（ECP）：{next_bet}円")

    # 終了条件
    if current_balance >= st.session_state.target_capital:
        st.success("🎉 目標金額に到達しました！")
    elif current_balance <= 0:
        st.error("💀 資金が尽きました…")

# リセットボタン
if st.button("1からスタート"):
    st.session_state.records = []
    st.session_state.ecp_state = reset_ecp()
    st.experimental_rerun()import streamlit as st
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
