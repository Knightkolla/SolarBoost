


# ☀️ SolarBoost

SolarBoost is an interactive web application that calculates and visualizes the sun's position and solar energy production potential based on location, date, and time.

---

## 🌟 Features
- Calculate the sun's position (azimuth and elevation) based on date, time, and location  
- Visualize sun position with an interactive polar plot  
- Get accurate sunrise and sunset times for any location  
- Estimate solar energy production for your solar panels  
- Plan optimal solar panel placement with real-time data  

---

## ⚙️ Installation

### Prerequisites
- Python 3.7 or higher  
- pip (Python package installer)  

### Setup Instructions
1. Clone the repository:
 bash
   git clone <repository-url>
   cd "Sun position"


2. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

1. Start the application:

   ```bash
   streamlit run app.py
   ```

2. Access the application in your browser:

   * Local URL: [http://localhost:8501](http://localhost:8501)
   * Network URL: `http://your-ip-address:8501` (for accessing from other devices on the same network)

3. Using the application:

   * **Input Parameters**: Enter date, time, location, and solar panel specifications in the sidebar
   * **Results**: View sun position, daylight info, and solar energy production estimates in the main panel
   * **Visualization**: Explore the interactive polar plot showing the sun’s position

---

## 🧪 Testing

The app includes test data for verification. Use the provided `test_data.md` for accuracy checks, including:

* Major cities around the world (New York, London, Tokyo, etc.)
* Extreme locations (North Pole, South Pole, Equator)
* Special dates (solstices and equinoxes)

**Example Test Case:**

* Location: New York (40.7128, -74.0060)
* Date: June 20, 2024 (Summer Solstice)
* Time: 12:00 PM (Local Time)

---

## 📦 Dependencies

* [streamlit ≥1.22.0](https://streamlit.io/) — Web application framework
* [pvlib ≥0.9.0](https://pvlib-python.readthedocs.io/) — Solar position & irradiance calculations
* [matplotlib ≥3.5.0](https://matplotlib.org/) — Data visualization
* [numpy ≥1.22.0](https://numpy.org/) — Numerical computations
* [pandas ≥1.4.0](https://pandas.pydata.org/) — Data manipulation

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

```


