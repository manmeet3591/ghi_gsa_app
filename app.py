import streamlit as st
import xarray as xr

# Load the dataset (update path if necessary)
@st.cache
def load_data():
    ds = xr.open_dataset("ghi_texas.nc")
    return ds

# Define the main function for the Streamlit app
def main():
    st.title("GHI Query App - Texas Region")

    # Load data
    ds = load_data()

    # User input for latitude and longitude
    lat = st.number_input("Enter latitude:", min_value=25.84, max_value=36.68, value=30.0)
    lon = st.number_input("Enter longitude:", min_value=-106.6, max_value=-93.51, value=-100.0)

    # Query the nearest neighbor value
    try:
        ghi_value = ds["b1"].sel(x=lon, y=lat, method="nearest").values
        st.write(f"Nearest GHI Value: {ghi_value}")
    except Exception as e:
        st.error(f"Error retrieving GHI value: {e}")

# Run the app
if __name__ == "__main__":
    main()
