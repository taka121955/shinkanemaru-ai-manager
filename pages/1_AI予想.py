import streamlit as st
from datetime import datetime
import random

def generate_ai_predictions():
    # ダミーデータ生成（本番はAIモデルと連携）
    shikibetsu_list = ["単勝", "2連単", "2連複", "3連単", "3連複"]
    predictions = []

    for _ in range(5):
        shikibetsu = random.choice(shikibetsu_list)
        numbers = sorted(random.sample(range(1, 7), 3))
        content = "-".join(map(str, numbers))
        predictions.append({
            "式別": shikibetsu,
            "賭け内容": content
        })

    return predictions

def show_page():
    st.title("📡 本日のAI予想")
    
    # 現在時刻表示（中央・大きめ）
    now = datetime.now().strftime("📅 %Y/%m/%d 🕒 %H:%M:%S")
    st.markdown(f"<h4 style='text-align: center; color: gray;'>{now}</h4>", unsafe_allow_html=True)

    # 予想生成 or 再生成
    if st.button("🔄 AI予想を生成／更新", use_container_width=True):
        st.session_state["ai_predictions"] = generate_ai_predictions()

    # 初期表示がなければ生成
    if "ai_predictions" not in st.session_state:
        st.session_state["ai_predictions"] = generate_ai_predictions()

    st.markdown("---")
    st.markdown("### 🧠 AI予想上位5件")

    for i, prediction in enumerate(st.session_state["ai_predictions"], start=1):
        st.markdown(
            f"""
            <div style='border:1px solid #ccc; border-radius:8px; padding:10px; margin:10px 0; background-color:#f9f9f9'>
                <strong>予想 {i}：</strong><br>
                式別：<span style='color:#007bff'>{prediction['式別']}</span><br>
                内容：<span style='color:#28a745'>{prediction['賭け内容']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='text-align: right; font-size: 12px;'>※ 番号を②入力ページで選択可能</div>", unsafe_allow_html=True)
