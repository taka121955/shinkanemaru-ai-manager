import streamlit as st
from datetime import datetime
from utils.calc_ecp import calculate_bet_amount  # 自動賭金関数（修正済み）

# タイトル
st.markdown("### ✍️ 勝敗入力フォーム")
st.markdown("🎯 **AI予想をベースに入力**")

# 現在時刻表示（参考用）
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.markdown(f"🕒 現在時刻： `{now}`")

# ▼ AI予想を取得（ページ①で保存された内容）
jcd_name = st.session_state.get("jcd_name", "")
shikibetsu = st.session_state.get("shikibetsu", "")
yosou = st.session_state.get("yosou", "")

# ▼ プルダウン
col1, col2 = st.columns(2)
with col1:
    jcd_selected = st.selectbox("競艇場", options=[
        "住之江", "丸亀", "唐津", "平和島", "若松", "徳山", "常滑", "蒲郡", "福岡", "児島"
    ], index=0 if jcd_name == "" else -1)
with col2:
    shikibetsu_selected = st.selectbox("式別", options=["単勝", "2連単", "3連単"], index=0 if shikibetsu == "" else -1)

# ▼ 賭け内容
input_yosou = st.text_input("反省内容（例：1-3-4）", value=yosou if yosou else "")

# ▼ ECP賭金自動反映
bet_amount = calculate_bet_amount(strategy="ecp", previous_results=[])
st.markdown(f"💰 自動ハイハイ金（ECP方式）： `{bet_amount}` 円")

# ▼ 登録ボタン
if st.button("✅ 登録する"):
    st.success(f"✅ 登録しました！\n\n- 競艇場：{jcd_selected}\n- 式別：{shikibetsu_selected}\n- 賭け：{input_yosou}\n- 金額：{bet_amount}円")
