"""
File     : app.py
Date     : 2023.12.23
Author   : Ming-Chang Lee
RWEPA    : http://rwepa.blogspot.tw/
YouTube  : https://www.youtube.com/@alan9956
Email    : alan9956@gmail.com
GitHub   : https://github.com/rwepa
Encoding : UTF-8
"""

# streamlit run app.py
# http://localhost:8501/

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib

# 設定中文字型
# matplotlib.font_manager.fontManager.addfont('SimHei.ttf')

# 設定 matplotlib.rcParams 方法
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 設定負號正確顯示
matplotlib.rcParams['axes.unicode_minus'] = False
# 設定完成

urls = 'https://raw.githubusercontent.com/rwepa/DataDemo/master/faithful.csv'

df = pd.read_csv(urls)
data = df['waiting']
st.markdown("""
<style>
.big-font {
    font-size:30px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p class="big-font">411410168李明昌</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">Hello Streamlit!</p>', unsafe_allow_html=True)
    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider(
        '**透明度**',
        0.0, 1.0, 0.5
    )
    st.write("Required packages:")
    st.markdown('+ streamlit', unsafe_allow_html=True)
    st.markdown('+ matplotlib', unsafe_allow_html=True)
    st.markdown('+ pandas', unsafe_allow_html=True)

# 'Bins selected: ', add_slider

fig, ax = plt.subplots()
# ax.hist(data, bins=add_slider)
ax.scatter(df['eruptions'], df['waiting'], alpha=add_slider) # 散佈圖
ax.set_xlabel('eruptions(分鐘)')
ax.set_ylabel('waiting(分鐘)')
ax.set_title('eruptions vs. waiting 散佈圖 - 411410168李明昌')
# ax.set_title('噴火と待機中の散布図 - 411410168 Li Mingchang')
ax.grid(linewidth=0.6, linestyle="--")

st.pyplot(fig)
# end
