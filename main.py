st.markdown("""
<style>
.stat-container {
  display: flex;
  justify-content: space-between;
  font-size: 18px;
  font-weight: bold;
}
.left, .right {
  width: 48%;
}
</style>

<div class="stat-container">
  <div class="left">
    🎯 目標金額：<span style='color:blue;'>-- 円</span><br>
    💼 準備金額：<span style='color:green;'>-- 円</span><br>
    📦 積立金額：<span style='color:orange;'>-- 円</span>
  </div>
  <div class="right">
    📈 勝率：<span style='color:blue;'>--%</span><br>
    🎯 的中率：<span style='color:green;'>--%</span><br>
    💹 回収率：<span style='color:orange;'>--%</span>
  </div>
</div>
""", unsafe_allow_html=True)
