"""
XGBoost-Based Automatic Alert System
Uses XGBoost ML model to predict electricity access and send alerts
"""

import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')


class XGBoostAlertSystem:
    """
    XGBoost ML model for electricity access prediction and automatic alerts
    """
    
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.model = None
        self.feature_columns = []
        self.model_accuracy = 0
        self.model_mse = 0
        
    def load_and_prepare_data(self):
        """Load and prepare data for XGBoost training"""
        df = pd.read_csv(self.csv_path)
        
        # Select features for prediction
        potential_features = [
            'Year',
            'Access to clean fuels for cooking',
            'Renewable energy share in the total final energy consumption (%)',
            'Electricity from fossil fuels (TWh)',
            'Electricity from nuclear (TWh)',
            'Electricity from renewables (TWh)',
            'Low-carbon electricity (% electricity)',
            'Primary energy consumption per capita (kWh/person)',
            'Energy intensity level of primary energy (MJ/$2017 PPP GDP)',
            'Value_co2_emissions_kt_by_country',
            'gdp_growth',
            'gdp_per_capita',
            'Land Area(Km2)',
            'Latitude',
            'Longitude'
        ]
        
        # Filter available columns and ensure they are numeric
        self.feature_columns = []
        for col in potential_features:
            if col in df.columns:
                # Convert to numeric, coercing errors to NaN
                df[col] = pd.to_numeric(df[col], errors='coerce')
                self.feature_columns.append(col)
        
        # Prepare data
        df_clean = df[self.feature_columns + ['Entity', 'Access to electricity (% of population)']].copy()
        
        # Ensure target is numeric
        df_clean['Access to electricity (% of population)'] = pd.to_numeric(
            df_clean['Access to electricity (% of population)'], errors='coerce'
        )
        
        # Drop rows with NaN values
        df_clean = df_clean.dropna()
        
        X = df_clean[self.feature_columns]
        y = df_clean['Access to electricity (% of population)']
        
        print(f"✅ Data loaded: {len(X)} samples, {len(self.feature_columns)} features")
        
        return X, y, df_clean
    
    def train_xgboost_model(self):
        """Train XGBoost model"""
        print("\n🚀 Training XGBoost Model...")
        print("=" * 70)
        
        # Load data
        X, y, df_clean = self.load_and_prepare_data()
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Initialize XGBoost
        self.model = XGBRegressor(
            n_estimators=1000,
            learning_rate=0.1,
            max_depth=6,
            min_child_weight=1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            verbosity=0
        )
        
        # Train model
        print("📊 Training XGBoost...")
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred_train = self.model.predict(X_train)
        y_pred_test = self.model.predict(X_test)
        
        mse_train = mean_squared_error(y_train, y_pred_train)
        mse_test = mean_squared_error(y_test, y_pred_test)
        rmse_test = np.sqrt(mse_test)
        r2_test = r2_score(y_test, y_pred_test)
        
        self.model_mse = mse_test
        self.model_accuracy = r2_test * 100
        
        print(f"\n✅ XGBoost Model Trained Successfully!")
        print(f"   MSE (Train): {mse_train:.2f}")
        print(f"   MSE (Test): {mse_test:.2f}")
        print(f"   RMSE (Test): {rmse_test:.2f}")
        print(f"   R² Score: {r2_test:.4f}")
        print(f"   Accuracy: {self.model_accuracy:.2f}%")
        print("=" * 70)
        
        return self
    
    def predict_country_access(self, country_name, year=2024):
        """
        Predict electricity access for a specific country
        
        Args:
            country_name: Name of the country
            year: Year to predict for
            
        Returns:
            dict: Prediction results
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_xgboost_model() first.")
        
        # Load data
        df = pd.read_csv(self.csv_path)
        
        # Get latest data for country
        country_data = df[df['Entity'] == country_name].sort_values('Year').tail(1)
        
        if country_data.empty:
            return {
                'found': False,
                'country': country_name,
                'message': f'No data found for {country_name}'
            }
        
        # Prepare features
        X_pred = country_data[self.feature_columns]
        
        # Make prediction
        predicted_access = self.model.predict(X_pred)[0]
        
        # Get current access
        current_access = country_data['Access to electricity (% of population)'].values[0]
        
        # Determine alert status
        if predicted_access < 50:
            status = 'critical'
            alert_type = 'urgent'
        elif predicted_access < 75:
            status = 'needs_improvement'
            alert_type = 'reminder'
        elif predicted_access >= 95:
            status = 'excellent'
            alert_type = 'congratulations'
        else:
            status = 'good'
            alert_type = 'status_update'
        
        return {
            'found': True,
            'country': country_name,
            'year': year,
            'current_access': float(current_access),
            'predicted_access': float(predicted_access),
            'change': float(predicted_access - current_access),
            'status': status,
            'alert_type': alert_type,
            'model': 'XGBoost',
            'model_accuracy': self.model_accuracy
        }
    
    def predict_all_countries(self, year=2024):
        """
        Predict electricity access for all countries
        
        Returns:
            list: Predictions for all countries
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_xgboost_model() first.")
        
        # Load data
        df = pd.read_csv(self.csv_path)
        
        # Get latest data for each country
        latest_data = df.groupby('Entity').last().reset_index()
        
        predictions = []
        
        for _, row in latest_data.iterrows():
            country = row['Entity']
            
            try:
                # Prepare features
                X_pred = row[self.feature_columns].values.reshape(1, -1)
                
                # Make prediction
                predicted_access = self.model.predict(X_pred)[0]
                
                # Get current access
                current_access = row['Access to electricity (% of population)']
                
                # Determine status
                if predicted_access < 50:
                    status = 'critical'
                    alert_type = 'urgent'
                elif predicted_access < 75:
                    status = 'needs_improvement'
                    alert_type = 'reminder'
                elif predicted_access >= 95:
                    status = 'excellent'
                    alert_type = 'congratulations'
                else:
                    status = 'good'
                    alert_type = 'status_update'
                
                predictions.append({
                    'country': country,
                    'year': year,
                    'current_access': float(current_access),
                    'predicted_access': float(predicted_access),
                    'change': float(predicted_access - current_access),
                    'status': status,
                    'alert_type': alert_type
                })
                
            except Exception as e:
                print(f"⚠️  Error predicting for {country}: {e}")
                continue
        
        return predictions
    
    def send_automatic_alerts(self):
        """
        Automatically send alerts based on XGBoost predictions
        
        Returns:
            dict: Summary of alerts sent
        """
        print("\n📧 Generating Automatic Alerts with XGBoost...")
        print("=" * 70)
        
        # Get predictions for all countries
        predictions = self.predict_all_countries()
        
        # Import email system
        try:
            from email_alerts import SDG7EmailAlerts
            alert_system = SDG7EmailAlerts()
        except:
            print("⚠️  Email system not available")
            return {
                'success': False,
                'message': 'Email system not available',
                'predictions': predictions
            }
        
        # Send alerts
        alerts_sent = []
        
        for pred in predictions:
            country = pred['country']
            access = pred['predicted_access']
            status = pred['status']
            
            # Check if we have email for this country
            if country not in alert_system.COUNTRY_EMAILS:
                continue
            
            # Only send for critical, needs_improvement, or excellent
            if status in ['critical', 'needs_improvement', 'excellent']:
                # Generate email content
                subject, body = alert_system.generate_email_content(
                    country, access, status, 'developing', pred['year']
                )
                
                email = alert_system.COUNTRY_EMAILS[country]
                
                # Send email
                success = alert_system.send_email(
                    email, subject, body, country_name=country, log_to_db=True
                )
                
                if success:
                    alerts_sent.append({
                        'country': country,
                        'email': email,
                        'status': status,
                        'access': access,
                        'year': pred['year'],
                        'subject': subject,
                        'model': 'XGBoost'
                    })
        
        print(f"\n✅ Sent {len(alerts_sent)} alerts using XGBoost predictions")
        print("=" * 70)
        
        return {
            'success': True,
            'total_predictions': len(predictions),
            'alerts_sent': len(alerts_sent),
            'model': 'XGBoost',
            'model_accuracy': self.model_accuracy,
            'alerts': alerts_sent
        }
    
    def get_model_info(self):
        """Get information about the trained model"""
        if self.model is None:
            return {'trained': False}
        
        return {
            'trained': True,
            'model_type': 'XGBoost',
            'n_features': len(self.feature_columns),
            'features': self.feature_columns,
            'mse': self.model_mse,
            'accuracy': self.model_accuracy
        }


# Test function
if __name__ == '__main__':
    print("🧪 Testing XGBoost Alert System")
    print("=" * 70)
    
    # Initialize
    alert_system = XGBoostAlertSystem('../global-data-on-sustainable-energy.csv')
    
    # Train model
    alert_system.train_xgboost_model()
    
    # Test prediction for a specific country
    print("\n📊 Testing Prediction for Kenya:")
    result = alert_system.predict_country_access('Kenya')
    print(f"   Current Access: {result['current_access']:.2f}%")
    print(f"   Predicted Access: {result['predicted_access']:.2f}%")
    print(f"   Status: {result['status']}")
    print(f"   Alert Type: {result['alert_type']}")
    
    # Get all predictions
    print("\n📊 Generating Predictions for All Countries...")
    predictions = alert_system.predict_all_countries()
    print(f"   Total Predictions: {len(predictions)}")
    
    # Show sample predictions
    print("\n📋 Sample Predictions:")
    for pred in predictions[:5]:
        print(f"   {pred['country']:20s} - {pred['predicted_access']:5.1f}% ({pred['status']})")
    
    print("\n✅ XGBoost Alert System Ready!")
