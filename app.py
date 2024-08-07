import streamlit as st
import pandas as pd

def main():
    # Title of the application
    st.title('CSV Merger App')

    # Instructions
    st.write('Please upload multiple CSV files. The app will combine them into a single CSV file.')

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

        # Input for custom file name
        output_file_name = st.text_input('Enter desired output file name', 'combined.csv')
        if not output_file_name.endswith('.csv'):
            output_file_name += '.csv'

        # Button to let user save the combined CSV with the specified file name
        if st.button('Save Combined CSV'):
            # Convert DataFrame to CSV
            combined_csv = combined_df.to_csv(index=False).encode('utf-8')

            # Download button for the combined CSV with custom file name
            st.download_button(label="Download combined CSV",
                               data=combined_csv,
                               file_name=output_file_name,
                               mime='text/csv')

    # Add footer widget
    st.markdown("""---""")
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image('https://jlenra.stripocdn.email/content/guids/CABINET_b4fb9434a27e7f73d8d9af44957cbe646ea8281715657430766aee513bd7ddd9/images/garberarchblue.png', width=150)

    with col2:
        st.write("""
        **Developed by**
        *Garber Management Digital Marketing Team*
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
