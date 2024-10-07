import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.ticker as mtick


def format_axis(ax):

    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))

def visualize_data(df):

    st.title(":bar_chart: Data Visualization")

    st.header("Sample")
    st.dataframe(df.sample(20))

    selected_columns = st.multiselect('Select column for visualization:', df.columns)




    visualization_options = ['Scatter Plot', 'Bar Chart', 'Histogram']

    chosen_visualization = st.selectbox('Choose a visualization:', visualization_options)

    if chosen_visualization == 'Scatter Plot':
        if len(selected_columns) >= 2:
            x_axis = st.selectbox('X-axis:', selected_columns)
            y_axis = st.selectbox('Y-axis:', selected_columns)

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.scatterplot(x=x_axis, y=y_axis, data=df)
            st.pyplot(fig)
        elif len(selected_columns) == 1:
            st.warning("Scatter plot requires at least two variables.")


    elif chosen_visualization == 'Bar Chart' or chosen_visualization == 'Histogram':
        if len(selected_columns) >= 2:
            x_axis = st.selectbox('X-axis:', selected_columns)
            y_axis = st.selectbox('Y-axis:', selected_columns)

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=x_axis, y=y_axis, data=df)
            st.pyplot(fig)

        elif len(selected_columns) == 1:
            x_axis = selected_columns[0]
            freq_count = df[x_axis].value_counts()

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(x=freq_count.index, y=freq_count.values, ax=ax)
            st.pyplot(fig)
        else:
            st.warning("Please select at least one column.")

    st.header("Heatmap")

    selected_features = st.multiselect("select some features:", df.columns)

    if len(selected_features) > 0:
        features = df[selected_features]
        fig, ax = plt.subplots(figsize=(15, 5))
        sns.heatmap(features.corr(), annot=True, cmap='coolwarm', square=True)
        st.pyplot(fig)
    else:
        st.warning("Please select at least one feature.")



if 'df_cleaned' not in st.session_state:
    st.error("No cleaned dataset found.")
else:
    df = st.session_state.df_cleaned
    visualize_data(df)