import streamlit as st
import plotly_express as px
import pandas as pd
import numpy as np
import io
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Employee Insights Dashboard!!!", page_icon=":bar_chart:",layout="wide")
st.title(" :bar_chart: Employee Insights Dashboard")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)




uploaded_file = st.file_uploader("Select a file", type=["csv", "txt", "xlsx", "xls"])

if uploaded_file is not None:
    st.sidebar.success("File uploaded successfully!")

    # Display some information about the uploaded file
    st.subheader("Uploaded File Information:")
 

    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)  # You can modify this based on the file 
else:
    st.warning("Please upload a CSV or Excel file.")

st.sidebar.header("Filters")

all_names = ['All'] + list(df['Gender'].unique())
selected_name = st.sidebar.selectbox("Select Gender", all_names, index=0)
if selected_name != 'All':
    filtered_df = df[df['Gender'] == selected_name]
else:
    filtered_df = df


all_workmode= ['All'] + list(filtered_df['Primary Skills'].unique())
selected_gender1 = st.sidebar.selectbox("Select Primary Skills", all_workmode, index=0)
if selected_gender1 != 'All':
    filtered_df = filtered_df[filtered_df['Primary Skills'] == selected_gender1]

all_workmode1= ['All'] + list(filtered_df['Willing to go to Blore office'].unique())
selected_gender = st.sidebar.selectbox("Select Willing to go to Blore office", all_workmode1, index=0)
if selected_gender != 'All':
    filtered_df = filtered_df[filtered_df['Willing to go to Blore office'] == selected_gender]


# Filter data based on selected category
df88 = filtered_df
df8899 = df88["Willing to go to Blore office"]
category_df1=df88["Willing to go to Blore office"]
category_df3=df88[["Willing to go to Blore office","Designation"]]
MMA=df["Unit (DU/CU/Bench)"].value_counts()
category_df4=df88[["Willing to go to Blore office","Unit (DU/CU/Bench)"]]
category_df5=df88[["Willing to go to Blore office","Primary Skills"]]
category_df6=df88[["Willing to go to Blore office","Secondary Skills"]]
category_df7=df88[["Willing to go to Blore office","Work mode (WFH / WFO / WFCO / Hybrid)"]]


numeric_value1=round(df88["Total years of experience"].mean(),2)
numeric_value2=df88["Total years of experience"].max()
numeric_value3=df88["Total years of experience"].min()
df3=df88.loc[df88["Gender"]=="Male"]
df31=df88.loc[df88["Gender"]=="Female"]
numeric_value343=round(df3["Total years of experience"].mean(),2)
numeric_value22895=df31["Total years of experience"].mean()
df3874=df88.loc[df88["Total years of experience"]>df88["Total years of experience"].mean()]
df34414=df88.loc[df88["Total years of experience"]<df88["Total years of experience"].mean()]
numeric_value34887=len(df3874)
numeric_value228957=len(df34414)


st.write("Total Tenure in Doodblue Analysis")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Experience Average", value=numeric_value1)
with col2:
    st.metric(label="Total Experience Max", value=numeric_value2)
with col3:
    st.metric(label="Total Experience Min", value=numeric_value3)
col4,col5,col6,col7 = st.columns(4)
with col4:
    st.metric(label="Avg Experience Male", value=numeric_value343)
with col5:
    st.metric(label="Avg Experience Female", value=numeric_value22895)
with col6:
    st.metric(label="No. Of Employee having Experience greater than the average", value=numeric_value34887)
with col7:
    st.metric(label="No. Of Employee having Experience lesser than the average", value=numeric_value228957)
numeric_value11=round(df88["Tenure in doodleblue"].mean(),2)
numeric_value22=df88["Tenure in doodleblue"].max()
numeric_value33=df88["Tenure in doodleblue"].min()
df3=df88.loc[df88["Gender"]=="Male"]
df31=df88.loc[df88["Gender"]=="Female"]
numeric_value34=round(df3["Tenure in doodleblue"].mean(),2)
numeric_value2289=df31["Tenure in doodleblue"].mean()
df387=df88.loc[df88["Tenure in doodleblue"]>df88["Tenure in doodleblue"].mean()]
df3441=df88.loc[df88["Tenure in doodleblue"]<df88["Tenure in doodleblue"].mean()]
numeric_value3488=len(df387)
numeric_value22895=len(df3441)


st.write("Total Tenure Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Tenure Average", value=numeric_value11)
with col2:
    st.metric(label="Total Tenure Max", value=numeric_value22)
with col3:
    st.metric(label="Total Tenure Min", value=numeric_value33)
col4,col5,col6,col7 = st.columns(4)
with col4:
    st.metric(label="Avg Tenure Male", value=numeric_value34)
with col5:
    st.metric(label="Avg Tenure Female", value=numeric_value2289)
with col6:
    st.metric(label="No. Of Employee having tenure greater than the average", value=numeric_value3488)
with col7:
    st.metric(label="No. Of Employee having tenure lesser than the average", value=numeric_value22895)


st.subheader("People willing to go to Banglore")
fig = px.histogram(df8899, x=df8899,color_discrete_sequence=[ 'blue'],title=" Histogram of People Willing to move to Banglore")
st.plotly_chart(fig,use_container_width=True, height = 200)



st.subheader("Designation wise Relocation")
fig = px.histogram(category_df3, x=category_df3["Designation"], color="Willing to go to Blore office", title=" Bar Chart Analysis vs Designation")
st.plotly_chart(fig,use_container_width=True)


st.subheader("Current Work Status wise Relocation")
fig = px.histogram(category_df4, x=category_df4["Unit (DU/CU/Bench)"], color="Willing to go to Blore office", title=" Bar Chart Analysis vs Current Status")
st.plotly_chart(fig,use_container_width=True)

st.subheader("Primary Skill wise Relocation")
fig = px.histogram(category_df5, x=category_df5["Primary Skills"], color="Willing to go to Blore office", title=" Bar Chart Analysis vs Primary Skill")
st.plotly_chart(fig,use_container_width=True)

st.subheader("Secondary Skill wise Relocation")
fig = px.histogram(category_df6, x=category_df6["Secondary Skills"], color="Willing to go to Blore office", title=" Bar Chart Analysis vs Secondary Skills")
st.plotly_chart(fig,use_container_width=True)

st.subheader("Work Mode wise Relocation")
fig = px.histogram(category_df7, x=category_df7["Work mode (WFH / WFO / WFCO / Hybrid)"], color="Willing to go to Blore office", title=" Bar Chart Analysis vs Work Mode")
st.plotly_chart(fig,use_container_width=True)
