import streamlit as st
import pandas as pd
from pathlib import Path
import seaborn as sns

def make_plot(df):
	non_numeric_columns = df.select_dtypes(include='object').columns.tolist()
	color_by = [None] + non_numeric_columns
	color_selected = st.sidebar.selectbox("Color By", color_by)
	pair_plot(df, color_selected)

def pair_plot(df, hue=None):
	st.header("Pair Plot")
	fig = sns.pairplot(df, hue=hue)
	st.pyplot(fig)


with st.sidebar:    
	st.sidebar.title("Problem 2: Pair Plot")
	st.sidebar.markdown("Application to explore the numerical columns as a pair plot.")

	root = Path("examples")
	paths = {f.name: f for f in sorted(root.glob("*.csv"))}
	st.sidebar.header("Select a Dataset")
	options = ["Upload New Dataset"] + list(paths.keys())
	path = st.selectbox("Select a dataset", options)


if path == "Upload New Dataset":
	st.header("Upload a New Dataset")
	uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

	if uploaded_file:
		df = pd.read_csv(uploaded_file)
		make_plot(df)

else:
	df = pd.read_csv(root.joinpath(path))
	make_plot(df)