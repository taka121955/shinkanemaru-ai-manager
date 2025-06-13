import streamlit as st
import pandas as pd
from utils.calc_ecp import calculate_next_bet

st.title("📊 統計データ")

# 勝敗履歴ファイルの読み込み or 初期化
csv_file = "history.csv"
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame(columns=["場", "レース", "オッズ", "賭金", "的中", "払戻", "収支"])
    df.to_csv(csv_file, index=False)

# 統計計算
total_bet = df["賭金"].sum() if not df.empty else 0
total_return = df["払戻"].sum() if not df.empty else 0
total_profit = df["収支"].sum() if not df.empty else 0
win_count = df[df["的中"] == "的中"].shape[0]
total_count = df.shape[0]

win_rate = win_count / total_count * 100 if total_count > 0 else 0
hit_rate = win_rate
roi = (total_return / total_bet) * 100 if total_bet > 0 else 0
next_bet = calculate_next_bet(df)

# 表示
st.markdown(f"💼 現在の残高：{10000 + total_profit}円")
st.markdown(f"🎯 目標金額：20000円")
st.markdown(f"📈 累積損益：{total_profit}円")
st.markdown(f"🎯 的中率：{hit_rate:.1f}%")
st.markdown(f"🏆 勝率：{win_rate:.1f}%")
st.markdown(f"💸 回収率：{roi:.1f}%")
st.markdown(f"🧠 次回推奨 賭金（ECP方式）：{next_bet}円")

# 入力フォーム
st.subheader("✏️ 勝敗入力")
場 = st.selectbox("競艇場", ["大村", "住之江", "平和島", "蒲郡", "丸亀"])
レース = st.text_input("レース番号", "1R")
オッズ = st.number_input("オッズ", min_value=1.5, step=0.1)
賭金 = st.number_input("賭金", min_value=100, step=100)
的中 = st.radio("結果", ["的中", "不的中"])

if st.button("記録する"):
    払戻 = int(賭金 * オッズ) if 的中 == "的中" else 0
    収支 = 払戻 - 賭金
    df.loc[len(df)] = [場, レース, オッズ, 賭金, 的中, 払戻, 収支]
    df.to_csv(csv_file, index=False)
    st.success("✅ 記録しました！")
    
