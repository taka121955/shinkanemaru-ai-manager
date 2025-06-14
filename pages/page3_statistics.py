import streamlit as st
import pandas as pd
from datetime import datetime

CSV_PATH = "results.csv"

def load_data():
    try:
        df = pd.read_csv(CSV_PATH)
        df["日付"] = pd.to_datetime(df["日付"], errors='coerce')
        df.dropna(subset=["日付"], inplace=True)
        return df
    except Exception:
        return pd.DataFrame(columns=["日付", "競艇場", "レース", "賭金", "オッズ", "的中"])

def compute_set_stats(df):
    if len(df) < 3:
        return None

    last_set = df.tail(3).copy()
    total_bet = last_set["賭金"].sum()
    payout = sum(last_set["賭金"] * last_set["オッズ"] * (last_set["的中"] == "的中"))
    profit = payout - total_bet
    win_count = (last_set["的中"] == "的中").sum()
    recovery_rate = round(payout / total_bet * 100, 1) if total_bet > 0 else 0

    return {
        "セット件数": len(last_set),
        "総賭金": total_bet,
        "総回収": payout,
        "利益": profit,
        "的中数": win_count,
        "回収率": recovery_rate,
        "詳細": last_set.reset_index(drop=True)
    }

def page_statistics():
    st.markdown("### 📊 ECP1セット（直近3件）の統計")

    df = load_data()
    if df.empty:
        st.info("データがまだ記録されていません。")
        return

    stats = compute_set_stats(df)
    if not stats:
        st.warning("まだ3件分の記録がないため、ECPセットが完成していません。")
        return

    col1, col2 = st.columns(2)
    with col1:
        st.metric("🎯 的中数", f"{stats['的中数']} / 3")
        st.metric("💰 総賭金", f"{int(stats['総賭金'])} 円")
    with col2:
        st.metric("📈 回収率", f"{stats['回収率']} %")
        st.metric("📉 利益", f"{int(stats['利益'])} 円")

    with st.expander("📄 セット詳細"):
        st.dataframe(stats["詳細"])

page_statistics()
