import streamlit as st
from utils.calc_ecp import calculate_next_bet
import pandas as pd

st.markdown("## 📝 勝敗入力フォーム", unsafe_allow_html=True)
st.markdown("🎯 <span style='font-size:22px;'>AI予想をベースに入力</span>", unsafe_allow_html=True)

# ▼ 競艇場選択
競艇場一覧 = ["若松", "住之江", "丸亀", "常滑", "蒲郡", "福岡", "平和島", "児島", "鳴門", "唐津"]
st.markdown("📍 <span style='font-size:18px;'>競艇場</span>", unsafe_allow_html=True)
place = st.selectbox("", 競艇場一覧, key="place")

# ▼ 式別選択
式別一覧 = ["単勝", "2連単", "3連単"]
st.markdown("📘 <span style='font-size:18px;'>式別</span>", unsafe_allow_html=True)
bet_type = st.selectbox("", 式別一覧, key="bet_type")

# ▼ 投票内容
st.markdown("📝 <span style='font-size:18px;'>投票内容（例：1-3-4）</span>", unsafe_allow_html=True)
content = st.text_input("", key="content")

# ▼ 現在の残高・積立金（仮にここでは固定値）
initial_fund = 10000  # 初期資金
reserve_fund = 0

# ▼ ベット金額の自動計算（ECP方式）
records = []  # 実際はCSVから読み込み（後で修正可能）
bet_amount, wave, step, reserve_fund = calculate_next_bet(records, initial_fund, reserve_fund)

if bet_amount is None:
    st.markdown("<span style='color:red; font-size:20px;'>⚠️ 資金不足のためリセットが必要です。</span>", unsafe_allow_html=True)
else:
    st.markdown(f"💰 <span style='font-size:18px;'>自動賭け金（ECP方式）</span> ： <span style='color:green; font-size:20px;'>{bet_amount}円</span>", unsafe_allow_html=True)
    st.caption("← この金額で登録されます")

# ▼ 的中・不的中の選択
st.markdown("🎯 <span style='font-size:18px;'>結果は？</span>", unsafe_allow_html=True)
hit = st.radio("", ["的中", "不的中"], horizontal=True, key="hit")

# ▼ 登録ボタン
if st.button("✅ 登録する"):
    st.success("登録完了！")
    # → 登録処理を書く（CSV保存など）
