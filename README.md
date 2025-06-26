# Survey Insights

A machine learning application for analyzing and predicting survey results.

## Technologies Used

- **Frontend**: Streamlit - A powerful Python library for creating web applications
- **Data Processing**: Pandas - For data manipulation and analysis
- **Machine Learning**: Scikit-learn - For building and training predictive models
- **Data Visualization**: Built-in Streamlit components
- **Jupyter Notebook**: For initial data exploration and model training

## Project Structure

- `app.py`: Main application entry point
- `explore_page.py`: Data exploration interface
- `predict_page.py`: Prediction interface
- `style.py`: UI styling and configuration
- `survey_results_public.csv`: Survey dataset
- `saved_steps.pkl`: Pre-trained model
- `requirements.txt`: Project dependencies

## Requirements

- Python 3.x
- Git
- A web browser

## Installation Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/Baha-Bouazizi/Software-Developer-Salary-Prediction
   cd SurveyInsights
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

   This will start a local server and open the application in your default web browser.

## Usage

1. **Exploration Mode**
   - Use the exploration interface to analyze survey data
   - Visualize different aspects of the dataset
   - Filter and segment data as needed

2. **Prediction Mode**
   - Use the prediction interface to make predictions based on the trained model
   - Input your data and get instant predictions
   - View prediction confidence scores

## Note

- Make sure to have Python 3.x installed on your system
- Ensure you have enough RAM to process the dataset
- The application requires internet connection for initial setup but works offline once installed

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
