import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import pandas as pd

if 'bot_probabilty_weight' not in st.session_state:
    st.session_state['bot_probabilty_weight'] = 0
if 'general_risk_probabilty' not in st.session_state:
    st.session_state['general_risk_probabilty'] = 0
if 'submit_now' not in st.session_state:
    st.session_state['submit_now'] = False
if 'real' not in st.session_state:
    st.session_state['real'] = 0
if 'suspicious' not in st.session_state:
    st.session_state['suspicious'] = 0
if 'fake' not in st.session_state:
    st.session_state['fake'] = 0
if 'zerofake_score' not in st.session_state:
    st.session_state['zerofake_score'] = 0

submit = st.button('SUBMIT!')

# Original array
def weight_average(array, weights):
    result = np.average(array, weights=weights)
    result = np.round(result, 4)
    return result

if submit:
    st.session_state['submit_now'] = True
if st.session_state['submit_now']:
    st.subheader('GRAPH')
    #creating a sample array
    a = np.array([st.session_state['bot_probabilty_weight'], st.session_state['general_risk_probabilty']])
    #specifying the figure to plot 
    fig, ax = plt.subplots(figsize=(8,4), facecolor='w')
    ax.hist(a, bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    ax.axvline(st.session_state['real'], color='g', linewidth=7.0)
    ax.axvline(st.session_state['suspicious'], color='orange', linewidth=5.0)
    #plotting the figure
    st.pyplot(fig)

    zerofake_score = np.round(0.33*st.session_state['bot_probabilty_weight'] + 0.33*st.session_state['general_risk_probabilty'], 4)
    st.session_state['zerofake_score'] = zerofake_score

with st.container():
    st.subheader('Fake User Thresholds')
    thres_col1, thres_col2, thres_col3 = st.columns([1,1,1])
    real = thres_col1.slider('Real', min_value=0, max_value=100, value=70)
    st.session_state['real'] = real/100
    suspicious = thres_col2.slider('Suspicious', min_value=0, max_value=100, value=85)
    st.session_state['suspicious'] = suspicious/100
    #fake = thres_col3.slider('Fake', min_value=0, max_value=100, value=100)
    #st.session_state['fake'] = fake/100

with st.container():
    st.subheader('Bot Probability')
    bot_col1, bot_col2, bot_col3 = st.columns([1,1,1])
    data_center = bot_col1.slider('Data Center', min_value=0, max_value=100)
    bot_behavior = bot_col2.slider('Bot Behavior', min_value=0, max_value=100)
    network_detection = bot_col3.slider('Network Detection', min_value=0, max_value=100)

if st.session_state['submit_now']:
    weights = np.array([0.33, 0.33, 0.33])
    array = np.array([data_center/100, bot_behavior/100, network_detection/100])
    bot_probabilty_weight = weight_average(array, weights)
    st.session_state['bot_probabilty_weight'] = bot_probabilty_weight
    st.write(st.session_state['bot_probabilty_weight'])

with st.container():
    st.subheader('General Risk Probability')
    geo_col1, geo_col2, geo_col3 = st.columns([1,1,1])
    unique_regions = geo_col1.slider('Unique Regions', min_value=0, max_value=100)
    impossible_travel = geo_col2.slider('Impossible Travel', min_value=0, max_value=100)
    forbidden_geographies = geo_col3.slider('Forbidden Geographies', min_value=0, max_value=100)
    device_col1, device_col2 = st.columns([1,1])
    unique_devices = device_col1.slider('Unique Devices', min_value=0, max_value=100)
    emulator_vm = device_col2.slider('Emulator / VM', min_value=0, max_value=100)
    network_col1, network_col2, network_col3 = st.columns([1,1,1])
    proxy_ip = network_col1.slider('Proxy IP', min_value=0, max_value=100)
    vpn = network_col2.slider('VPN', min_value=0, max_value=100)
    tor = network_col3.slider('TOR', min_value=0, max_value=100)
    con_col1, con_col2 = st.columns([1,1])
    consortium_risk = device_col1.slider('Consortium Risk', min_value=0, max_value=100)
    lie_detection = device_col2.slider('Lie Detection', min_value=0, max_value=100)

if st.session_state['submit_now']:
    weights = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    array = np.array([unique_regions/100, impossible_travel/100, forbidden_geographies/100,
                        unique_devices/100, emulator_vm/100, proxy_ip/100, vpn/100, tor/100,
                        consortium_risk/100, lie_detection/100])
    gr_probabilty_weight = weight_average(array, weights)
    st.session_state['general_risk_probabilty'] = gr_probabilty_weight
    st.write(st.session_state['general_risk_probabilty'])

with st.container():
    st.subheader('Multi-Accounting')
    st.text_input('Number of accounts')
    

item = {
    'Account': 1,
    'ZeroFake Score': st.session_state['zerofake_score'],
    'Bot Probability': st.session_state['bot_probabilty_weight'],
    'Mult-accounting Probability': 1,
    'General Risk Propability': st.session_state['general_risk_probabilty']
}
with st.container():
    st.subheader('Data')
    df = pd.DataFrame(item, index=[0])
    st.dataframe(df)


