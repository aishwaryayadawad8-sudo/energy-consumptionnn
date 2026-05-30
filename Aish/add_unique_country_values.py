#!/usr/bin/env python3
"""
Add unique, realistic values for each country's graphs
"""

import os

def add_unique_country_values():
    """Update dashboard to generate unique values for each country"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Adding unique country-specific graph values...")
    print(f"📁 Updating file: {index_path}")
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add comprehensive country profiles with unique characteristics
        country_profiles = '''
        // Comprehensive country profiles with unique characteristics
        const countryProfiles = {
            'Afghanistan': { 
                development: 'low', renewableBase: 15, growthRate: 0.8, volatility: 'high',
                fossilDominance: 85, nuclearCapacity: 0, hydroPotential: 25
            },
            'Albania': { 
                development: 'medium', renewableBase: 95, growthRate: 1.2, volatility: 'low',
                fossilDominance: 5, nuclearCapacity: 0, hydroPotential: 90
            },
            'Algeria': { 
                development: 'medium', renewableBase: 8, growthRate: 2.1, volatility: 'medium',
                fossilDominance: 92, nuclearCapacity: 0, hydroPotential: 5
            },
            'Argentina': { 
                development: 'high', renewableBase: 35, growthRate: 1.8, volatility: 'medium',
                fossilDominance: 55, nuclearCapacity: 10, hydroPotential: 45
            },
            'Australia': { 
                development: 'high', renewableBase: 28, growthRate: 3.2, volatility: 'low',
                fossilDominance: 62, nuclearCapacity: 0, hydroPotential: 15
            },
            'Austria': { 
                development: 'high', renewableBase: 78, growthRate: 2.5, volatility: 'low',
                fossilDominance: 22, nuclearCapacity: 0, hydroPotential: 65
            },
            'Bangladesh': { 
                development: 'low', renewableBase: 12, growthRate: 4.5, volatility: 'high',
                fossilDominance: 88, nuclearCapacity: 0, hydroPotential: 8
            },
            'Belgium': { 
                development: 'high', renewableBase: 25, growthRate: 1.8, volatility: 'low',
                fossilDominance: 45, nuclearCapacity: 30, hydroPotential: 5
            },
            'Brazil': { 
                development: 'high', renewableBase: 85, growthRate: 2.8, volatility: 'medium',
                fossilDominance: 15, nuclearCapacity: 2, hydroPotential: 75
            },
            'Canada': { 
                development: 'high', renewableBase: 68, growthRate: 2.2, volatility: 'low',
                fossilDominance: 22, nuclearCapacity: 15, hydroPotential: 60
            },
            'Chile': { 
                development: 'high', renewableBase: 55, growthRate: 4.2, volatility: 'medium',
                fossilDominance: 45, nuclearCapacity: 0, hydroPotential: 25
            },
            'China': { 
                development: 'high', renewableBase: 32, growthRate: 5.8, v