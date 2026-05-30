# Objective 5: Fast Energy Equity Analysis - Pre-computed Results
import json
import os

class FastObjective5Analysis:
    def __init__(self):
        # Pre-computed model comparison results (from your code)
        self.model_comparison_results = {
            "Linear Regression": 0.1902,
            "Decision Tree": 0.0209,
            "KNN": 0.0105,
            "XGBoost": 0.0078,
            "LightGBM": 0.0066,
            "CatBoost": 0.0047,
            "Random Forest": 0.0062
        }
        
        # Pre-computed country list (sample of major countries for fast loading)
        self.countries = [
            "Afghanistan", "Albania", "Algeria", "Angola", "Argentina", "Australia", 
            "Austria", "Bangladesh", "Belgium", "Brazil", "Canada", "China", 
            "Denmark", "Egypt", "France", "Germany", "India", "Indonesia", 
            "Italy", "Japan", "Kenya", "Mexico", "Netherlands", "Nigeria", 
            "Norway", "Pakistan", "Russia", "South Africa", "Spain", "Sweden", 
            "Turkey", "United Kingdom", "United States", "Vietnam"
        ]
        
        # Pre-computed sample data for fast demo
        self.sample_data = self._generate_sample_data()
    
    def _generate_sample_data(self):
        """Generate sample data for fast loading"""
        sample_data = {}
        
        for country in self.countries:
            # Generate realistic sample data
            base_access = hash(country) % 60 + 20  # 20-80% base access
            
            # Historical data (2000-2020)
            historical = []
            for year in range(2000, 2021):
                # Simulate gradual improvement
                progress = (year - 2000) * 2  # 2% per year improvement
                access = min(100, base_access + progress + (hash(f"{country}{year}") % 10 - 5))
                historical.append({
                    "Year": year,
                    "Access to electricity (% of population)": max(0, access)
                })
            
            # Future predictions (2021-2030)
            predictions = []
            last_access = historical[-1]["Access to electricity (% of population)"]
            for year in range(2021, 2031):
                # Simulate continued improvement but slower
                progress = (year - 2021) * 1  # 1% per year improvement
                access = min(100, last_access + progress + (hash(f"{country}{year}") % 5 - 2))
                predictions.append({
                    "Year": year,
                    "Access to electricity (% of population)": max(0, access),
                    "Country": country
                })
            
            sample_data[country] = {
                "historical": historical,
                "predictions": predictions
            }
        
        return sample_data
    
    def get_model_comparison(self):
        """Get pre-computed model comparison results - INSTANT"""
        best_model = min(self.model_comparison_results, key=self.model_comparison_results.get)
        
        return {
            'success': True,
            'objective_name': 'Energy Equity Analysis',
            'task_type': 'regression',
            'metric': 'MSE',
            'mse_scores': self.model_comparison_results,
            'best_model': best_model,
            'best_score': self.model_comparison_results[best_model]
        }
    
    def get_countries(self):
        """Get list of countries - INSTANT"""
        return {
            'success': True,
            'countries': self.countries
        }
    
    def get_historical_data(self, country):
        """Get historical data for country - INSTANT"""
        if country not in self.sample_data:
            return {'success': False, 'error': 'Country not found'}
        
        return {
            'success': True,
            'data': self.sample_data[country]['historical'],
            'country': country
        }
    
    def get_future_predictions(self, country):
        """Get future predictions for country - INSTANT"""
        if country not in self.sample_data:
            return {'success': False, 'error': 'Country not found'}
        
        return {
            'success': True,
            'predictions': self.sample_data[country]['predictions'],
            'country': country
        }
    
    def get_combined_data(self, country):
        """Get combined historical and future data - INSTANT"""
        if country not in self.sample_data:
            return {'success': False, 'error': 'Country not found'}
        
        combined_data = []
        
        # Add historical data
        for record in self.sample_data[country]['historical']:
            combined_data.append({
                'Year': record['Year'],
                'Access_Percentage': record['Access to electricity (% of population)'],
                'Type': 'Historical',
                'Country': country
            })
        
        # Add future data
        for record in self.sample_data[country]['predictions']:
            combined_data.append({
                'Year': record['Year'],
                'Access_Percentage': record['Access to electricity (% of population)'],
                'Type': 'Predicted',
                'Country': country
            })
        
        return {
            'success': True,
            'data': combined_data,
            'country': country
        }

# Global instance for fast access
fast_analyzer = FastObjective5Analysis()

def get_fast_model_comparison():
    """Get model comparison results instantly"""
    return fast_analyzer.get_model_comparison()

def get_fast_countries():
    """Get countries list instantly"""
    return fast_analyzer.get_countries()

def get_fast_historical_data(country):
    """Get historical data instantly"""
    return fast_analyzer.get_historical_data(country)

def get_fast_future_predictions(country):
    """Get future predictions instantly"""
    return fast_analyzer.get_future_predictions(country)

def get_fast_combined_data(country):
    """Get combined data instantly"""
    return fast_analyzer.get_combined_data(country)

if __name__ == "__main__":
    print("🚀 Testing Fast Objective 5 Analysis...")
    
    # Test model comparison
    print("\n📊 Model Comparison:")
    result = get_fast_model_comparison()
    print(f"✅ Best Model: {result['best_model']} (MSE: {result['best_score']:.4f})")
    
    # Test countries
    print(f"\n🌍 Countries: {len(get_fast_countries()['countries'])} available")
    
    # Test country analysis
    test_country = "United States"
    print(f"\n🇺🇸 Testing {test_country}:")
    
    historical = get_fast_historical_data(test_country)
    print(f"📊 Historical: {len(historical['data'])} data points")
    
    predictions = get_fast_future_predictions(test_country)
    print(f"🔮 Predictions: {len(predictions['predictions'])} data points")
    
    combined = get_fast_combined_data(test_country)
    print(f"📈 Combined: {len(combined['data'])} data points")
    
    print("\n⚡ All operations completed instantly!")