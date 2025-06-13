import streamlit as st
from datetime import datetime
import pytz

# 日本時間の表示（太字・大きめ）
japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
st.markdown(f"## 🕒 日本時間：**{japan_time.strftime('%Y年%m月%d日（%a）%H:%M')}**")

# 初期資金と目標金額の表示（中央揃え）
st.markdown("### 💰 初期資金：**10,000円**　｜　🎯 目標金額：**10,000円**")

st.markdown("---")

# ページ構成
page = st.sidebar.selectbox("表示するページを選んでください", [
    "① AI予想（今日の出走表）",
    "② 結果記録ページ",
    "③ 統計データページ",
    "④ 勝敗入力ページ",
    "⑤ 競艇結果取込"
])

if page == "① AI予想（今日の出走表）":
    st.header("① AI予想：出走表付き")
    st.info("⚙️ 本物のAI予想機能は現在準備中です。仮ではなく実装予定。")
    # AI予想ロジック（式別・艇番・的中率でソート予定）

elif page == "② 結果記録ページ":
    st.header("② 結果記録")
    st.warning("⚠️ 機能準備中：レース結果の保存・履歴表示機能がここに実装されます。")

elif page == "③ 統計データページ":
    st.header("③ 統計データ")
    st.success("✅ 勝率、的中率、回収率などの統計表示準備中。")
    # 次回賭金や回収率表示はここに

elif page == "④ 勝敗入力ページ":
    st.header("④ 勝敗入力")
    st.write("レース結果を記録してください。")
    # 入力フォーム（競艇場名、レース番号、賭金、オッズ、結果）

elif page == "⑤ 競艇結果取込":
    st.header("⑤ 競艇結果自動入力")
    st.info("⚙️ 自動で公式サイトなどからレース結果を取得する機能（開発中）")

st.markdown("---")
st.markdown("#### 👤 制作者：小島崇彦")
