#!/usr/bin/env python3
"""
Data adapter for the new energy dataset
Maps the new dataset structure to the existing project structure
"""

import pandas as pd
import numpy as np

class NewEnergyDataAdapter:
    """
    Adapter to use the new energy dataset with existing ML models
    """
    
    def __init__(self, csv_path='energy_data_new.csv'):
        self.csv_path = csv_path
        self.df = None
        
    def load_data(self):
        """Load the new dataset"""
        try:
            self.df = pd.read_csv(self.csv_path)
            print(f"✅ Loaded {len(self.df)} records from {self.csv_path}")
            return True
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False
    
    def get_countries(self):
        """Get list of available countries"""
        if self.df is None:
            self.load_data()
        return sorted(self.df['Country'].unique().tolist())
    
    def get_country_data(self, country):
        """Get data for a specific country"""
        if self.df is None:
            self.load_data()
        
        country_data = self.df[self.df['Country'] == country].copy()
        if country_data.empty:
            return None
            
        # Sort by year
        country_data = country_data.sort_values('Year')
        
        return {
            'country': country,
            'years': country_data['Year'].tolist(),
            'electricity_access': country_data['Access_to_Electricity_%'].tolist(),
            'co2_emissions': country_data['CO2_Emissions'].tolist(),
            'renewable_energy': country_data['Renewable_Energy_%'].tolist(),
            'fuel_emissions': country_data['Fuel_Emissions_Index'].tolist(),
            'latest_access': country_data['Access_to_Electricity_%'].iloc[-1],
            'latest_year': country_data['Year'].iloc[-1]
        }
    
    def get_all_data(self):
        """Get data for all countries"""
        if self.df is None:
            self.load_data()
        
        all_data = []
        for country in self.get_countries():
            country_data = self.get_country_data(country)
            if country_data:
                all_data.append(country_data)
        
        return all_data
    
    def get_latest_access_rates(self):
        """Get latest electricity access rates for all countries"""
        if self.df is None:
            self.load_data()
        
        # Get latest year data for each country
        latest_data = self.df.groupby('Country').apply(
            lambda x: x.loc[x['Year'].idxmax()]
        ).reset_index(drop=True)
        
        return {
            row['Country']: {
                'access_rate': row['Access_to_Electricity_%'],
                'year': row['Year'],
                'co2_emissions': row['CO2_Emissions'],
                'renewable_energy': row['Renewable_Energy_%'],
                'fuel_emissions': row['Fuel_Emissions_Index']
            }
            for _, row in latest_data.iterrows()
        }
    
    def predict_future_access(self, years_ahead=1, country=None):
        """
        Simple prediction based on trend analysis
        """
        if self.df is None:
            self.load_data()
        
        predictions = []
        countries = [country] if country else self.get_countries()
        
        for ctry in countries:
            country_data = self.df[self.df['Country'] == ctry].copy()
            if len(country_data) < 2:
                continue
                
            # Sort by year
            country_data = country_data.sort_values('Year')
            
            # Calculate trend (simple linear regression)
            years = country_data['Year'].values
            access = country_data['Access_to_Electricity_%'].values
            
            # Simple trend calculation
            if len(years) >= 2:
                trend = (access[-1] - access[-2]) / (years[-1] - years[-2])
                
                for i in range(1, years_ahead + 1):
                    future_year = years[-1] + i
                    future_access = min(100, max(0, access[-1] + (trend * i)))
                    
                    predictions.append({
                        'country': ctry,
                        'year': future_year,
                        'predicted_access': future_access,
                        'trend': trend
                    })
        
        return predictions
    
    def get_summary_stats(self):
        """Get summary statistics"""
        if self.df is None:
            self.load_data()
        
        return {
            'total_records': len(self.df),
            'countries': self.df['Country'].nunique(),
            'year_range': f"{self.df['Year'].min()} - {self.df['Year'].max()}",
            'avg_access_rate': self.df['Access_to_Electricity_%'].mean(),
            'avg_co2_emissions': self.df['CO2_Emissions'].mean(),
            'avg_renewable_energy': self.df['Renewable_Energy_%'].mean(),
            'countries_100_access': len(self.df[self.df['Access_to_Electricity_%'] == 100]['Country'].unique()),
            'countries_below_50_access': len(self.df[self.df['Access_to_Electricity_%'] < 50]['Country'].unique())
        }

# Example usage
if __name__ == "__main__":
    adapter = NewEnergyDataAdapter()
    
    if adapter.load_data():
        print("\n📊 Summary Statistics:")
        stats = adapter.get_summary_stats()
        for key, value in stats.items():
            print(f"   {key}: {value}")
        
        print("\n🌍 Available Countries:")
        countries = adapter.get_countries()
        for country in countries:
            data = adapter.get_country_data(country)
            print(f"   {country}: {data['latest_access']}% access in {data['latest_year']}")
        
        print("\n🔮 Future Predictions (2021):")
        predictions = adapter.predict_future_access(1)
        for pred in predictions:
            print(f"   {pred['country']}: {pred['predicted_access']:.1f}% (trend: {pred['trend']:+.1f}%/year)")
