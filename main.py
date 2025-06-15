import streamlit as st
from datetime import datetime

st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="centered")

# 現在時刻
now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
st.markdown(f"""
    <div style='text-align:center; background-color:#f0f8ff; padding:10px; border-radius:10px;'>
        <h2 style='font-size:26px;'>🕒 現在時刻：{now}</h2>
    </div>
""", unsafe_allow_html=True)

# タイトル
st.markdown("""
    <div style='text-align:center; margin-top:20px;'>
        <h1 style='font-size:34px;'>💼 新金丸法 × AI資金マネージャー</h1>
        <p style='font-size:18px;'>以下のページを選択してください</p>
    </div>
""", unsafe_allow_html=True)

# メニュー表示（装飾付き）
st.markdown("""
    <div style='text-align:center; margin-top:20px;'>
        <span style='display:inline-block; background-color:#d0eaff; padding:12px 25px; margin:8px; font-size:18px; border-radius:10px;'>① AI予想</span>
        <span style='display:inline-block; background-color:#ffe0cc; padding:12px 25px; margin:8px; font-size:18px; border-radius:10px;'>② 勝敗入力</span>
        <span style='display:inline-block; background-color:#fff4cc; padding:12px 25px; margin:8px; font-size:18px; border-radius:10px;'>③ 統計データ</span><br>
        <span style='display:inline-block; background-color:#e2e2ff; padding:12px 25px; margin:8px; font-size:18px; border-radius:10px;'>④ 結果履歴</span>
        <span style='display:inline-block; background-color:#ffe0f0; padding:12px 25px; margin:8px; font-size:18px; border-radius:10px;'>⑤ 競艇結果</span>
        <span style='display:inline-block; background-color:#d7ffd7; padding:12px 25px; margin:8px; font-size:18px; border-radius:10px;'>⑥ 資金設定</span>
    </div>
""", unsafe_allow_html=True)

# 資金ステータス表示
st.markdown("""
    <div style='text-align:center; margin-top:30px; font-size:20px; background-color:#f9f9f9; padding:20px; border-radius:15px;'>
        🎯 <b style='color:#0033cc;'>目標金額</b>：<span style='color:#0033cc;'>50,000円</span><br>
        💰 <b style='color:#008800;'>準備金額</b>：<span style='color:#008800;'>10,000円</span><br>
        📦 <b style='color:#cc6600;'>積立金額</b>：<span style='color:#cc6600;'>3,000円</span>
    </div>
""", unsafe_allow_html=True)

# 制作者名
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px;'>制作：小島崇彦</p>", unsafe_allow_html=True)
