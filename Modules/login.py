import streamlit as st
from Modules.auth import register_user, login_user

import streamlit as st
from Modules.auth import register_user, login_user

def login():
    with st.sidebar:
        st.title("🔑 Login / Register")
        tab = st.radio("Menu", ["Login", "Register"])

        if tab == "Login":
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                success, role = login_user(username, password)
                if success:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.session_state['role'] = role
                    st.success("Login berhasil!")
                else:
                    st.error("Username atau password salah.")

        elif tab == "Register":
            username = st.text_input("Username Baru")
            password = st.text_input("Password Baru", type="password")
            if st.button("Register"):
                if register_user(username, password):
                    st.success("Registrasi berhasil! Silakan login.")
                else:
                    st.error("Username sudah digunakan. Pilih username lain.")


def logout():
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()
