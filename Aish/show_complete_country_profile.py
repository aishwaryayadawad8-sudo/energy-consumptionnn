#!/usr/bin/env python3
"""
Show Complete Country Profile
============================

This script modifies the dashboard to show the complete country profile
with all charts as shown in the screenshot - country header, status, 
metric cards, and all trend charts.
"""

import os

def show_complete_country_profile():
    """Modify dashboard to show complete country profile layout"""
    
    html_file_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("📊 SHOWING COMPLETE COUNTRY PROFILE")
    print("=" * 50)
    print(f"📁 Updating file: {html_file_path}")
    
    # Read current file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add CSS for the complete profile layout
    css_addition = '''        
        .country-profile-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .country-profile-header h2 {
            margin: 0;
            font-size: 1.8rem;
            font-weight: 600;
        }
        
        .country-profile-header .flag-icon {
            font-size: 1.5rem;
            margin-right: 10px;
        }
        
        .status-card {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-left: 4px solid #28a745;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        }
        
        .status-card h5 {
            margin: 0 0 5px 0;
            color: #155724;
            font-weight: 600;
        }
        
        .status-card p {
            margin: 0;
            color: #155724;
            font-size: 0.9rem;
        }
        
        .status-icon {
            color: #28a745;
            margin-right: 8px;
        }
        
        .metric-cards-2x2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .metric-card-large {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 1