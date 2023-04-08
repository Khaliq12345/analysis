import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

if 'bot_probabilty_weight' not in st.session_state:
    st.session_state['bot_probabilty_weight'] = False
if 'general_risk_probabilty' not in st.session_state:
    st.session_state['general_risk_probabilty'] = False

# Original array
def weight_average(array, weights):
    result = np.average(array, weights=weights)
    result = np.round(result, 4)
    return result

with st.container():
    st.subheader('Bot Probability')
    bot_col1, bot_col2, bot_col3 = st.columns([1,1,1])
    data_center = bot_col1.slider('Data Center', min_value=0, max_value=100)
    bot_behavior = bot_col2.slider('Bot Behavior', min_value=0, max_value=100)
    network_detection = bot_col3.slider('Network Detection', min_value=0, max_value=100)

if st.session_state['bot_probabilty_weight']:
    weights = np.array([0.33, 0.33, 0.33])
    array = np.array([data_center/100, bot_behavior/100, network_detection/100])
    bot_probabilty_weight = weight_average(array, weights)
    st.write(bot_probabilty_weight)

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

if st.session_state['general_risk_probabilty']:
    weights = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    array = np.array([unique_regions/100, impossible_travel/100, forbidden_geographies/100,
                        unique_devices/100, emulator_vm/100, proxy_ip/100, vpn/100, tor/100,
                        consortium_risk/100, lie_detection/100])
    gr_probabilty_weight = weight_average(array, weights)
    st.write(gr_probabilty_weight)

with st.container():
    st.subheader('Multi-Accounting')
    st.text_input('Number of accounts')


submit = st.button('Analyse!')
if submit:
    st.session_state['bot_probabilty_weight'] = True
    st.session_state['general_risk_probabilty'] = True
    #creating a sample array
    a = np.array([bot_probabilty_weight, gr_probabilty_weight])
    #specifying the figure to plot 
    fig, ax = plt.subplots(figsize =(10, 7))
    ax.hist(a, bins = [0, 0.25, 0.5, 0.7, 0.85, 1])
    #plotting the figure
    st.pyplot(fig)




