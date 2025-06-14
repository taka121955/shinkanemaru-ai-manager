import streamlit as st
import pandas as pd

# 仮データ（今後CSV読み込み予定）
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame([
        {"日付": "2025/06/13", "競艇場": "住之江", "レース": "1R", "賭金": 1000, "オッズ": 2.5, "的中": "的中"},
        {"日付": "2025/06/13", "競艇場": "住之江", "レース": "2R", "賭金": 1000, "オッズ": 1.8, "的中": "不的中"},
        {"日付": "2025/06/14", "競艇場": "戸田", "レース": "1R", "賭金": 500, "オッズ": 3.0, "的中": "的中"},
        {"日付": "2025/06/14", "競艇場": "戸田", "レース": "2R", "賭金": 1000, "オッズ": 2.0, "的中": "不的中"},
    ])

df = st.session_state.df

# 統計計算
total_bets = len(df)
total_money = df["賭金"].sum()
total_hits = df[df["的中"] == "的中"].shape[0]
hit_rate = total_hits / total_bets * 100 if total_bets else 0
recovery = (df[df["的中"] == "的中"]["オッズ"] * df[df["的中"] == "的中"]["賭金"]).sum()
recovery_rate = recovery / total_money * 100 if total_money else 0
win_rate = total_hits / total_bets * 100 if total_bets else 0

# A. 統計表示
st.markdown("## 📊 今までの統計")
col1, col2, col3 = st.columns(3)
col1.metric("総レース数", f"{total_bets} 回")
col2.metric("総賭金", f"{total_money} 円")
col3.metric("的中数", f"{total_hits} 回")

col1, col2, col3 = st.columns(3)
col1.metric("的中率", f"{hit_rate:.1f} %")
col2.metric("回収率", f"{recovery_rate:.1f} %")
col3.metric("勝率", f"{win_rate:.1f} %")

st.markdown("---")

# B. 最新レース（削除付き）
st.markdown("## 🎯 最新の1レース結果")

if len(df) > 0:
    latest = df.iloc[-1]
    回収金 = latest["賭金"] * latest["オッズ"] if latest["的中"] == "的中" else 0
    利益 = 回収金 - latest["賭金"]

    st.write(f"📅 日付: {latest['日付']} / 🏟️ {latest['競艇場']} {latest['レース']}")
    st.write(f"💰 賭金: {latest['賭金']} 円 / 🎯 オッズ: {latest['オッズ']}")
    st.write(f"📌 的中: {latest['的中']} / 💸 回収金: {回収金:.0f} 円 / 📈 利益: {利益:.0f} 円")

    if st.button("🗑️ 最新レースを削除（クリア）"):
        st.session_state.df = df.iloc[:-1]
        st.experimental_rerun()
else:
    st.info("表示する最新レースがありません。")

st.markdown("---")
st.markdown("### 📝 記録一覧")
st.dataframe(df, use_container_width=True)
