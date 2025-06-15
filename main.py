# ✅ 改善版：現在時刻と資金情報（パッと見やすく）
jst = datetime.utcnow().astimezone()

st.markdown(f"""
<div style='text-align: center; margin-top: 10px;'>
    <div style='font-size: 18px;'>🕒 <b>現在時刻（日本時間）</b></div>
    <div style='font-size: 28px; font-weight: bold; margin-top: 4px;'>
        {jst.strftime('%Y/%m/%d %H:%M:%S')}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-size: 18px; line-height: 1.8em; margin-top: 12px;'>
    🎯 <b>目標金額：<span style="color:#d10000;">10000円</span></b>　
    💰 <b>初期資金：<span style="color:#007700;">5000円</span></b>　
    📊 <b>累積資金：<span style="color:#003399;">7200円</span></b>
</div>
<hr style='margin: 12px 0 20px 0;'>
""", unsafe_allow_html=True)
