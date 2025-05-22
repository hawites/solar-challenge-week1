# Solar Challenge Week 1

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate
3. Clean data: Perform cleaning on each country file
4. Visualize data and compare results

##  Project Structure


solar-challenge-week1/
+-- notebooks/
¦   +-- benin_eda.ipynb
¦   +-- sierra_leone_eda.ipynb
¦   +-- togo_eda.ipynb
¦   +-- compare_countries.ipynb
+-- data/                   # Local only – 
+-- requirements.txt
+-- README.md
+-- .gitignore
+-- .github/
    +-- workflows/
        +-- ci.yml

## Streamlit Dashboard

An interactive dashboard built with Streamlit for visualizing solar irradiance data.

### Features:
- Country selector (Benin, Togo, Sierra Leone)
- Boxplot for GHI, DNI, DHI
- Monthly average GHI chart
- Summary stats table

### Deployment:
Access the live dashboard here https://solar-challenge-week1-doekx4fvgadf8zrwrdemwj.streamlit.app/
