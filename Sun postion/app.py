import streamlit as st
import pvlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.patches import Circle, Rectangle, Wedge

# Set page configuration
st.set_page_config(
    page_title="SolarBoost",
    page_icon="☀️",
    layout="wide"
)

# App title and description
st.title("☀️ SolarBoost")
st.markdown(
    """
    ## Introduction
    * Calculate the sun's position (azimuth and elevation) based on date, time, and location
    * Visualize sun position with interactive polar plot
    * Get accurate sunrise and sunset times for any location
    * Estimate solar energy production for your solar panels
    * Plan optimal solar panel placement with real-time data
    """
)

# Create sidebar for inputs
with st.sidebar:
    st.header("Input Parameters")
    
    # Date input
    date = st.date_input(
        "Date",
        datetime.now().date(),
        help="Select the date for sun position calculation"
    )
    
    # Time input
    time = st.time_input(
        "Time",
        datetime.now().time(),
        help="Select the time for sun position calculation"
    )
    
    # Location inputs
    st.subheader("Location")
    
    # Latitude input with validation
    latitude = st.number_input(
        "Latitude (degrees)",
        min_value=-90.0,
        max_value=90.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
        help="Enter latitude in decimal degrees (-90 to 90)"
    )
    
    # Longitude input with validation
    longitude = st.number_input(
        "Longitude (degrees)",
        min_value=-180.0,
        max_value=180.0,
        value=0.0,
        step=0.0001,
        format="%.4f",
        help="Enter longitude in decimal degrees (-180 to 180)"
    )
    
    # Time zone input
    timezone = st.number_input(
        "Time Zone (UTC offset in hours)",
        min_value=-12.0,
        max_value=14.0,
        value=0.0,
        step=0.5,
        help="Enter the UTC offset for your timezone"
    )
    
    # Solar Panel Parameters
    st.subheader("Solar Panel Specifications")
    
    # Panel area input
    panel_area = st.number_input(
        "Panel Area (m²)",
        min_value=0.1,
        max_value=100.0,
        value=1.0,
        step=0.1,
        format="%.2f",
        help="Enter the total area of solar panels in square meters"
    )
    
    # Panel efficiency input
    panel_efficiency = st.number_input(
        "Panel Efficiency (%)",
        min_value=1.0,
        max_value=30.0,
        value=20.0,
        step=0.5,
        format="%.1f",
        help="Enter the efficiency of your solar panels (typical range: 15-22%)"
    )
    
    # Panel tilt angle
    panel_tilt = st.number_input(
        "Panel Tilt (degrees)",
        min_value=0.0,
        max_value=90.0,
        value=latitude if latitude > 0 else 0.0,  # Default to latitude for northern hemisphere
        step=1.0,
        format="%.1f",
        help="Enter the tilt angle of your solar panels from horizontal"
    )
    
    # Panel azimuth angle
    panel_azimuth = st.number_input(
        "Panel Azimuth (degrees)",
        min_value=0.0,
        max_value=360.0,
        value=180.0,  # Default to south-facing
        step=1.0,
        format="%.1f",
        help="Enter the azimuth angle of your panels (180° = South, 90° = East, 270° = West)"
    )

# Combine date and time into a datetime object
timestamp = datetime.combine(date, time)

# Create a pandas DatetimeIndex for pvlib
times = pd.DatetimeIndex([timestamp])

# Calculate sun position using pvlib
# Convert timezone offset to a timezone string for pvlib
tz_offset_str = f"Etc/GMT{'-' if timezone > 0 else '+'}{abs(int(timezone))}"

# Apply timezone to the DatetimeIndex
times = times.tz_localize('UTC').tz_convert(tz_offset_str)

solpos = pvlib.solarposition.get_solarposition(
    time=times,
    latitude=latitude,
    longitude=longitude,
    altitude=0,  # Assuming sea level
    temperature=12,  # Standard temperature in Celsius
    pressure=101325  # Standard pressure in Pascal
)

