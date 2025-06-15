import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils.calc_ecp import calculate_next_bet

# ファイルパス設定
RESULT_CSV = "results.csv"

# 日本時間表示
jst = datetime.utcnow().astimezone()
st.markdown(f"<h3 style='text-align: center;'>🕒 現在時刻（日本時間）：{jst.strftime('%Y/%m/%d %H:%M:%S')}</h3>", unsafe_allow_html=True)

st.markdown("<h2>✍️ 勝敗入力フォーム</h2>", unsafe_allow_html=True)
st.markdown("🎯<b>AI予想をベースに入力</b>", unsafe_allow_html=True)

# 初期値の取得
if not os.path.exists(RESULT_CSV):
    df = pd.DataFrame(columns=["日時", "競艇場", "式別", "反省内容", "賭け金", "的中", "波", "段階", "積立金"])
    df.to_csv(RESULT_CSV, index=False)
else:
    df = pd.read_csv(RESULT_CSV)

# 残高・積立金の計算
initial_fund = 10000
total_bet = df["賭け金"].sum() if not df.empty else 0
reserve_fund = df["積立金"].iloc[-1] if not df.empty else 0
current_fund = initial_fund - total_bet + reserve_fund

# 競艇場と式別の選択
places = ["住之江", "丸亀", "常滑", "児島", "福岡", "蒲郡", "大村", "若松", "平和島", "芦屋"]
styles = ["単勝", "複勝", "2連単", "2連複", "3連単", "3連複"]

place = st.selectbox("競艇場", places)
style = st.selectbox("式別", styles)
content = st.text_input("反省内容（例：1-3-4）")

# ECP方式で次回賭け金を自動取得
records = df.to_dict("records")
bet, wave, step, new_reserve = calculate_next_bet(records, current_fund, reserve_fund)

if bet is None:
    st.error("💥 資金不足です。リセットしてください。")
    if st.button("🔁 リセット"):
        df = pd.DataFrame(columns=["日時", "競艇場", "式別", "反省内容", "賭け金", "的中", "波", "段階", "積立金"])
        df.to_csv(RESULT_CSV, index=False)
        st.success("🔄 リセット完了しました。初期状態に戻ります。")
else:
    st.markdown(f"<p>💰 自動ハイハイ金（ECP方式）： <strong>{bet}円</strong></p>", unsafe_allow_html=True)
    if st.button("✅ 登録する"):
        new_data = {
            "日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "競艇場": place,
            "式別": style,
            "反省内容": content,
            "賭け金": bet,
            "的中": False,
            "波": wave,
            "段階": step,
            "積立金": new_reserve
        }
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(RESULT_CSV, index=False)
        st.success("✅ 勝敗データを登録しました！")

# デバッグ表示（必要であればON）
# st.dataframe(df.tail(5))
