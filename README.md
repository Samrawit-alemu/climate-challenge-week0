African Climate Trend Analysis (Week 0)

Strategic Data Analysis for COP32 Preparations

Project Overview

Acting as a Junior Data Analyst at EthioClimate Analytics, I have conducted an exploratory data
analysis (EDA) on historical and projected climate data (2015–2026) for five
African countries: Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.

The goal is to provide "negotiation-grade" evidence to support the Ethiopian
Ministry of Planning and Development in its role as host for COP32.

🛠 Installation and Setup (Reproducibility)

This section fulfills the Task 1 requirements.

Prerequisites

- Python 3.9 or higher
- Git

Steps

1.  Clone the repository:
    git clone https://github.com/your-username/climate-challenge-week0.git
    cd climate-challenge-week0
2.  Create and activate a virtual environment:

    # Windows

    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux

    python3 -m venv venv
    source venv/bin/activate

3.  Install dependencies:
    pip install -r requirements.txt

📂 Folder Structure

Following the suggested structure on page 6.

├── .github/
│ └── workflows/
│ └── ci.yml # CI/CD pipeline for dependency validation
├── app/
│ ├── main.py # Streamlit Dashboard UI
│ └── utils.py # Dashboard data logic
├── notebooks/
│ ├── ethiopia_eda.ipynb # Country-specific analysis
│ ├── kenya_eda.ipynb
│ ├── nigeria_eda.ipynb
│ ├── sudan_eda.ipynb
│ ├── tanzania_eda.ipynb
│ └── compare_countries.ipynb # Task 3: Regional Comparison
├── src/ # Source code for data processing
├── tests/ # Unit tests
├── requirements.txt # Python dependencies
└── README.md # Project documentation

Note: The data/ folder is excluded from version control as per privacy
protocols.

📊 Project Tasks

Task 1: Environment & CI/CD

- Initialized repository with a branching strategy (setup-task, eda-country,
  compare-countries, dashboard-dev).
- Integrated GitHub Actions to automate dependency installation checks on
  every push.

Task 2: Data Cleaning & EDA

- Processed 10+ years of climate data per country.
- Handled NASA sentinel values (-999) and performed Z-score outlier detection.
- Developed visualizations for temperature trends, bimodal rainfall patterns,
  and humidity-heat correlations.

Task 3: Regional Comparison

- Concatenated all datasets for a comparative analysis.
- Conducted ANOVA statistical testing to validate regional climate
  differences.
- Produced a Vulnerability Ranking based on extreme heat days and dry spell
  frequency.

🚀 Interactive Dashboard

To view the interactive climate dashboard:

1.  Run the following command:
    streamlit run app/main.py
2.  The dashboard allows users to filter by country, adjust year ranges, and
    interactively explore precipitation vs. temperature distributions.

📝 Key Findings for COP32

- Sudan is identified as the most thermally vulnerable nation with over 2,600
  extreme heat days.
- Nigeria faces the highest flood risk with extreme rainfall events
  exceeding 160mm.
- Ethiopia displays significant temperature volatility, requiring specialized
  "Early Warning Systems" for agriculture.

Author

Samrawit Alemu
Junior Data Analyst | EthioClimate Analytics
