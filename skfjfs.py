
import streamlit as st
import pygame as pyg
import random
pyg.mixer.init()
st.title("セキュリティアプリ")
st.download_button(
    label="コードをダウンロード",
    data="06032511E",
    file_name="password.txt",
    mime="text/plain"
)
codes=st.text_input("コードを入力")
if codes=="06032511E":
    
    if not "names" in st.session_state:
        st.session_state.names=""
    name=st.text_input("名前を入力")
    st.session_state.names=name
    if not "bal" in st.session_state:
        st.session_state.bal=""
    if name:
        if st.session_state.names=="verity":
            pyg.mixer.music.load("[Verity]俺のこと下......呼ばないで.mp3")
            pyg.mixer.music.play()
        else:
            
            if st.session_state.bal=="":
                st.balloons()
            st.text("サインイン成功！")
            st.session_state.bal="inst"
            st.write(f"ようこそ！{st.session_state.names}さん！")
            st.subheader("軽いゲームをしましょう！")
            if not "mikuji" in st.session_state:
                st.session_state.mikuji=["大吉","中吉","小吉","吉","凶"]
            if st.button("おみくじ"):
                st.write(st.session_state.mikuji[random.randint(0,4)])
            