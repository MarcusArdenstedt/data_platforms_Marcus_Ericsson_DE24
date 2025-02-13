import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
from load_data import load_data
from charts import line_chart

count = st_autorefresh(interval=10 * 1000, limit= 100, key="data_refresh")

def layout():
    df = load_data("SELECT * FROM etherium;")
    
    st.markdown("# Coin data")
    st.markdown("This will display live data from coinmarket API")
    
    st.markdown("latest data")
    
    st.dataframe(df.tail())
    
    st.markdown("## Latest price in USD for etherium")
    price_chart = line_chart(x= df.index, y= df["price_usd"], title= "price USD")
    st.pyplot(price_chart)
    
if __name__=='__main__':
    layout()