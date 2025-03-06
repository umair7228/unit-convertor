import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="wide")

st.markdown("""
    <style>
        .st-emotion-cache-1104ytp egexzqm0 {
            padding: 0px !important;
            margin-bottom: 0px !important;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center; /* Aligns items vertically */
            width: 100%;
            margin-bottom: 0px;
        }
        .buttons-container {
            display: flex;
            gap: 10px;
        }
        .buttons-container a {
            text-decoration: none;
        }
        .buttons-container button {
            padding: 8px 16px;
            font-size: 14px;
            border-radius: 8px;
            border: 1px solid #ccc;
            background-color: white;
            cursor: pointer;
            transition: 0.3s;
        }
        .buttons-container button:hover {
            background-color: #f0f0f0;
        }
        .hr-tagg {
            margin-top: -30px;
        }

        @media (max-width: 1024px) {
            .buttons-container button {
                padding: 6px 10px;
                font-size: 14px;
            }
            .title-container h1 {
                font-size: 40px;
            }
        }

        @media (max-width: 768px) {
            .header-container {
                flex-direction: column;
                align-items: center; /* Centers everything */
                text-align: center;
            }
            .buttons-container {
                justify-content: center;
                width: 100%;
                margin-top: 10px; /* Adds spacing for clarity */
            }

            .buttons-container button {
                width: 100%; /* Full width buttons for mobile */
            }
            .hr-tagg {
                margin-top: -20px;
            }
        }

        @media (max-width: 640px) {
            .title-container h1 {
                font-size: 32px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# HTML for title & buttons
st.markdown("""
    <div class="header-container">
        <div class="title-container">
            <h1>Unit Convertor</h1>
        </div>
        <div class="buttons-container">
            <a href="https://umair-portfolio-web.vercel.app/" target="_blank">
                <button>🌍 Portfolio</button>
            </a>
            <a href="https://www.linkedin.com/in/umairnawaz7228/" target="_blank">
                <button>🔗 LinkedIn</button>
            </a>
            <a href="https://github.com/umair7228" target="_blank">
                <button>🐙 GitHub</button>
            </a>
        </div>
    </div>
    <div class="hr-tagg"><hr></div>
""", unsafe_allow_html=True)

# Conversion factors for different units
conversion_data = {
    "Length": {
        "Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001,
        "Micrometer": 1e-6, "Nanometer": 1e-9, "Mile": 1609.34, "Yard": 0.9144,
        "Foot": 0.3048, "Inch": 0.0254
    },
    "Area": {
        "Square Meter": 1, "Square Kilometer": 1e6, "Square Centimeter": 0.0001,
        "Square Millimeter": 1e-6, "Hectare": 10000, "Acre": 4046.86,
        "Square Mile": 2.59e6, "Square Yard": 0.836127, "Square Foot": 0.092903, "Square Inch": 0.00064516
    },
    "Mass": {
        "Kilogram": 1, "Gram": 0.001, "Milligram": 1e-6, "Microgram": 1e-9,
        "Metric Ton": 1000, "Pound": 0.453592, "Ounce": 0.0283495
    },
    "Volume": {
        "Cubic Meter": 1, "Liter": 0.001, "Milliliter": 1e-6,
        "Cubic Centimeter": 1e-6, "Cubic Millimeter": 1e-9,
        "Cubic Inch": 1.63871e-5, "Cubic Foot": 0.0283168, "Cubic Yard": 0.764555
    },
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Speed": {
        "Meter per second": 1, "Kilometer per hour": 0.277778,
        "Mile per hour": 0.44704, "Knot": 0.514444, "Foot per second": 0.3048
    },
    "Time": {
        "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400,
        "Week": 604800, "Month": 2.63e6, "Year": 3.154e7
    },
    "Pressure": {
        "Pascal": 1, "Kilopascal": 1000, "Bar": 100000,
        "PSI": 6894.76, "Atmosphere": 101325
    },
    "Energy": {
        "Joule": 1, "Kilojoule": 1000, "Calorie": 4.184,
        "Kilocalorie": 4184, "Watt-hour": 3600, "Kilowatt-hour": 3.6e6
    },
    "Frequency": {
        "Hertz": 1, "Kilohertz": 1000, "Megahertz": 1e6, "Gigahertz": 1e9
    },
    "Fuel Economy": {
        "Kilometers per liter": 1, "Miles per gallon": 0.425144
    },
    "Digital Storage": {
        "Bit": 1, "Byte": 8, "Kilobyte": 8192, "Megabyte": 8.39e6,
        "Gigabyte": 8.59e9, "Terabyte": 8.8e12
    },
    "Data Transfer Rate": {
        "Bit per second": 1, "Kilobit per second": 1000,
        "Megabit per second": 1e6, "Gigabit per second": 1e9,
        "Terabit per second": 1e12
    },
    "Plane Angle": {
        "Degree": 1, "Radian": 57.2958, "Gradian": 0.9
    }
}

# Select conversion category
category = st.selectbox("Select the unit category", list(conversion_data.keys()))

# Select conversion units
if category:
    value = st.number_input("Enter the value", min_value=0.0, value=1.0, step=1.0)

    col1, col2 = st.columns(2)

    with col1:
        from_unit = st.selectbox("From", list(conversion_data[category]) if category != "Temperature" else conversion_data[category])

    with col2:
        to_unit = st.selectbox("To", list(conversion_data[category]) if category != "Temperature" else conversion_data[category])

    def convert(value, from_unit, to_unit, category):
        """Handles unit conversion."""
        if category == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                return (value - 32) * 5/9
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                return value + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                return value - 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            return value  # If same unit

        # Handle normal unit conversions
        if from_unit in conversion_data[category] and to_unit in conversion_data[category]:
            return value * (conversion_data[category][from_unit] / conversion_data[category][to_unit])
        return value  # If same unit

    if st.button("Convert"):
        result = convert(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")