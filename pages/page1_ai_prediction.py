import streamlit as st
import pandas as pd
from datetime import datetime

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")
    st.title("① AI予想")

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    try:
        csv_url = "https://docs

すみません、途中で途切れてしまいました。  
こちらが、**修正済みの `page1_ai_prediction.py`** の完全なコードです（`gspread` を使わず、**CSV URLから直接読み込む方式**に修正しています）。

---

### ✅ `page1_ai_prediction.py`（Streamlit Cloud対応・gspread無し）

```python
import streamlit as st
import pandas as pd
from datetime import datetime

def show_page():
    st.set_page_config(page_title="① AI予想", layout="centered")
    st.title("① AI予想")

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    st.markdown(f"🕒 現在時刻（日本時間）： `{now}`")

    try:
        # ✅ スプレッドシート（シート2）からCSVで取得
        csv_url = "https://docs.google.com/spreadsheets/d/1yfzSSgqA-1x2z-MF7xKnCMbFBJvb-7Kq4c84XSmRROg/export?format=csv&gid=1462109758"
        df = pd.read_csv(csv_url)

        # 的中率を数値化してソート
        df["的中率"] = df["的中率"].str.replace("%", "").astype(float)
        df_sorted = df.sort_values(by="的中率", ascending=False).head(10).reset_index(drop=True)

        # 番号付与（1〜10）
        df_sorted.index += 1
        df_sorted.index.name = "番号"

        # 表示
        st.markdown("### 🎯 本日のAI予想（的中率トップ10）")
        st.table(df_sorted)

    except Exception as e:
        st.error(f"データの取得に失敗しました：{e}")

# 呼び出し
show_page()
