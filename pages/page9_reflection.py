import streamlit as st
from datetime import datetime
import pytz

def show_page():
    # タイトル
    st.markdown("## ⑨ AI反省＆対策ノート 🤖📓")
    st.caption("AIと一緒に今日の賭けを振り返り、明日への改善を考えましょう。")

    st.markdown("---")

    # 📅 今日の日付（日本時間で取得）
    japan_time = datetime.now(pytz.timezone("Asia/Tokyo"))
    today_str = japan_time.strftime("%Y年%m月%d日（%a）")
    st.markdown(f"📅 本日：**{today_str}**")

    st.markdown("---")

    # 🧠 AIコメント（仮の静的メッセージ）
    st.subheader("🧠 AIコメント（分析）")
    st.info("今日は高配当狙いが多く、的中率がやや下がったようです。リスク配分を見直すと改善の余地があります。")

    # ✍️ 反省メモ入力欄
    st.subheader("✍️ 今日の気づき・反省メモ")
    memo = st.text_area(
        "反省点、感想、明日への意気込みなどを自由に入力してください。",
        placeholder="例：買い目が広すぎた／スタート展示をもっと重視したい など",
        height=150
    )

    # 🎯 明日へのアドバイス（仮表示）
    st.subheader("🎯 明日へのアドバイス（AI提案）")
    st.markdown("- イン逃げ傾向の強いレースを優先")
    st.markdown("- オッズ過信せず、選手の信頼度重視")
    st.markdown("- 買い目は3点以内に絞ると回収率が安定します")

    st.markdown("---")

    # 💾 保存ボタン（現時点では機能なし）
    st.button("📝 メモを保存（※将来的に履歴保存対応予定）")
