import streamlit as st
import pandas as pd

from bloom_filter import BloomFilter
from hyper_log_log import HyperLogLogEstimator

TITLE = 'Stream Mining'

st.set_page_config(page_title=TITLE, page_icon="🎓")
st.caption(TITLE)
st.title(TITLE)

st.write("""
# Bloom Filter & HyperLogLog
Apply the concepts of a Bloom Filter and HyperLogLog algorithm to a data set.
""")

# Read data and visualize it
data = pd.read_csv('data/diabetic_data.csv')
data_frame = pd.DataFrame(data)
st.header('Diabetic data')
st.write(data_frame)

# 1. Task: Check if an id is in the data set with a Bloom Filter
# extract unique IDs from column 'encounter_id'
encounter_ids = data['encounter_id'].unique()
st.write('Number of encounter_ids:', len(encounter_ids))

# create Bloom Filter
st.header('Bloom Filter')
# create slider to choose the filter length of the Bloom Filter
filter_length_slider = st.slider('Choose the filter length', 1, len(encounter_ids), 1)
# insert integer number to check
number_to_check = st.number_input('Insert a number to check if it is in the Bloom Filter.', value=0)

# create Bloom Filter and check if number_to_check is in the Bloom Filter
bloom_filter = BloomFilter(filter_length_slider, encounter_ids)
st.write("Is", number_to_check, "in the Bloom Filter?", bloom_filter.is_in_filter(number_to_check))

# 2. Task: Use HyperLogLog algorithm on a column of data to get the number of unique items
st.header('HyperLogLog algorithm')

# select column name from a list
column_name = st.selectbox('Select a column.', data.columns)
column_data = data[column_name]

# show estimated unique number (HyperLogLog algorithm)
fm_estimator = HyperLogLogEstimator(column_data)
st.write('Estimated Number of unique values:', fm_estimator.calculate_estimate())

# get real number unique values from column_name
real_unique_values = column_data.nunique()
st.write('Real Number of unique values:', real_unique_values)
