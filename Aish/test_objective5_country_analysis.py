#!/usr/bin/env python3
"""
Test script for Objective 5 Country Analysis
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from objective5_country_analysis import get_objective5_analysis

def test_country_analysis():
    """Test the country analysis functionality"""
    print("🚀 Testing Objective 5 Country Analysis")
    print("="*50)
    
    # Use the CSV file path
    csv_path = "global-data-on-sustainable-energy.csv"
    
    # Test 1: Get general analysis (no specific country)
    print("📊 Test 1: General Analysis")
    result = get_objective5_analysis(csv_path)
    
    if result['success']:
        print(f"✅ Analysis successful")
        print(f"🏆 Best Model: {result['best_model']}")
        print(f"📈 MSE Scores: {result['mse_scores']}")
        print(f"🌍 Available Countries: {len(result['countries'])}")
        print(f"📋 First 5 countries: {result['countries'][:5]}")
        
        # Test 2: Specific country analysis
        if result['countries']:
            test_country = result['countries'][0]  # Use first country
            print(f"\n📍 Test 2: Country Analysis for {test_country}")
            
            country_result = get_objective5_analysis(csv_path, test_country)
            
            if country_result['success']:
                print(f"✅ Country analysis successful")
                print(f"🏆 Best Model: {country_result['best_model']}")
                
                # Check historical data
                historical = country_result.get('historical_data', [])
                print(f"📊 Historical data points: {len(historical)}")
                if historical:
                    print(f"   Years: {historical[0]['Year']} - {historical[-1]['Year']}")
                    print(f"   Access range: {min(d['Access to electricity (% of population)'] for d in historical):.1f}% - {max(d['Access to electricity (% of population)'] for d in historical):.1f}%")
                
                # Check future predictions
                predictions = country_result.get('future_predictions', [])
                print(f"🔮 Future predictions: {len(predictions)}")
                if predictions:
                    print(f"   Prediction years: {predictions[0]['Year']} - {predictions[-1]['Year']}")
                    print(f"   Predicted access range: {min(d['Access to electricity (% of population)'] for d in predictions):.1f}% - {max(d['Access to electricity (% of population)'] for d in predictions):.1f}%")
                
                # Check combined data
                combined = country_result.get('combined_data', [])
                print(f"📈 Combined data points: {len(combined)}")
                if combined:
                    historical_points = len([d for d in combined if d['Type'] == 'Historical'])
                    predicted_points = len([d for d in combined if d['Type'] == 'Predicted'])
                    print(f"   Historical: {historical_points}, Predicted: {predicted_points}")
                
                print(f"✅ All tests passed for {test_country}!")
                
            else:
                print(f"❌ Country analysis failed: {country_result['error']}")
        
        # Test 3: Invalid country
        print(f"\n🚫 Test 3: Invalid Country Analysis")
        invalid_result = get_objective5_analysis(csv_path, "NonExistentCountry")
        if invalid_result['success']:
            if not invalid_result.get('historical_data') and not invalid_result.get('future_predictions'):
                print("✅ Correctly handled invalid country (no data returned)")
            else:
                print("⚠️ Invalid country returned data (unexpected)")
        else:
            print(f"✅ Correctly failed for invalid country: {invalid_result['error']}")
            
    else:
        print(f"❌ General analysis failed: {result['error']}")
        return False
    
    print("\n" + "="*50)
    print("🎉 All tests completed!")
    return True

if __name__ == "__main__":
    try:
        test_country_analysis()
    except Exception as e:
        print(f"❌ Test failed with exception: {e}")
        import traceback
        traceback.print_exc()