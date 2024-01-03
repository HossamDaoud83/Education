import streamlit as st
import pandas as pd
from datetime import timedelta
import io
import base64

# Function to generate a list of all dates when a course takes place
def generate_course_dates(start_date, final_exam_date):
    # Determine if the course is on a weekend or a weekday
    if start_date.weekday() in [4, 5]:  # Friday or Saturday
        delta = timedelta(days=14)
    else:  # Weekdays (Sunday to Thursday)
        delta = timedelta(days=7)

    # Generate the dates
    dates = [start_date]
    while dates[-1] + delta <= final_exam_date:
        dates.append(dates[-1] + delta)

    return dates

# Function to process the uploaded file
def process_file(uploaded_file):
    # Read the Excel file
    timetable_df = pd.read_excel(uploaded_file)

    # Expand timetable into individual course dates
    expanded_timetable = []
    for _, row in timetable_df.iterrows():
        course_dates = generate_course_dates(row['StartDate'], row['FinalExamDate'])
        for date in course_dates:
            expanded_timetable.append([row['Course'], row['Doctor Name'], date])

    # Create a dataframe from the expanded timetable
    expanded_df = pd.DataFrame(expanded_timetable, columns=['Course', 'Doctor Name', 'Course Date'])

    # Checking for conflicts
    grouped_df = expanded_df.sort_values(by=['Doctor Name', 'Course Date']).groupby('Doctor Name')

    conflicts = []
    for doctor, group in grouped_df:
        prev_start_date = None
        for _, row in group.iterrows():
            if prev_start_date and row['Course Date'] <= prev_start_date:
                conflicts.append([doctor, row['Course'], row['Course Date'], 'Overlap with previous course'])
            prev_start_date = row['Course Date']

    # Convert conflicts to a dataframe
    conflicts_df = pd.DataFrame(conflicts, columns=['Doctor Name', 'Course', 'Conflict Date', 'Conflict Type'])
    return conflicts_df

# Streamlit app
st.title('Course Timetable Conflict Detector')

# Download Example File
link = "https://docs.google.com/spreadsheets/d/1uvmsb1ivFgIh2oC6oHLA9yalfyTrsdrR/edit?usp=sharing&ouid=113847241366072233997&rtpof=true&sd=true"
st.markdown(f"[Download Example]({link})", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=['xlsx'])

if uploaded_file is not None:
    # Process the file
    conflicts_df = process_file(uploaded_file)

    # Show the data
    st.write("Conflicts Detected:")
    st.dataframe(conflicts_df)

    # Download conflicts as CSV
    towrite = io.BytesIO()
    conflicts_df.to_csv(towrite, index=False, encoding='utf-8')
    towrite.seek(0)
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="timetable_conflicts.csv">Download Conflicts CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
