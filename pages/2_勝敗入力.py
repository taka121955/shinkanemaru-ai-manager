import streamlit as st

# サンプルAI予想データ（仮）
ai_predictions = [
    {"番号": "①", "競艇場": "唐津", "式別": "2連単", "内容": "1-5", "的中率": "84%"},
    {"番号": "②", "競艇場": "若松", "式別": "3連単", "内容": "4-5-6", "的中率": "82%"},
    {"番号": "③", "競艇場": "住之江", "式別": "単勝", "内容": "3", "的中率": "81%"},
    {"番号": "④", "競艇場": "丸亀", "式別": "2連単", "内容": "2-1", "的中率": "80%"},
    {"番号": "⑤", "競艇場": "平和島", "式別": "3連単", "内容": "3-2-6", "的中率": "79%"},
    {"番号": "⑥", "競艇場": "福岡", "式別": "2連単", "内容": "1-2", "的中率": "77%"},
    {"番号": "⑦", "競艇場": "常滑", "式別": "単勝", "内容": "4", "的中率": "76%"},
    {"番号": "⑧", "競艇場": "芦屋", "式別": "3連単", "内容": "5-6-1", "的中率": "75%"},
    {"番号": "⑨", "競艇場": "尼崎", "式別": "3連単", "内容": "6-4-3", "的中率": "74%"},
    {"番号": "⑩", "競艇場": "津", "式別": "単勝", "内容": "2", "的中率": "73%"},
]

# タイトル
st.markdown("<h1 style='font-size:30px;'>📝 勝敗入力フォーム</h1>", unsafe_allow_html=True)
st.markdown("<span style='font-size:20px;'>🎯 登録する予想番号（①〜⑩）</span>", unsafe_allow_html=True)

selected_number = st.selectbox(" ", [pred["番号"] for pred in ai_predictions])

# 該当データ取得
selected_prediction = next((pred for pred in ai_predictions if pred["番号"] == selected_number), None)

if selected_prediction:
    st.markdown(f"<span style='font-size:18px;'>🚩 <b>競艇場</b>：{selected_prediction['競艇場']}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='font-size:18px;'>📘 <b>式別</b>：{selected_prediction['式別']}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='font-size:18px;'>✏️ <b>投票内容</b>：{selected_prediction['内容']}</span>", unsafe_allow_html=True)

    st.markdown(f"<span style='font-size:18px;'>💰 <b>自動賭け金（ECP方式）</b>：<span style='color:green;'>100円</span></span>", unsafe_allow_html=True)
    st.markdown("<span style='font-size:14px;'>↩ この金額で登録されます</span>", unsafe_allow_html=True)

    st.markdown("<span style='font-size:18px;'>🎯 結果は？</span>", unsafe_allow_html=True)
    result = st.radio(" ", ["的中", "不的中"], horizontal=True)

    if st.button("✅ 登録する"):
        st.success("登録が完了しました！")
else:
    st.warning("予想データが見つかりません。")
