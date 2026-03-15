import streamlit as st
from common import gradient_line, connect_to_codex_collections
from streamlit_option_menu import option_menu
from dialogs import add_website, delete_website, settings_website, scraping_website


def websites():
    st.title("Website Collection", help="This page allows you to manage and monitor your websites.")
    gradient_line()

    cols = st.columns([1, 1, 1, 1])
    with cols[0]:
        count = connect_to_codex_collections('websites').count_documents({})
        st.markdown(f'### Enrolled Websites: {count}')

    with cols[-1]:
        if st.button("➕Add", key="add_website_button", width='stretch'):
            add_website()

        website_names = [website['name'] for website in connect_to_codex_collections('websites').find()]
        
    cols = st.columns(4)
    for i, site in enumerate(website_names):
        with cols[i % 4]:
            with st.container(border=True):
                website_status = connect_to_codex_collections('websites').find_one({'name': site})['status']
                website_subscription = connect_to_codex_collections('websites').find_one({'name': site})['subscription']

                if website_status == 'Active':
                    website_status = ':green[Active]'
                elif website_status == 'Inactive':
                    website_status = ':red[Inactive]'
                
                if website_subscription == 'Free':
                    website_subscription = ':green[Free]'
                elif website_subscription == 'Paid':
                    website_subscription = ':blue[Paid]'


                st.subheader(site)
                st.write(f'Status: {website_status}')
                st.write(f'Subscription: {website_subscription}')

                sub_cols = st.columns([1, 1, 1])
                with sub_cols[0]:
                    if website_status == ':green[Active]':   
                        if st.button("Scrape", key=f"scrape_{site}", width='stretch'):
                            scraping_website(site)
                with sub_cols[1]:
                    if st.button("Settings", key=f"settings_{site}", width='stretch'):
                        settings_website(site)
                with sub_cols[-1]:
                    if st.button("Delete", key=f"delete_{site}", width='stretch'):
                        delete_website(site)

    



    