import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In Search for Happiness")
data_x_axis= st.selectbox("Select the Data for X-axis",
                          options=("GDP","Happiness","Generosity"))
data_y_axis=                                 st.selectbox("Select the Data for Y-axis",
                          options=("GDP","Happiness","Generosity"))
st.subheader(f"{data_x_axis} and {data_y_axis}")
df=pd.read_csv("happy.csv")
match data_x_axis:
    case "GDP":
        x_array=df["gdp"]
    case "Happiness":
        x_array=df["happiness"]
    case "Generosity":
        x_array=df["generosity"]
match data_y_axis:
    case "GDP":
        y_array=df["gdp"]
    case "Happiness":
        y_array=df["happiness"]
    case "Generosity":
        y_array=df["generosity"]

figure_1= px.scatter(x=x_array,y=y_array,labels={"x":data_x_axis,"y":data_y_axis})
st.plotly_chart(figure_1)



