from flask import Flask
from flask_mysqldb import MySQL
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings

warnings.filterwarnings("ignore")  # Ignore warnings for demonstration purposes

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'retails'

mysql = MySQL(app)


def queryDataset(sql):
    """
    Executes the given SQL query and returns the results as a pandas DataFrame.
    """
    try:
        with app.app_context():
            cursor = mysql.connection.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            df = pd.DataFrame(results)
            return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def forecast_with_arima(series, order=(1, 1, 1)):
    """
    Forecast using ARIMA model.
    :param series: Pandas Series with datetime index and numeric values.
    :param order: tuple (p, d, q) for ARIMA model.
    :return: Pandas Series with forecasted values.
    """
    model = ARIMA(series, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=365)  # Forecast for the next year (365 days)
    return forecast


if __name__ == '__main__':
    with app.app_context():
        # Revised SQL query to comply with ONLY_FULL_GROUP_BY
        sql = """
            SELECT 
                DATE(o.OrderDate) AS OrderDate, 
                o.CustomerID, 
                SUM(od.OrderQty * od.UnitPrice) AS TotalAmountSpent 
            FROM orders o
            JOIN orderdetails od ON o.OrderId = od.OrderId
            GROUP BY DATE(o.OrderDate), o.CustomerID
            ORDER BY DATE(o.OrderDate) ASC, o.CustomerID;
            """

        df_time_series = queryDataset(sql)
        if df_time_series is not None and not df_time_series.empty:
            df_time_series.columns = ['OrderDate', 'CustomerId', 'TotalAmountSpent']
            df_time_series['OrderDate'] = pd.to_datetime(df_time_series['OrderDate'])

            forecast_results = {}
            unique_customers = df_time_series['CustomerId'].unique()

            for customer_id in unique_customers:
                customer_data = df_time_series[df_time_series['CustomerId'] == customer_id]
                customer_data.set_index('OrderDate', inplace=True)

                # Ensure daily frequency by filling missing days with zeros
                customer_data = customer_data.resample('D').asfreq().fillna(0)

                forecast = forecast_with_arima(customer_data['TotalAmountSpent'])
                forecast_results[customer_id] = forecast.tail(365)  # Keep the last 365 days

            # Print the forecast results
            for customer_id, forecast in forecast_results.items():
                print(f"\nForecasted total amount spent for Customer ID {customer_id} for the next year:")
                print(forecast)
        else:
            print("Failed to fetch data for time series forecasting.")
