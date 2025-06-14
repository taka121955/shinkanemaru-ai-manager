import streamlit as st
import datetime
import random

# ページ設定
st.set_page_config(page_title="① AI予想", layout="wide")

# 日本時間での現在時刻表示（中央・太字）
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.markdown(f"<h4 style='text-align:center; font-weight:bold;'>現在時刻（日本時間）: {now.strftime('%Y/%m/%d %H:%M:%S')}</h4>", unsafe_allow_html=True)

# タイトル表示
st.markdown("## 🎯 AI予想（上位5件）")

# 仮のAI予想データ（最低オッズ1.5以上・全競艇場想定）
def generate_predictions():
    places = ["住之江", "戸田", "平和島", "蒲郡", "多摩川", "丸亀", "芦屋", "若松", "大村"]
    shiki_list = ["3連単", "2連単", "3連複", "2連複", "単勝", "複勝"]
    predictions = []

    for _ in range(20):  # 多めに生成して上位5件を抽出
        place = random.choice(places)
        race = f"{random.randint(1, 12)}R"
        shiki = random.choice(shiki_list)
        if shiki == "3連単":
            content = f"{random.randint(1,6)}-{random.randint(1,6)}-{random.randint(1,6)}"
        elif shiki == "3連複":
            a, b, c = sorted(random.sample(range(1, 7), 3))
            content = f"{a}={b}={c}"
        elif shiki == "2連単":
            content = f"{random.randint(1,6)}-{random.randint(1,6)}"
        elif shiki == "2連複":
            a, b = sorted(random.sample(range(1, 7), 2))
            content = f"{a}={b}"
        else:
            content = str(random.randint(1,6))
        odds = round(random.uniform(1.5, 10.0), 1)
        predictions.append({
            "競艇場": place,
            "レース": race,
            "式別": shiki,
            "予想": content,
            "オッズ": odds
        })

    # オッズ1.5以上の中から上位5件表示
    predictions.sort(key=lambda x: x["odds"], reverse=True)
    return predictions[:5]

# 予想表示
predictions = generate_predictions()

for i, p in enumerate(predictions, 1):
    st.markdown(f"### 🔹 第{i}位")
    st.markdown(f"- 競艇場: **{p['競艇場']}**")
    st.markdown(f"- レース番号: **{p['レース']}**")
    st.markdown(f"- 式別: **{p['式別']}**")
    st.markdown(f"- 予想: **{p['予想']}**")
    st.markdown(f"- オッズ: **{p['オッズ']}倍**")
    st.divider()

# ナビゲーションボタン（ページ下部）
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("① AI予想"):
        st.switch_page("pages/page1_ai_prediction.py")
with col2:
    if st.button("② 勝敗入力"):
        st.switch_page("pages/page2_input_result.py")
with col3:
    if st.button("③ 統計データ"):
        st.switch_page("pages/page3_statistics.py")
with col4:
    if st.button("④ 結果履歴"):
        st.switch_page("pages/page4_record_result.py")
with col5:
    if st.button("⑤ 競艇結果"):
        st.switch_page("pages/page5_boat_results.py")

# 最下部に制作者名
st.markdown("<div style='text-align:center; font-size:13px;'>制作者：小島崇彦</div>", unsafe_allow_html=True)
