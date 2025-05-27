import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

st.title("🌍 COVID-19 Dashboard")
st.markdown("Data Source: [JHU CSSE COVID-19 GitHub](https://github.com/CSSEGISandData/COVID-19)")

# Load local archived data
local_url = "time_series_19-covid-Confirmed_archived_0325.csv"
try:
    df = pd.read_csv(local_url)
    cases_worldwide = df.iloc[:, 4:].sum(axis=0)
    cases_worldwide.index = pd.to_datetime(cases_worldwide.index, errors='coerce')

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(cases_worldwide.index, cases_worldwide.values)
    ax1.set_title("Worldwide Confirmed COVID-19 Cases (Archived Data)")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Number of Cases")
    ax1.grid(True)
    st.pyplot(fig1)
except Exception as e:
    st.error(f"Failed to load or process archived data: {e}")

# Load online data from GitHub
st.markdown("---")
st.subheader("Top 5 Countries with Most Confirmed Cases")

try:
    url_new = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    dff = pd.read_csv(url_new)

    df_country = dff.drop(columns=["Province/State", "Lat", "Long"])
    df_country = df_country.groupby("Country/Region").sum()
    df_country = df_country.transpose()
    df_country.index = pd.to_datetime(df_country.index, errors='coerce')

    latest_totals = df_country.iloc[-1]
    top_5_countries = latest_totals.sort_values(ascending=False).head(5).index

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    for country in top_5_countries:
        ax2.plot(df_country.index, df_country[country], label=country)

    ax2.set_title("Top 5 Countries - COVID-19 Confirmed Cases Over Time")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Confirmed Cases")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

except Exception as e:
    st.error(f"Failed to load or process online data: {e}")
