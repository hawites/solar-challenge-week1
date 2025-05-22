import pandas as pd

class SolarDataLoader:
    def __init__(self):
        self.country_files = {
            'Benin': 'data/benin-malanville_clean.csv',
            'Togo': 'data/togo-dapaong_qc_clean.csv',
            'Sierra Leone': 'data/sierraleone-bumbuna_clean.csv'
        }

    def get_country_list(self):
        return list(self.country_files.keys())

    def load_data(self, country):
        path = self.country_files.get(country)
        if path:
            try:
                df = pd.read_csv(path)
                df['Country'] = country
                return df
            except FileNotFoundError:
                return pd.DataFrame()
        return pd.DataFrame()
