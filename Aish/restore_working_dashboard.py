#!/usr/bin/env python3
"""
Script to restore the complete working explore dashboard
"""

import os

def restore_working_dashboard():
    """Restore the complete working explore dashboard"""
    
    index_path = "sustainable_energy/dashboard/templates/dashboard/index.html"
    
    print("🔄 Restoring complete working explore dashboard...")
    print(f"📁 Updating file: {index_path}")
    
    # Complete working HTML content
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Explore Dashboard - SDG 7 Energy Analytics (2000-2030)</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .dashboard-container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header-section {
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }
        
        .search-section {
            background: white;
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }'''
    
    try:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("✅ Started restoring dashboard...")
        return True
        
    except Exception as e:
        print(f"❌ Error restoring dashboard: {e}")
        return False

def main():
    """Main function"""
    print("🔄 RESTORING COMPLETE EXPLORE DASHBOARD")
    print("=" * 50)
    
    success = restore_working_dashboard()
    
    if success:
        print("✅ Dashboard restoration started...")
    else:
        print("❌ Restoration failed.")

if __name__ == "__main__":
    main()