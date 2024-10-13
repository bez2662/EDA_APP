import pandas as pd
import streamlit as st
from io import StringIO


st.set_page_config(page_title = 'EDA', page_icon= "bar_chart", layout='wide')

st.title(':bar_chart: EDA')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)


def clean_data(df):
    df_cleaned = df.dropna()
    df_cleaned = df_cleaned.drop_duplicates()

    return df_cleaned

fl = st.file_uploader(':file_folder: Upload a file', type="csv")
if fl is not None:
    try:
        file_contents = fl.getvalue().decode('utf-8')
        s = StringIO(file_contents)
        df = pd.read_csv(s, encoding='ISO-8859-1')

    except Exception as e:
        st.error(f"Error processing the file: {str(e)}")

    if not df.empty:
        st.header("Sample")
        st.dataframe(df.sample(20))

        st.header("Dataset Information")
        st.write(f"Shape: {df.shape}")
        st.write(f"Columns: {len(df.columns)}")
        st.write(f"Rows: {len(df)}")

        col1,col2,col3 = st.columns(3)
        with col1:
            st.text("Stats")
            st.write(df.describe())
        with col2:
            st.text("Unique values:")
            st.write(df.nunique())
        with col3:
            st.text("Null value count:")
            st.write(df.isnull().sum())

        if st.button('Clean Dataset'):
            df_cleaned = clean_data(df)
            st.header("Cleaned DataFrame")
            st.dataframe(df_cleaned.head(10))
            st.write(f"Shape: {df_cleaned.shape}")

            st.session_state.df_cleaned = df_cleaned


    else:
        st.error("No data available.")

else:
    st.write('no file is selected')

