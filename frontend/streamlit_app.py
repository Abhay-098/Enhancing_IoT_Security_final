import streamlit as st
import requests, json

st.set_page_config(page_title='Server-Client Demo with Backend', layout='wide')

BACKEND = st.text_input('Backend URL (include https:// or http://)', value='http://localhost:5000')
if BACKEND.endswith('/'):
    BACKEND = BACKEND[:-1]

st.title('Server ↔ Client Demo with Persistent Backend (Secure & Insecure)')

col1, col2 = st.columns([2,1])
with col2:
    st.header('Certificates')
    name = st.text_input('New cert name', value='deviceA')
    if st.button('Generate cert'):
        r = requests.post(BACKEND + '/generate_cert', json={'name':name})
        st.write(r.json())
    if st.button('List certs'):
        r = requests.get(BACKEND + '/certs')
        st.write(r.json())

with col1:
    st.header('Sender (Server)')
    topic = st.text_input('Topic', value='iot/device/data')
    payload = st.text_input('Message', value='Temperature=26.5')
    mode = st.selectbox('Mode', ['insecure','secure'], index=1)
    try:
        certs = requests.get(BACKEND + '/certs').json()
    except Exception:
        st.error('Backend not reachable. Check URL.')
        certs = []
    cert_names = [''] + [c['name'] for c in certs]
    cert_name = st.selectbox('Certificate (for secure send)', cert_names, index=1)
    if st.button('Send message'):
        data = {'topic':topic,'payload':payload,'mode':mode,'cert_name':cert_name}
        r = requests.post(BACKEND + '/send', json=data)
        st.write(r.json())

    st.header('Receiver (Client)')
    limit = st.number_input('Messages to fetch', value=10, min_value=1, max_value=100)
    if st.button('Fetch messages'):
        r = requests.get(BACKEND + f'/messages?limit={limit}')
        msgs = r.json()
        st.session_state['msgs'] = msgs
    msgs = st.session_state.get('msgs', [])
    for m in msgs:
        st.subheader(f"{m['topic']} — {m['mode']} — {m['ts']}")
        st.code(m['wire'][:200])
        if m['mode'] == 'secure':
            sel = st.selectbox(f"Use cert to decrypt (msg {m['id']})", [''] + [c['name'] for c in certs], key=f"dec_{m['id']}")
            if st.button('Attempt decrypt', key=f'decbtn_{m['id']}'):
                r = requests.post(BACKEND + '/decrypt', json={'cert_name':sel,'wire':m['wire']})
                st.write(r.json())
        else:
            st.write('Plaintext message:')
            st.code(m['payload'])
