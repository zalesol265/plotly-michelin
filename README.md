# Michelin Star Restaurant Dash App

This is an interactive Dash web application that visualizes the Michelin Star restaurants dataset, offering insights into restaurant locations, awards, and cuisines. It utilizes Plotly maps for geospatial analysis and interactive data filtering, allowing users to explore Michelin-starred restaurants worldwide.

## Features

- **Interactive Map Visualization**: Displays Michelin Star restaurants on a map using Plotly's MapLibre integration, with filters for cuisine type, price, Michelin star rating, and eco-friendly (GreenStar) ratings.
- **Restaurant Insights**: Explore key statistics, such as the distribution of Michelin stars across different cuisines and regions, with additional breakdowns by country and city.
- **Responsive Design**: The app is mobile-friendly and provides a clean, intuitive interface for exploring Michelin restaurant data.
- **Future Integration**: Potential for integration of Large Language Models (LLMs) for enhanced data insights and natural language querying of the dataset.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.7+**
- **Git** (if cloning the repository from GitHub)

### Setup Instructions

1. **Clone the repository**:
   If you're using Git, run the following command:
   ```bash
   git clone https://github.com/your-username/michelin-star-dash-app.git
   cd michelin-star-dash-app


2. **Create and activate a virtual environment**:
   - For Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - For macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:
   With the virtual environment activated, install the required dependencies using:
   ```bash
   pip install -r requirements.txt
4. **Run the Dash app**:
   Once all dependencies are installed, start the app:
   ```bash
   python app.py
5. **Access the app**: Open your web browser and go to:
    ```bash
    http://127.0.0.1:8050/
    