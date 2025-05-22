import streamlit as st
from utils import SolarDataLoader
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class SolarDashboardApp:
    def __init__(self):
        self.data_loader = SolarDataLoader()
        self.selected_country = None
        self.df = pd.DataFrame()

    def render(self):
        st.set_page_config(page_title="Solar Dashboard", layout="wide")
        st.title("☀️ Cross-Country Solar Irradiance Dashboard")

        self.selected_country = st.selectbox("Select a country:", self.data_loader.get_country_list())
        self.df = self.data_loader.load_data(self.selected_country)

        if self.df.empty:
            st.warning("No data available.")
            return

        self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
        self.df['Month'] = self.df['Timestamp'].dt.month

        self.show_metric_boxplot()
        self.show_monthly_avg_chart()
        self.show_summary_stats()

    def show_metric_boxplot(self):
        metric = st.selectbox("Choose irradiance metric:", ['GHI', 'DNI', 'DHI'])

        st.subheader(f"{metric} Distribution in {self.selected_country}")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(y=self.df[metric], ax=ax)
        ax.set_title(f"{metric} Boxplot")
        st.pyplot(fig)

    def show_monthly_avg_chart(self):
        st.subheader("📈 Average GHI by Month")
        monthly_avg = self.df.groupby('Month')['GHI'].mean()
        
        fig, ax = plt.subplots(figsize=(8, 4))
        monthly_avg.plot(kind='bar', ax=ax)
        ax.set_title("Average GHI by Month")
        ax.set_ylabel("GHI (W/m²)")
        ax.set_xlabel("Month")
        st.pyplot(fig)

    def show_summary_stats(self):
        st.subheader("📋 Summary Statistics")
        desc = self.df[['GHI', 'DNI', 'DHI']].describe().round(2)
        st.markdown(desc.to_markdown())


if __name__ == "__main__":
    app = SolarDashboardApp()
    app.render()
