# Test Data for Solar Sun Position Predictor

Below are some sample locations and dates you can use to test the application. These include various locations around the world and different times of the year to verify the application works correctly.

## Sample Test Locations

### Major Cities

| City | Latitude | Longitude | Time Zone (UTC) |
|------|----------|-----------|----------------|
| New York, USA | 40.7128 | -74.0060 | -5 (EST) or -4 (EDT) |
| London, UK | 51.5074 | -0.1278 | 0 (GMT) or +1 (BST) |
| Tokyo, Japan | 35.6762 | 139.6503 | +9 |
| Sydney, Australia | -33.8688 | 151.2093 | +10 (AEST) or +11 (AEDT) |
| Rio de Janeiro, Brazil | -22.9068 | -43.1729 | -3 |
| Cape Town, South Africa | -33.9249 | 18.4241 | +2 |

### Extreme Locations

| Location | Latitude | Longitude | Time Zone (UTC) | Notes |
|----------|----------|-----------|----------------|-------|
| North Pole | 90.0000 | 0.0000 | 0 | Polar day/night |
| South Pole | -90.0000 | 0.0000 | 0 | Polar day/night |
| Equator (Quito) | 0.0000 | -78.4678 | -5 | Equal day/night |

## Special Dates to Test

### Solstices and Equinoxes (2024)

| Event | Date | Notes |
|-------|------|-------|
| Spring Equinox | March 20, 2024 | Equal day and night |
| Summer Solstice (Northern) | June 20, 2024 | Longest day in Northern Hemisphere |
| Fall Equinox | September 22, 2024 | Equal day and night |
| Winter Solstice (Northern) | December 21, 2024 | Shortest day in Northern Hemisphere |

## Expected Results

Here are some expected results for specific location/date/time combinations:

### New York on Summer Solstice
- **Location**: New York (40.7128, -74.0060)
- **Date**: June 20, 2024
- **Time**: 12:00 PM (Local Time)
- **Expected Results**:
  - Azimuth: ~177° (approximately south)
  - Elevation: ~73° (high in the sky)
  - Sunrise: ~5:25 AM
  - Sunset: ~8:30 PM
  - Day Length: ~15h 5m

### London on Winter Solstice
- **Location**: London (51.5074, -0.1278)
- **Date**: December 21, 2024
- **Time**: 12:00 PM (Local Time)
- **Expected Results**:
  - Azimuth: ~180° (south)
  - Elevation: ~15° (low in the sky)
  - Sunrise: ~8:05 AM
  - Sunset: ~3:55 PM
  - Day Length: ~7h 50m

### Equator on Equinox
- **Location**: Quito, Ecuador (0.0000, -78.4678)
- **Date**: March 20, 2024
- **Time**: 12:00 PM (Local Time)
- **Expected Results**:
  - Azimuth: ~0° or 360° (north)
  - Elevation: ~90° (directly overhead)
  - Sunrise: ~6:00 AM
  - Sunset: ~6:00 PM
  - Day Length: ~12h 0m

## Testing Tips

1. **Verify Sunrise/Sunset**: For locations near the equator, sunrise should be around 6 AM and sunset around 6 PM throughout the year with minimal variation.

2. **Check Polar Regions**: For dates near the solstices, locations inside the Arctic/Antarctic Circles may show "polar day" (no sunset) or "polar night" (no sunrise).

3. **Elevation at Solar Noon**: At solar noon (when the sun is highest):
   - On the equator: The sun should be directly overhead (90°) on equinoxes
   - At the Tropic of Cancer (23.5°N): The sun should be directly overhead on the June solstice
   - At the Tropic of Capricorn (23.5°S): The sun should be directly overhead on the December solstice

4. **Azimuth Direction**: In the Northern Hemisphere, the sun should be in the south at solar noon. In the Southern Hemisphere, it should be in the north.

5. **Day Length Variation**: The difference between summer and winter day length increases as you move away from the equator.