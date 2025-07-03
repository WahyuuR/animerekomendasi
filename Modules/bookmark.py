import mysql.connector
import streamlit as st
from Modules.db_config import DB_CONFIG

def add_bookmark(title):
    username = st.session_state['username']
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()
    c.execute("INSERT INTO bookmarks (username, title) VALUES (%s, %s)", (username, title))
    conn.commit()
    conn.close()
    st.success(f"{title} berhasil ditambahkan ke bookmark!")

def get_bookmarks():
    username = st.session_state['username']
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()
    c.execute("SELECT title FROM bookmarks WHERE username = %s", (username,))
    bookmarks = [row[0] for row in c.fetchall()]
    conn.close()
    return bookmarks

def remove_multiple_bookmarks(titles):
    username = st.session_state['username']
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()
    for title in titles:
        c.execute("DELETE FROM bookmarks WHERE username = %s AND title = %s", (username, title))
    conn.commit()
    conn.close()
    st.success(f"Berhasil menghapus {len(titles)} bookmark.")
