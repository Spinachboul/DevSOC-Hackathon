import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('match_options.csv')  # Replace 'your_dataset.csv' with your actual dataset file

# Streamlit app
st.title("Player Availability")
st.markdown("Enter your preferences:")
sport = st.selectbox("Sport of Interest", df['Sport of Interest'].unique())
skill_level = st.selectbox("Skill Level", ['beginner', 'Intermediate', 'Advanced'])
age_range = st.slider("Age Range", min_value=18, max_value=60, value=(18, 30))
location = st.text_input("Location")
availability = st.selectbox("Availability", df['Availability'].unique())
playing_style = st.selectbox("Preferred Playing Style", df['Preferred Playing Style'].unique())
fitness_level = st.selectbox("Fitness Level", df['Fitness Level'].unique())
gender = st.selectbox("Gender", df['Gender'].unique())
interests = st.text_input("Interests and Hobbies")
ratings = st.slider("Rating", min_value=100, max_value=10000, value=(100, 300))


# Filter the dataset based on the preferences
filtered_df = df[
    (df['Sport of Interest'] == sport) &
    (df['Skill Level'] == skill_level) &
    (df['Age Range'].between(age_range[0], age_range[1])) &
    (df['Location'].str.contains(location, case=False)) &
    (df['Availability'] == availability) &
    (df['Preferred Playing Style'] == playing_style) &
    (df['Fitness Level'] == fitness_level) &
    (df['Gender'] == gender) &
    (df['Interests and Hobbies'].str.contains(interests, case=False))
]

# Display the results
if len(filtered_df) > 0:
    st.success(f"There are {len(filtered_df)} players available for the given preferences.")
    st.table(filtered_df)
else:
    st.warning("No players found for the given preferences.")


