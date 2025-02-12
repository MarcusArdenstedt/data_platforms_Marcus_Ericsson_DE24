from read_data import read_data
import duckdb
import streamlit as st 


def approved_by_data_area_bar():
    df = read_data()

    df = duckdb.query(""" SELECT 
                    utbildningsområde, COUNT(*) AS Beviljad 
                    FROM 
                        df
                    WHERE 
                        beslut = 'Beviljad'
                    GROUP BY 
                        utbildningsområde
                    ORDER BY
                        Beviljad
                    DESC
                    """).df()

    st.bar_chart(df, x= "Utbildningsområde", y= "Beviljad")
