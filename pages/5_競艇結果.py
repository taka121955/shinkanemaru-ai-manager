import streamlit as st

def show_page():
    st.markdown("### ⑤競艇結果")

    st.info("ここに競艇の最新レース結果や履歴を表示できます。")

    # プレースホルダー的なサンプル（今後スクレイピングやAPIと連携予定）
    st.write("🚤 例：")
    st.write("- 2025/06/14 丸亀12R 1-2-3 的中")
    st.write("- 2025/06/14 多摩川10R 5-1-2 外れ")

    st.markdown("---")
    st.caption("※ 今後、公式サイト連携や自動取得機能を搭載予定です。")
