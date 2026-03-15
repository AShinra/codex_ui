import streamlit as st
from common import connect_to_codex_collections
import time

@st.dialog("Add Website")
def add_website():
    
    name = st.text_input(
        label="Website Name",
        label_visibility='collapsed',
        placeholder="Enter the name of the website")
    url = st.text_input(
        label="Website URL",
        label_visibility='collapsed',
        placeholder="Enter the URL of the website")
    
    cols = st.columns([1,2])
    with cols[0]:
        st.write("Subscription Type")
    with cols[1]:
        subscription_type = st.radio(
            label='Subscription Type',
            label_visibility='collapsed',
            options=['Free', 'Paid'],
            index=0, key='subscription_type',
            horizontal=True)
    
    if subscription_type == 'Paid':
        st.warning("Please enter your subscription details for the website.")
        subscription_user = st.text_input(
            label='Subscription Username/Email',
            label_visibility='collapsed',
            placeholder='Enter your subscription username/email',
            key='subscription_user')
        subscription_pass = st.text_input(
            label='Subscription Password',
            label_visibility='collapsed',
            placeholder='Enter your subscription password',
            key='subscription_pass',
            type='password')
    else:
        subscription_user = None
        subscription_pass = None
    
    if name and url:
        if st.button("Add Website", width='stretch'):
            result_name = connect_to_codex_collections('websites').find_one({'name': name})
            result_url = connect_to_codex_collections('websites').find_one({'url': url})
            if result_name==None and result_url==None: 
                with st.spinner("Updating website list..."):
                    st.toast("Adding website to collection")
                    time.sleep(3)
                    connect_to_codex_collections('websites').insert_one({
                        'name': name,
                        'url': url,
                        'status':'Inactive',
                        'subscription': subscription_type,
                        'subscription_user': subscription_user,
                        'subscription_pass': subscription_pass})
                    st.toast(f"{name} added to collection", icon="✅")
                    time.sleep(3)
                    st.toast("Updating website list...")
                    time.sleep(3)
            else:
                st.error("A website with the same name or URL already exists.")
                with st.spinner("Closing dialog..."):
                    time.sleep(2)
            st.rerun()


@st.dialog("Delete Website")
def delete_website(site):
    st.warning(f"Are you sure you want to delete {site}?")
    if st.button("Delete", width='stretch'):
        with st.spinner(f"Deleting {site}..."):
            st.toast(f'Deleting {site}', icon="🗑️")
            time.sleep(3)
            connect_to_codex_collections('websites').delete_one({'name': site})
            st.toast(f'{site} deleted from collection', icon="✅")
            time.sleep(3)
            st.toast('Updating website list...')
            time.sleep(3)
            st.rerun()

@st.dialog("Settings")
def settings_website(site):
    document = connect_to_codex_collections('websites').find_one({'name': site})
    website_name = document['name']
    website_url = document['url']
    current_status = document['status']
    website_subscription = document['subscription']

    if website_subscription=='Paid':
        website_subscription = f':blue[Paid] - details saved'
    else:
        website_subscription = f':green[Free]'

    st.write(f"Website: {website_name}")
    st.write(f"URL: {website_url}")
    st.write(f"Subscription: {website_subscription}")
    website_status = st.radio(
        label="Status",
        options=['Active', 'Inactive'],
        index=0 if current_status=='Active' else 1,
        key=f"status_{site}")
    
    website_sections = st.multiselect(
        label='Section Selection',
        options=['Section Url1', 'Section Url2', 'Section Url3'],
        key=f'section_selection_{site}')
    
    schedule_selection = st.selectbox(
        label='Schedule',
        options=['Hourly','Daily', 'Custom'],
        key=f'schedule_{site}')
    
    

    # cols = st.columns(2, border=True)
    # with cols[0]:
    #     status_selection = st.radio(
    #         label="Status",
    #         options=['Active', 'Inactive'],
    #         index=0 if document['status']=='Active' else 1, key=f"status_{site}")
    # with cols[1]:
    #     subscription_selection = st.radio(
    #     label="Subscription",
    #     options=['Free', 'Paid'],
    #     index=0 if document['subscription']=='Free' else 1, key=f"subscription_{site}")
    
    # if subscription_selection == 'Paid':
        
    #     # check subscription details
    #     result = connect_to_codex_collections('websites').find_one({'name': site})
    #     subscription_user = result['subscription_user']
    #     result = connect_to_codex_collections('websites').find_one({'name': site})
    #     subscription_pass = result['subscription_pass']

    #     if subscription_user in [None, ''] and subscription_pass in [None, '']:
    #         st.warning("No subscription details found. Please add your subscription details.")
    #         sub_user = st.text_input(
    #             label="Username/Email",
    #             label_visibility='collapsed',
    #             placeholder="Username/Email for subscription",
    #             key=f"sub_user")
    #         subs_pass = st.text_input(
    #             label="Password",
    #             label_visibility='collapsed',
    #             placeholder="Password for subscription",
    #             key=f"sub_pass")
            

        # if st.button(
        #     label="Add/Update Subscription Details",
        #     key=f"add_subscription_details_{site}",
        #     width='stretch'):
        #     subscription_username = st.text_input(
        #         label="Username/Email",
        #         label_visibility='collapsed',
        #         placeholder="Username/Email for subscription",
        #         key=f"subscription_details_{site}")
        #     subscription_password = st.text_input(
        #         label="Password",
        #         label_visibility='collapsed',
        #         placeholder="Password for subscription",
        #         key=f"subscription_token_{site}",
        #         type="password")


    # if st.button("Save Settings", width='stretch'):
    #     with st.spinner("Saving settings..."):
    #         st.toast(f'Updating settings of {site}')
    #         time.sleep(3)
            
    #         if subscription_selection=='Paid':
    #             connect_to_codex_collections('websites').update_one(
    #                 {'name': site},
    #                 {'$set': {
    #                     'status': status_selection,
    #                     'subscription': subscription_selection,
    #                     'subscription_username_key': subscription_username,
    #                     'subscription_token_key': subscription_password}})
            
    #         st.toast(f'Settings of {site} updated', icon="✅")
    #         time.sleep(3)
    #         st.write('Updating website list...')
    #         time.sleep(3)
    #         st.rerun()

@st.dialog("Scraping Website")
def scraping_website(site):
    st.write(f"Scraping {site}...")
    with st.spinner("Scraping in progress...", show_time=True):
        st.toast(f'Checking {site}')
        time.sleep(3)
        st.toast('Checking sections')
        time.sleep(3)
        st.toast('Gathering URLS')
        time.sleep(3)
        st.toast('Parsing URL content')
        time.sleep(3)
        st.toast('Saving Data')
        time.sleep(3)
        st.toast(f'Scraping of {site} completed successfully!', icon="✅")
        time.sleep(2)
        st.rerun()
        