# Extract azimuth and elevation (zenith angle converted to elevation)
azimuth = solpos['azimuth'].iloc[0]
elevation = solpos['apparent_elevation'].iloc[0]

# Display results
st.header("Sun Position Results")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Azimuth (degrees)",
        value=f"{azimuth:.2f}°",
        help="Azimuth is the sun's angle along the horizon (0° = North, 90° = East, 180° = South, 270° = West)"
    )

with col2:
    st.metric(
        label="Elevation (degrees)",
        value=f"{elevation:.2f}°",
        help="Elevation is the angle of the sun above the horizon (0° = horizon, 90° = directly overhead)"
    )

# Add explanation
st.markdown("""
### Understanding Sun Position

- **Azimuth**: The sun's angle along the horizon measured clockwise from North.
  - 0° = North
  - 90° = East
  - 180° = South
  - 270° = West

- **Elevation**: The angle of the sun above the horizon.
  - 0° = at the horizon
  - 90° = directly overhead (zenith)
  - Negative values indicate the sun is below the horizon
""")

# Visualization
st.header("Sun Position Visualization")

# Create figure for visualization
fig, ax = plt.subplots(figsize=(10, 5), subplot_kw={'projection': 'polar'})

# Convert azimuth from degrees to radians and adjust for polar plot
# In polar plots, 0 is to the right (East) and increases counter-clockwise
# We need to convert from azimuth (0=North, clockwise) to polar (0=East, counter-clockwise)
azimuth_rad = np.radians((450 - azimuth) % 360)

# Plot the sun position
ax.scatter(azimuth_rad, 90 - elevation, s=300, color='yellow', edgecolor='orange', zorder=3, label='Sun')

# Set the polar plot limits and direction
ax.set_theta_zero_location('N')  # Set 0 degrees to North
ax.set_theta_direction(-1)  # Set clockwise direction
ax.set_rlim(0, 90)  # Set radial limits from 0 to 90 degrees

# Add compass directions
ax.set_xticklabels(['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'])

# Set radial ticks and labels
ax.set_rticks([0, 30, 60, 90])  # Elevation angles
ax.set_yticklabels(['90°', '60°', '30°', '0°'])  # Elevation labels

# Add horizon circle
ax.add_patch(plt.Circle((0, 0), 90, transform=ax.transData._b, fill=False, color='gray', linestyle='--', alpha=0.5))

# Add grid
ax.grid(True, alpha=0.3)

# Add title
ax.set_title(f'Sun Position: Azimuth={azimuth:.1f}°, Elevation={elevation:.1f}°', pad=20)

# Display the plot in Streamlit
st.pyplot(fig)

# Add day length calculation
st.header("Daylight Information")

# Calculate sunrise, sunset, and day length
# Create a datetime for the start of the day in the specified timezone
day_start = pd.DatetimeIndex([times[0].replace(hour=0, minute=0, second=0)])

sunrise_sunset = pvlib.solarposition.sun_rise_set_transit_spa(
    day_start,
    latitude,
    longitude
)

# Extract sunrise and sunset times
sunrise = sunrise_sunset['sunrise']
sunset = sunrise_sunset['sunset']

