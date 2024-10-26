import streamlit as st
import xarray as xr
import pandas as pd

# Load the dataset with multi-file input (update path if necessary)
@st.cache
def load_data():
    ds = xr.open_mfdataset('ssrd_era5_2023_texas_???.nc')
    return ds

# Define the main function for the Streamlit app
def main():
    st.title("GHI Query App - Texas Region")

    # Load data
    ds = load_data()

    # User input for latitude and longitude
    lat = st.number_input("Enter latitude:", min_value=25.84, max_value=36.68, value=30.0)
    lon_input = st.number_input("Enter longitude (e.g., -100):", min_value=-106.6, max_value=-93.51, value=-100.0)
    
    # Convert longitude input to positive format by adding 360
    lon = 360 + lon_input

    # Query the nearest neighbor value and convert to CSV
    try:
        selected_data = ds.sel(latitude=lat, method='nearest').sel(longitude=lon, method='nearest').to_dataframe()
        csv_file = selected_data.to_csv(index=False)

        # Download button for CSV file
        st.download_button(
            label="Download GHI Data as CSV",
            data=csv_file,
            file_name=f'ssrd_texas_2023_lat{lat}_lon{lon_input}.csv',
            mime='text/csv'
        )
        st.write(f"Data for Latitude: {lat} and Longitude: {lon_input} has been prepared for download.")

    except Exception as e:
        st.error(f"Error retrieving GHI data: {e}")

# Run the app
if __name__ == "__main__":
    main()

# import streamlit as st
# import xarray as xr

# # Load the dataset (update path if necessary)
# @st.cache
# def load_data():
#     ds = xr.open_dataset("ghi_texas.nc")
#     return ds

# # Define the main function for the Streamlit app
# def main():
#     st.title("GHI Query App - Texas Region")

#     # Load data
#     ds = load_data()

#     # User input for latitude and longitude
#     lat = st.number_input("Enter latitude:", min_value=25.84, max_value=36.68, value=30.0)
#     lon = st.number_input("Enter longitude:", min_value=-106.6, max_value=-93.51, value=-100.0)

#     # Query the nearest neighbor value
#     try:
#         ghi_value = ds["b1"].sel(x=lon, y=lat, method="nearest").values
#         st.write(f"Nearest GHI Value: {ghi_value}")
#     except Exception as e:
#         st.error(f"Error retrieving GHI value: {e}")

# # Run the app
# if __name__ == "__main__":
#     main()
