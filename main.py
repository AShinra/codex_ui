import streamlit as st
from streamlit_option_menu import option_menu
from home import home
from websites import websites

if __name__ == "__main__":
    
    hide_streamlit_style = """<style>
    ._profileContainer_gzau3_63{display: none;}
    </style>"""
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)    

    st.set_page_config(
        layout="wide",
        page_title='CODEX')
    
    # hide streamlit toolbar
    st.markdown("""<style>[data-testid="stToolbar"] {display: none;}</style>""", unsafe_allow_html=True)
    st.markdown("""<style>[data-testid="manage-app-button"] {display: none !important;}</style>""", unsafe_allow_html=True)
    st.markdown("""<style>[data-testid="stSidebarCollapseButton"] {display: none !important;}</style>""", unsafe_allow_html=True)
    st.markdown("""<style>[data-testid="stSidebarHeader"] {height: 1rem;}</style>""", unsafe_allow_html=True)
    st.markdown("""<style>.stSidebar.st-emotion-cache-1legitb {background-color: black;}</style>""", unsafe_allow_html=True)

    with st.sidebar:

        selected_option = option_menu(
            menu_title="Menu",
            options=["Home", "Websites", "About", "Contact"],
            icons=["house", "globe", "info-circle", "envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical")
    
    if selected_option == "Home":
        home()
    elif selected_option == "Websites":
        websites()


    