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

all_names = ['All'] + list(df['Willing to go to Blore office'].unique())
selected_name = st.sidebar.selectbox("Select Willing to go to Blore office", all_names, index=0)
if selected_name != 'All':
    filtered_df = df[df['Willing to go to Blore office'] == selected_name]
else:
    filtered_df = df

all_workmode1= ['All'] + list(filtered_df['Gender'].unique())
selected_gender = st.sidebar.selectbox("Select Gender", all_workmode1, index=0)
if selected_gender != 'All':
    filtered_df = filtered_df[filtered_df['Gender'] == selected_gender]

all_workmode= ['All'] + list(filtered_df['Primary Skills'].unique())
selected_gender1 = st.sidebar.selectbox("Select Primary Skills", all_workmode, index=0)
if selected_gender1 != 'All':
    filtered_df = filtered_df[filtered_df['Primary Skills'] == selected_gender1]


# Filter data based on selected category
df88 = filtered_df
df8899 = df88["Willing to go to Blore office"]
category_df1=df88["Willing to go to Blore office"]
category_df3=df88[["Willing to go to Blore office","Designation"]]
MMA=df88["Unit (DU/CU/Bench)"].value_counts().reset_index()
MMA.columns = ['Unit', 'Count']
MMA1=df88["Willing to go to Blore office"].value_counts().reset_index()
MMA1.columns = ['Willing to go to Blore office', 'Count']
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
numeric_value1444=len(df88)

st.write("")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Total Employee Count", value=numeric_value1444)


st.write("Total Overall Experience Analysis")
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
    st.metric(label="No. Of Employee having Experience > average", value=numeric_value34887)
with col7:
    st.metric(label="No. Of Employee having Experience < average", value=numeric_value228957)
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
df333=df88.loc[df88["Willing to go to Blore office"]=="No"]
df3133=df88.loc[df88["Willing to go to Blore office"]=="Yes"]
numeric_value348845=round(len(df333)/len(df88),2)
numeric_value2289545=round(len(df3133)/len(df88),2)


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
    st.metric(label="No. Of Employee having tenure > average", value=numeric_value3488)
with col7:
    st.metric(label="No. Of Employee having tenure < average", value=numeric_value22895)

st.write("Total Movement Analysis")
col1, col2= st.columns(2)
with col1:
    st.metric(label="Total Movement Ratio for Yes", value=numeric_value348845)
with col2:
    st.metric(label="Total Movement Ratio for No", value=numeric_value2289545)

df324=df88.sort_values(by='Tenure in doodleblue', ascending=False)
df345=df324.head(3)
df444=df345[["Employee Name","Tenure in doodleblue"]]


fig = px.histogram(df444, x='Employee Name', y='Tenure in doodleblue', title="Top 3 Tenured Employee")
st.plotly_chart(fig,use_container_width=True)


fig = px.pie(MMA1, names='Willing to go to Blore office', values='Count', title="Willing to go to Blore office")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df3, x=category_df3["Designation"], title="Designation wise distribution")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df3, x=category_df3["Designation"], color="Willing to go to Blore office", title="Designation wise relocation")
st.plotly_chart(fig,use_container_width=True)


fig = px.histogram(category_df4, x=category_df4["Unit (DU/CU/Bench)"], title="Current Unit wise distribution")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df4, x=category_df4["Unit (DU/CU/Bench)"], color="Willing to go to Blore office", title="Current Unit wise relocation")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df5, x=category_df5["Primary Skills"], title="Primary Skill wise distribution")
st.plotly_chart(fig,use_container_width=True)


fig = px.histogram(category_df5, x=category_df5["Primary Skills"], color="Willing to go to Blore office", title="Primary Skill wise relocation")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df6, x=category_df6["Secondary Skills"], title="Secondary Skill wise distribution")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df6, x=category_df6["Secondary Skills"], color="Willing to go to Blore office", title="Secondary Skill wise relocation")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df7, x=category_df7["Work mode (WFH / WFO / WFCO / Hybrid)"], title="Work Mode wise distribution")
st.plotly_chart(fig,use_container_width=True)

fig = px.histogram(category_df7, x=category_df7["Work mode (WFH / WFO / WFCO / Hybrid)"], color="Willing to go to Blore office", title="Work Mode wise relocation")
st.plotly_chart(fig,use_container_width=True)

