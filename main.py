import streamlit as st
from datetime import datetime
import pytz
import sys
import os

# ===== ページ読み込み設定 =====
pages_dir = os.path.join(os.path.dirname(__file__), "pages")
if pages_dir not in sys.path:
    sys.path.append(pages_dir)

# ===== ページ設定 =====
st.set_page_config(page_title="新金丸法 × AI資金マネージャー", layout="wide")

# ===== 現在時刻（中央上部） =====
now = datetime.now(pytz.timezone("Asia/Tokyo"))
st.markdown(f"<h2 style='text-align: center;'>{now.strftime('%Y年%m月%d日（%a） %H:%M')}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== ✅ menu は先に定義する（これが超重要）=====
menu = st.sidebar.radio("📋 ページ選択", [
    "🏠 メインページ", "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 開催結果", "⑥ 設定", "⑦ 場別予想", "⑧ 総合評価", "⑨ 特別分析"
], label_visibility="collapsed")

# ===== 各ページ処理 =====
if menu == "🏠 メインページ":
    st.markdown("## 📊 今日のステータス", unsafe_allow_html=True)

    # ===== サンプル数値（ここを将来CSVと連動）=====
    accuracy = "85%"
    win_text = "3勝2敗"
    wins = 3
    losses = 2
    fund_now = 10000
    fund_goal = 10000
    stack = "+4,800円"
    win_rate = "70%"
    return_rate = "125%"

    # 勝ち負け色（勝ち越しで青、負け越しで赤）
    win_color = "#007bff" if wins > losses else "#dc3545"

    # 🎉 目標達成で点滅エフェクト
    flash = ""
    if fund_now >= fund_goal:
        flash = """
        <div style="text-align:center; font-size:28px; font-weight:bold; animation: flash 1s infinite;">
            ✨ 目標達成！ ✨
        </div>
        <style>
        @keyframes flash {
            0% {color: gold;}
            50% {color: orange;}
            100% {color: gold;}
        }
        </style>
        """

    html = f"""
    {flash}
    <div style='text-align: center; font-size: 24px; font-weight: bold; line-height: 2;'>
        🎯 的中率：<span>{accuracy}</span><br>
        📈 勝敗：<span style='color:{win_color};'>{win_text}</span><br>
        💰 積立金：<span>{stack}</span><br>
        🏆 勝率：<span>{win_rate}</span><br>
        ✅ 回収率：<span>{return_rate}</span><br>
        🎒 軍資金：<span>{fund_now:,}円</span><br>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
    st.markdown("---")
    st.info("左のメニューからページを選んでください。")

elif menu == "① AI予想":
    from page1_ai_prediction import show_page; show_page()

elif menu == "② 勝敗入力":
    from page2_input_result import show_page; show_page()

elif menu == "③ 統計データ":
    from page3_statistics import show_page; show_page()

elif menu == "④ 結果履歴":
    from page4_record_result import show_page; show_page()

elif menu == "⑤ 開催結果":
    from page5_today_schedule import show_page; show_page()

elif menu == "⑥ 設定":
    from page6_settings import show_page; show_page()

elif menu == "⑦ 場別予想":
    from page7_per_boatplace_prediction import show_page; show_page()

elif menu == "⑧ 総合評価":
    from page8_summary_today import show_page; show_page()

elif menu == "⑨ 特別分析":
    from page9_reflection import show_page; show_page()

# ===== フッター制作者名 =====
st.markdown("---")
st.markdown("<div style='text-align: center;'>制作：小島崇彦</div>", unsafe_allow_html=True)
