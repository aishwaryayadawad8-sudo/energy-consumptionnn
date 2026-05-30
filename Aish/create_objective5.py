#!/usr/bin/env python3
"""Script to create objective5.html"""

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Objective 5: SDG 7 Electricity Access Forecasting</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); min-height: 100vh; padding: 20px 0; }
        .dashboard-container { max-width: 1400px; margin: 0 auto; }
        .header-section { background: white; border-radius: 15px; padding: 30px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
        .back-btn { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; border: none; padding: 10px 20px; border-radius: 50px; margin-bottom: 15px; }
        .section-card { background: white; border-radius: 15px; padding: 25px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
        .section-title { color: #2c3e50; font-weight: bold; margin-bottom: 20px; font-size: 1.5rem; }
        .chart-container { position: relative; height: 450px; margin-top: 20px; }
        .btn-load { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; border: none; padding: 12px 30px; border-radius: 50px; font-weight: bold; }
        .loading { text-align: center; padding: 40px