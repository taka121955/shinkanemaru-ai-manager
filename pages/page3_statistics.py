import streamlit as st
import pandas as pd

CSV_RESULT = "results.csv"
CSV_TEMP = "temp_set.csv"

# ⬇️ 目標金額と初期資金（main.pyのセッションから取得）
目標金額 = st.session_state.get("goal_amount", 10000)
初期資金 = st.session_state.get("initial_amount", 5000)

def load_data(path):
    try:
        df = pd.read_csv(path)
        df["日付"] = pd.to_datetime(df["日付"], errors='coerce')
        df.dropna(subset=["日付"], inplace=True)
        return df
    except:
        return pd.DataFrame(columns=["日付", "競艇場", "レース", "賭金", "オッズ", "的中"])

def compute_temp_stats(df):
    if df.empty:
        return None
    total_bet = df["賭金"].sum()
    payout = sum(df["賭金"] * df["オッズ"] * (df["的中"] == "的中"))
    remaining = 初期資金 - total_bet + payout
    win_count = (df["的中"] == "的中").sum()
    profit = payout - total_bet
    recovery = round((payout / total_bet) * 100, 1) if total_bet > 0 else 0
    return {
        "残金": remaining,
        "的中数": win_count,
        "総賭金": total_bet,
        "回収": payout,
        "利益": profit,
        "回収率": recovery,
        "明細": df.reset_index(drop=True)
    }

def page_statistics():
    st.markdown("## 📊 ECPセット統計（1セット）")

    # --- 現在進行中のセット ---
    df_temp = load_data(CSV_TEMP)
    stats = compute_temp_stats(df_temp)

    if df_temp.empty or stats is None:
        st.info("現在進行中のセットはありません。")
    else:
        st.dataframe(df_temp)

        st.markdown(f"### 🎯 目標金額：{目標金額:,}円")
        st.markdown(f"### 💰 初期資金：{初期資金:,}円")
        st.markdown(f"### 💼 現在の残金：{int(stats['残金']):,}円")

        if stats["残金"] < 100 or stats["残金"] >= 目標金額:
            st.success("✅ セットが終了しました（100円未満 または 目標達成）")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("🎯 的中数", f"{stats['的中数']} 本")
                st.metric("💰 総賭金", f"{int(stats['総賭金'])} 円")
            with col2:
                st.metric("📈 回収率", f"{stats['回収率']} %")
                st.metric("📉 利益", f"{int(stats['利益'])} 円")
            with st.expander("📄 セット詳細"):
                st.dataframe(stats["明細"])
        else:
            st.warning("このセットはまだ継続中です。（残金あり・未達成）")

    if st.button("🔄 セットを初期化（temp_set.csv）"):
        open(CSV_TEMP, "w").write("日付,競艇場,レース,賭金,オッズ,的中\n")
        st.success("temp_set.csv をリセットしました")

    st.markdown("---")

    # --- 永続記録（全セット） ---
    st.markdown("## 📚 全記録セット")
    df_all = load_data(CSV_RESULT)
    if df_all.empty:
        st.info("本記録（results.csv）はまだ空です。")
    else:
        st.dataframe(df_all)

page_statistics()
