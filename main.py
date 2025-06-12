import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="新金丸AIマネージャー", layout="wide")

# 初期化
if "balance" not in st.session_state:
    st.session_state.balance = 10000
if "goal" not in st.session_state:
    st.session_state.goal = 20000
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=["日付", "競艇場", "レース", "オッズ", "賭金", "的中", "収支"])
if "ecp" not in st.session_state:
    st.session_state.ecp = {"loss_count": 0}

def get_next_bet_amount(loss_count):
    ecp_steps = [100, 300, 900]
    return ecp_steps[min(loss_count, len(ecp_steps) - 1)]

# 時刻表示（日本時間・大きく・太字）
jst = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.markdown(f"## 🕒 現在の日本時間：**<span style='font-size:28px;'>{jst.strftime('%Y/%m/%d %H:%M:%S')}</span>**", unsafe_allow_html=True)

# 統計表示
df = st.session_state.df
hit_rate = df["的中"].mean() if not df.empty else 0
win_rate = (df["収支"] > 0).mean() if not df.empty else 0
recovery_rate = (df["収支"].sum() / df["賭金"].sum()) if not df.empty and df["賭金"].sum() > 0 else 0

st.markdown(f"""
### 💹 資金状況
- 💼 現在の残高：{st.session_state.balance}円  
- 🎯 目標金額：{st.session_state.goal}円  
- 📉 累積損益：{df['収支'].sum() if not df.empty else 0}円  
- 🎯 的中率：{round(hit_rate * 100, 1)}%  
- 🏆 勝率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：{get_next_bet_amount(st.session_state.ecp['loss_count'])}円
""")

st.markdown("## 📝 勝敗入力")

# 勝敗記録入力（プルダウン付き）
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    place = st.selectbox("競艇場", ["若松", "丸亀", "大村", "平和島", "蒲郡", "芦屋", "尼崎", "児島", "常滑", "津", "びわこ", "下関", "宮島", "江戸川", "戸田", "多摩川", "徳山", "住之江", "鳴門", "唐津"])
with col2:
    race = st.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
with col3:
    odds = st.number_input("オッズ", min_value=1.0, step=0.1)
with col4:
    bet = st.number_input("賭金", step=100)
with col5:
    hit = st.selectbox("的中", [True, False])
with col6:
    submit = st.button("記録")

if submit:
    if odds < 1.5:
        st.warning("⚠️ オッズ1.5未満は対象外です。")
    else:
        profit = (odds * bet - bet) if hit else -bet
        new_data = {
            "日付": jst.strftime("%Y-%m-%d %H:%M:%S"),
            "競艇場": place,
            "レース": race,
            "オッズ": odds,
            "賭金": bet,
            "的中": hit,
            "収支": profit
        }
        st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_data])], ignore_index=True)
        st.session_state.balance += profit
        st.session_state.ecp["loss_count"] = 0 if hit else st.session_state.ecp["loss_count"] + 1
        st.success("✅ 記録を追加しました")

# 勝敗履歴表示
st.markdown("## 📊 勝敗履歴")
st.dataframe(st.session_state.df[::-1], use_container_width=True)
