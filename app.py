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
    footer = """
    <div class="footer">
        <table cellpadding="0" cellspacing="0" width="100%" role="presentation">
            <tbody><tr>
                <td align="left" style="padding:0;Margin:0;width:560px">
                    <table cellpadding="0" cellspacing="0" width="100%" role="presentation">
                        <tbody><tr>
                            <td align="center" style="padding:10px;Margin:0;font-size:0">
                                <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" role="presentation">
                                    <tbody><tr>
                                        <td style="padding:0;Margin:0;border-bottom:0px solid #cccccc;background:unset;height:1px;width:100%;margin:0px"></td>
                                    </tr>
                                </tbody></table>
                            </td>
                        </tr>
                        <tr>
                            <td align="center" style="padding:0;Margin:0;font-size:0px"><img src="https://jlenra.stripocdn.email/content/guids/CABINET_b4fb9434a27e7f73d8d9af44957cbe646ea8281715657430766aee513bd7ddd9/images/garberarchblue.png" alt="" style="display:block;border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic" width="150"></td>
                        </tr>
                        <tr>
                            <td align="center" class="es-m-txt-c es-m-p10" style="padding:0;Margin:0;padding-top:5px">
                                <p style="Margin:0;font-family:'Lato', sans-serif;line-height:20px;color:#333;font-size:13px">Designed by</p>
                                <p style="Margin:0;font-family:'Lato', sans-serif;line-height:20px;color:#021143;font-size:13px"><strong>Garber Management Digital Marketing Team</strong></p>
                            </td>
                        </tr>
                    </tbody></table>
                </td>
            </tr>
        </tbody></table>
    </div>
    """
    
    st.markdown(footer, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