# Check if sunrise/sunset exist for the given day (e.g., polar day/night)
if pd.notna(sunrise.iloc[0]) and pd.notna(sunset.iloc[0]):
    sunrise_time = sunrise.iloc[0].strftime('%H:%M')
    sunset_time = sunset.iloc[0].strftime('%H:%M')
    
    # Calculate day length
    day_length_td = sunset.iloc[0] - sunrise.iloc[0]
    hours, remainder = divmod(day_length_td.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    day_length_str = f"{hours}h {minutes}m"
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Sunrise", sunrise_time)
    
    with col2:
        st.metric("Sunset", sunset_time)
    
    with col3:
        st.metric("Day Length", day_length_str)
else:
    if latitude > 66.5 or latitude < -66.5:  # Near polar regions
        st.info("In polar regions, there may be periods of midnight sun or polar night depending on the season.")
    else:
        st.warning("Could not calculate sunrise/sunset times for the given location and date.")

# Calculate Solar Energy Production
st.header("Solar Energy Production Estimate")

# Calculate clear sky radiation using pvlib
try:
    # Get solar position for the specific time
    solar_position = pvlib.solarposition.get_solarposition(
        time=times,
        latitude=latitude,
        longitude=longitude,
        altitude=0
    )
    
    # Calculate clear sky irradiance using simplified Solis model
    clearsky_data = pvlib.clearsky.simplified_solis(solar_position['apparent_zenith'])
    
    # Get direct normal irradiance (DNI), global horizontal irradiance (GHI), and diffuse horizontal irradiance (DHI)
    dni = clearsky_data['dni']
    ghi = clearsky_data['ghi']
    dhi = clearsky_data['dhi']
    
    # Calculate total irradiance on the plane of array (POA)
    clearsky = pvlib.irradiance.get_total_irradiance(
        surface_tilt=panel_tilt,
        surface_azimuth=panel_azimuth,
        dni=dni,
        ghi=ghi,
        dhi=dhi,
        solar_zenith=solar_position['apparent_zenith'],
        solar_azimuth=solar_position['azimuth']
    )
    
    # Get the plane of array irradiance (W/m²)
    poa_irradiance = clearsky['poa_global'].iloc[0]
    
    # Calculate instantaneous power (W)
    panel_efficiency_decimal = panel_efficiency / 100  # Convert from percentage to decimal
    power_output_watts = poa_irradiance * panel_area * panel_efficiency_decimal
    
    # Convert to kW for display
    power_output_kw = power_output_watts / 1000
    
    # Calculate energy production for 1 hour (kWh)
    energy_production_kwh = power_output_kw * 1  # Assuming 1 hour of production at this rate
    
    # Display results
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Solar Irradiance",
            value=f"{poa_irradiance:.2f} W/m²",
            help="Solar irradiance on the plane of the solar panel"
        )
    
    with col2:
        st.metric(
            label="Power Output",
            value=f"{power_output_kw:.3f} kW",
            help="Instantaneous power output from your solar panel setup"
        )
    
    with col3:
        st.metric(
            label="Energy (1 hour)",
            value=f"{energy_production_kwh:.3f} kWh",
            help="Estimated energy production if conditions remain constant for 1 hour"
        )
    
    # Add explanation
    st.markdown("""
    ### Understanding Solar Energy Production
    
    - **Solar Irradiance**: The amount of solar radiation received per unit area on the panel surface (W/m²)
    - **Power Output**: The instantaneous electrical power generated by your solar panels (kW)
    - **Energy Production**: The estimated electrical energy produced over time (kWh)
    
    **Note**: These calculations assume clear sky conditions. Actual production may be lower due to clouds, dust, or other factors.
    """)
    
    # Show factors affecting production
    with st.expander("Factors Affecting Solar Production"):
        st.markdown("""
        - **Panel Orientation**: Optimal tilt is generally equal to your latitude
        - **Time of Day**: Peak production occurs at solar noon
        - **Season**: Summer months typically have higher production in most locations
        - **Weather**: Clouds and atmospheric conditions reduce production
        - **Panel Efficiency**: Higher efficiency panels produce more power per square meter
        - **Temperature**: Most panels lose efficiency at high temperatures
        """)

except Exception as e:
    st.warning(f"Could not calculate solar energy production: {str(e)}")
    st.info("Solar energy calculations require valid sun position data. Please ensure the sun is above the horizon.")

# Add footer
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p>Created with Streamlit and pvlib | SolarBoost</p>
</div>
""", unsafe_allow_html=True)