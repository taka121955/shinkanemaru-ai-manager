# 仮の統計データ（実際はCSVやSheetsから取得）
win_rate = 58.3
hit_rate = 41.7
recovery_rate = 112.4

# 2列表示で資金情報と統計情報を並べて表示
st.markdown(
    f"""
    <div style='display: flex; justify-content: space-between;'>
        <div style='width: 48%; font-size: 20px;'>
            🎯 <b>目標金額：</b><span style='color:blue;'>{funds['target']:,}円</span><br>
            💼 <b>準備金額：</b><span style='color:green;'>{funds['reserve']:,}円</span><br>
            📦 <b>積立金額：</b><span style='color:orange;'>{funds['savings']:,}円</span>
        </div>
        <div style='width: 48%; font-size: 20px;'>
            📈 <b>勝率：</b><span style='color:green;'>{win_rate:.1f}%</span><br>
            🎯 <b>的中率：</b><span style='color:orange;'>{hit_rate:.1f}%</span><br>
            💸 <b>回収率：</b><span style='color:red;'>{recovery_rate:.1f}%</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
