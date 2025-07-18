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

# ===== 現在時刻（中央表示） =====
now = datetime.now(pytz.timezone("Asia/Tokyo"))
st.markdown(f"<h2 style='text-align: center;'>{now.strftime('%Y年%m月%d日（%a） %H:%M')}</h2>", unsafe_allow_html=True)
st.markdown("---")

# ===== サイドバー メニュー =====
menu = st.sidebar.radio("📋 ページ選択", [
    "🏠 メインページ", "① AI予想", "② 勝敗入力", "③ 統計データ",
    "④ 結果履歴", "⑤ 開催結果", "⑥ 設定", "⑦ 場別予想", "⑧ 総合評価", "⑨ 特別分析"
], label_visibility="collapsed")

# ===== メインページ =====
if menu == "🏠 メインページ":
    st.markdown("## 📊 今日のステータス", unsafe_allow_html=True)

    # --- 仮データ ---
    accuracy = "85%"
    win_text = "3勝2敗"
    wins = 3
    losses = 2
    fund_now = 10000
    fund_goal = 10000
    stack = "+4,800円"
    win_rate = "70%"
    return_rate = "125%"

    # --- 勝敗色分け ---
    win_color = "#007bff" if wins > losses else "#dc3545"

    # --- 目標達成演出（点滅） ---
    flash_html = ""
    if fund_now >= fund_goal:
        flash_html = """
        <div style='text-align:center; font-size:26px; font-weight:bold; animation: flash 1s infinite;'>
            ✨ <span style='color:gold;'>目標達成！</span> ✨
        </div>
        <style>
        @keyframes flash {
            0% {color: gold;}
            50% {color: orange;}
            100% {color: gold;}
        }
        </style>
        """

    # --- Excel風ステータス表 ---
    html_table = f"""
    {flash_html}
    <style>
    .excel-table {{
        width: 90%;
        margin: auto;
        border-collapse: collapse;
        font-size: 18px;
    }}
    .excel-table td {{
        border: 1px solid #999;
        padding: 8px 14px;
        text-align: left;
        font-weight: bold;
    }}
    .excel-table tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>

    <table class="excel-table">
        <tr><td>🎯 的中率</td><td>{accuracy}</td></tr>
        <tr><td>📈 勝敗</td><td style='color:{win_color};'>{win_text}</td></tr>
        <tr><td>💰 積立金</td><td>{stack}</td></tr>
        <tr><td>🏆 勝率</td><td>{win_rate}</td></tr>
        <tr><td>✅ 回収率</td><td>{return_rate}</td></tr>
        <tr><td>🎒 軍資金</td><td>{fund_now:,}円</td></tr>
    </table>
    """
    st.markdown(html_table, unsafe_allow_html=True)

    # ===== 📁 メニュー一覧（ボタンサイズ統一） =====
    st.markdown("### 📁 メニュー一覧")

    menu_labels = [
        "① AI予想", "② 勝敗入力", "③ 統計データ",
        "④ 結果履歴", "⑤ 開催結果", "⑥ 設定",
        "⑦ 場別予想", "⑧ 総合評価", "⑨ 特別分析"
    ]

    btn_html = """
    <style>
    .menu-row {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 10px;
    }
    .menu-btn {
        display: inline-block;
        width: 160px;
        height: 50px;
        line-height: 50px;
        text-align: center;
        margin: 6px 10px;
        background-color: #f0f4f8;
        border-radius: 10px;
        border: 1.5px solid #ccc;
        text-decoration: none;
        font-weight: bold;
        color: #1a73e8;
        font-size: 16px;
        box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
        transition: all 0.2s ease-in-out;
    }
    .menu-btn:hover {
        transform: translateY(-2px);
        background-color: #e8f0fe;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
    }
    </style>
    <div class='menu-row'>
    """

    for label in menu_labels:
        btn_html += f"<a href='#' class='menu-btn'>{label}</a>"

    btn_html += "</div>"
    st.markdown(btn_html, unsafe_allow_html=True)

    st.markdown("---")
    st.info("左のメニューからページを選んでください。")

# ===== 他のページの読み込み =====
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

# ===== フッター（制作者名） =====
st.markdown("---")
st.markdown("<div style='text-align: center;'>制作：小島崇彦</div>", unsafe_allow_html=True)
