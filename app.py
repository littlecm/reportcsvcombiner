import streamlit as st
import pandas as pd

def main():
    # Title of the application
    st.title('CSV Merger App')

    # Instructions
    st.write('Upload multiple CSV files. The app will combine them into a single CSV file.')

    # File uploader allows user to add multiple files
    uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True, type=['csv'])
    if uploaded_files is not None and len(uploaded_files) > 0:
        # Empty list to hold dataframes
        dataframes = []

        # Loop through the files
        for uploaded_file in uploaded_files:
            # Read the file into a dataframe and append to list
            df = pd.read_csv(uploaded_file)
            dataframes.append(df)

        # Concatenate all dataframes in the list
        combined_df = pd.concat(dataframes, ignore_index=True)

        # Show the combined dataframe
        st.write('Combined DataFrame:')
        st.dataframe(combined_df)

        # Button to let user save the combined CSV
        if st.button('Save Combined CSV'):
            # Convert DataFrame to CSV
            combined_csv = combined_df.to_csv(index=False).encode('utf-8')

            # Download button for the combined CSV
            st.download_button(label="Download combined CSV",
                               data=combined_csv,
                               file_name='combined.csv',
                               mime='text/csv')

if __name__ == "__main__":
    main()
