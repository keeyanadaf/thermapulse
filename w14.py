import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit UI setup with light pink background and black headings
st.markdown(
    """
    <style>
    body {
        background-color: #FFB6C1;  /* Light pink background */
        background-image: none;  /* Remove any background image */
        color: black;  /* Black text for high contrast */
    }
    h1, h2, h3, p {
        color: black;  /* Black text for headings */
    }
    .metric {
        color: #FF5733 !important;  /* Orange color for metrics */
    }
    .streamlit-expanderHeader {
        color: #FF5733;  /* High contrast for expandable headers */
    }
    .css-1v3fvcr {
        background-color: #FFB6C1;  /* Light pink background for sidebar */
    }
    .stButton>button {
        background-color: #FF5733;  /* Button color */
        color: white;
    }
    .stButton>button:hover {
        background-color: #C70039;  /* Hover effect for button */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["Homepage", "Dashboard"])

# Homepage
if menu == "Homepage":
    st.title("Welcome to ThermaPulse!")
    st.header("Experience Intelligent Pain Relief")
    st.markdown(
        """
        *ThermaPulse* is a cutting-edge smart belt designed for:  
        - *AI-Driven Insights*: Smarter therapy tailored to your needs.  
        - *Dynamic Adjustments*: Real-time pain relief using TENS and near-IR radiation.  
        - *Personalized Comfort*: Therapy modes adapted just for you.  

        #### Key Features:
        - Continuous therapy tracking.  
        - Intelligent decision support for personalized recommendations.  
        - Dynamic mode switching for enhanced comfort.  

        Explore how TheraPulse can transform pain management.  
        """
    )
    # Add Image to Homepage
    st.image("https://down-sg.img.susercontent.com/file/sg-11134201-7qve0-lf3ifgnjlvgfed", caption="TheraPulse Smart Belt")  # Replace with the correct image URL

    st.button("Learn More")

# Dashboard
elif menu == "Dashboard":
    st.title("ThermaPulse Dashboard")
    st.write("Track therapy sessions, analyze trends, and explore personalized insights.")

    # Mock Data for Visualization
    data = {
        "Timestamp": pd.date_range(start="2024-01-01", periods=10, freq="D"),
        "TENS Intensity": [20, 30, 25, 35, 40, 30, 20, 25, 30, 35],
        "Near-IR Intensity": [15, 20, 25, 20, 25, 30, 25, 20, 15, 20],
        "Relief Score": [3, 4, 5, 4, 5, 5, 3, 4, 4, 5],
    }
    df = pd.DataFrame(data)

    # Relief Trends
    st.subheader("Therapy Trends")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["Timestamp"], df["TENS Intensity"], label="TENS Intensity", marker="o", color="#FF5733")  # Red color for TENS
    ax.plot(df["Timestamp"], df["Near-IR Intensity"], label="Near-IR Intensity", marker="o", color="#FFDD57")  # Yellow for Near-IR
    ax.set_xlabel("Date")
    ax.set_ylabel("Intensity Level")
    ax.set_title("Therapy Intensity Over Time")
    ax.legend()
    ax.grid(True, color='black')  # Grid color to match the black headings
    st.pyplot(fig)

    # User Feedback Visualization
    st.subheader("User Feedback")
    relief_chart = df[["Timestamp", "Relief Score"]]
    st.bar_chart(relief_chart.set_index("Timestamp"), color='#FFDD57')  # Yellow bars for relief score

    # Therapy Session Summary
    st.subheader("Session Summary")
    st.dataframe(df)

    # Recommendations Section
    st.subheader("Personalized Recommendations")
    st.write(
        """
        Based on your recent sessions:
        - Increase *TENS intensity* during peak pain hours.  
        - Adjust *Near-IR intensity* for sustained relief.  
        - Monitor and rate relief scores consistently to refine insights.  
        """
    )
    st.button("Generate New Insights")
