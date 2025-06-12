from datetime import datetime
import pandas as pd
import streamlit as st

# --- ダミーのAI予想関数 ---
def get_ai_predictions():
    return [
        {"場": "住之江", "レース": "9", "式別": "3連単", "買い目": "1-2-3", "score": 0.86},
        {"場": "住之江", "レース": "11", "式別": "3連単", "買い目": "2-1-3", "score": 0.77},
        {"場": "住之江", "レース": "1", "式別": "3連単", "買い目": "1-3-2", "score": 0.70},
        {"場": "大村", "レース": "5", "式別": "3連単", "買い目": "3-1-2", "score": 0.68},
        {"場": "丸亀", "レース": "7", "式別": "3連単", "買い目": "1-2-6", "score": 0.66},
    ]

# --- 初期設定 ---
st.set_page_config(page_title="AI予想×新金丸法", layout="wide")

# --- 日本時間表示 ---
st.markdown("### 🕒 現在の日本時間")
st.markdown(f"<h2><b>{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}</b></h2>", unsafe_allow_html=True)

# --- AI予想表示 ---
st.markdown("## 🧠 AI予想（中率 × 勝率重視）")
for pred in get_ai_predictions():
    st.markdown(f"🏁 {pred['場']} 🎯{pred['レース']}R 🧠 {pred['式別']}【{pred['買い目']}】 スコア：{pred['score']}")

# --- セッション初期化 ---
if "records" not in st.session_state:
    st.session_state.records = []

df = pd.DataFrame(st.session_state.records)

# --- 統計情報 ---
st.markdown("## 📊 統計情報")
hit_count = df[df["結果"] == "的中"].shape[0] if not df.empty else 0
total_count = df.shape[0]
win_rate = hit_count / total_count if total_count > 0 else 0
recovery_rate = (
    df["収支"].sum() / df["賭金"].sum()
    if not df.empty and df["賭金"].sum() > 0 else 0
)
current_balance = 10000 + (df["収支"].sum() if not df.empty else 0)

st.markdown(f"""
- 💼 現在の残高：{current_balance}円  
- 🎯 的中率：{round(win_rate * 100, 1)}%  
- 💸 回収率：{round(recovery_rate * 100, 1)}%  
- 🧠 次回推奨ベット額（ECP方式）：100円
""")

# --- 勝敗入力フォーム ---
st.markdown("## ✏️ 勝敗入力")
col1, col2, col3, col4, col5 = st.columns(5)
場 = col1.selectbox("競艇場", ["住之江", "大村", "丸亀", "芦屋", "若松"])
レース = col2.selectbox("レース番号", [f"{i}R" for i in range(1, 13)])
オッズ = col3.number_input("オッズ（1.5以上）", min_value=1.5, step=0.1)
賭金 = col4.number_input("賭金", min_value=100, step=100)
結果 = col5.radio("的中／不的中", ["的中", "不的中"])

# --- 記録保存処理 ---
if st.button("記録"):
    収支 = int(賭金 * オッズ) - 賭金 if 結果 == "的中" else -賭金
    st.session_state.records.append({
        "日付": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "競艇場": 場,
        "レース": レース,
        "オッズ": オッズ,
        "賭金": 賭金,
        "結果": 結果,
        "収支": 収支
    })
    st.success("✅ 記録を保存しました。")
    st.experimental_rerun()

# --- 勝敗履歴表示 ---
st.markdown("## 📉 勝敗履歴")
if not df.empty:
    st.dataframe(df)
else:
    st.info("履歴がまだありません。")

# --- フッター ---
st.markdown("---")
st.markdown("制作者：小島崇彦")
