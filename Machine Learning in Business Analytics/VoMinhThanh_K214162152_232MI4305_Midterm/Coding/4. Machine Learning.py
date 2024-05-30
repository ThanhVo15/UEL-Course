from flask import Flask
from flask_mysqldb import MySQL
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Obama123'
app.config['MYSQL_DB'] = 'retails'

mysql.init_app(app)


def queryDataset(sql):
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


def preprocess_data(df):
    pass


if __name__ == '__main__':
    with app.app_context():
        # Fetch data from the database
        sql = "SELECT o.CustomerID, SUM(od.OrderQty) AS TotalItemsPurchased, SUM(od.OrderQty * od.UnitPrice) AS TotalAmountSpent " \
              "FROM orders o " \
              "JOIN orderdetails od ON o.OrderId = od.OrderId " \
              "GROUP BY o.CustomerID;"

        df = queryDataset(sql)
        if df is not None:
            df.columns = ['CustomerId', 'TotalItemsPurchased', 'TotalAmountSpent']

            # Preprocess the data
            preprocess_data(df)

            # Define features (X) and target variable (y)
            X = df[['TotalItemsPurchased', 'TotalAmountSpent']]
            y = df['CustomerId']  # Assuming we want to predict customer behavior

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Standardize features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            # Initialize and train the logistic regression model
            model = LogisticRegression()
            model.fit(X_train_scaled, y_train)

            # Make predictions
            y_pred = model.predict(X_test_scaled)

            # Evaluate the model
            accuracy = accuracy_score(y_test, y_pred)
            report = classification_report(y_test, y_pred)
            print("Accuracy:", accuracy)
            print("Classification Report:\n", report)

            # Print predictions
            print("Predictions:", y_pred)
        else:
            print("Failed to fetch data.")
