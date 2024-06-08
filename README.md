# Random Forest Regressor for Spectral Reflectance Prediction

## Overview

This Streamlit application allows users to build, train, validate, and use a Random Forest model to predict one spectral reflectance band based on others from a given dataset. The interface is user-friendly, providing easy selections for input and output variables, adjusting test data rate, and visualizing model performance and feature importance.

## Prerequisites

Ensure you have the following libraries installed:

- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `numpy`

Install the required libraries using:

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn numpy
```

## Instructions to Run the Application

1. **Run the Streamlit application**:
    ```bash
    streamlit run streamlit_app.py
    ```

## Features

### Sidebar

- **Variable Selection**: Select one output variable (target) and at least one input variable (features).
- **Test Data Rate**: Adjust the rate of test data using a slider.

### Main Page

1. **Title and Description**: Provides an overview of the application.
2. **Dataset Information**: Details about the dataset used.
3. **Model Information**: Displays selected output variable, input variables, training data shape, and test data shape.
4. **Scatter Plot**: Scatter plot comparing predicted vs. observed values for the test data, showing R-squared and RMSE values.
5. **Feature Importance Chart**: Bar chart showing the importance of each feature in the model.
6. **Model Prediction**: 
   - User input fields for entering values of input variables.
   - Displays the predicted value of the output variable.
   - Bar chart showing the predicted output value.



## License

This project is licensed under the MIT License. See the LICENSE file for details.