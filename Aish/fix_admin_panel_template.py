#!/usr/bin/env python3
"""
Fix the admin panel template
"""

template_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel - Email Alert System</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/electric-background.css' %}">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px 0;
        }
        
        .hover-card {
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .hover-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.2) !important;
        }
        
        .icon-wrapper {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
        }
        
        .card {
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        
        .btn-lg {
            padding: 12px 40px;
            border-radius: 50px;
            font-weight: bold;
        }
    </style>
</head>
<body class="electric-bg">
    <!-- Electric Shock Wave Canvas -->
    <canvas id="electric-canvas"></canvas>
    
    <!-- Main content wrapper -->
    <div class="main-content-wrapper">
        <div class="container-fluid py-4">
            <div class="row mb-4">
                <div class="col-12">
                    <div class="card shadow-lg border-0" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
                        <div class="card-body text-white text-center py-5">
                            <h1 class="display-4 mb-3">
                                <i class="fas fa-user-shield"></i> Admin Panel
                            </h1>
                            <p class="lead">Email Alert System Management</p>
                            <div class="mt-3">
                                <span class="badge bg-light text-dark px-3 py-2">
                                    <i class="fas fa-user"></i> {{ user.username }}
                                </span>
                                <a href="{% url 'admin_logout' %}" class="btn btn-outline-light ms-3">
                                    <i class="fas fa-sign-out-alt"></i> Logout
                                </a>
                                <a href="{% url 'objective_selector' %}" class="btn btn-outline-light ms-2">
                                    <i class="fas fa-home"></i> Home
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <!-- Email Alert System Card -->
                <div class="col-md-6 mb-4">
                    <div class="card shadow-lg border-0 h-100 hover-card">
                        <div class="card-body text-center p-5" style="background: white;">
                            <div class="icon-wrapper mb-4">
                                <i class="fas fa-envelope fa-5x text-primary"></i>
                            </div>
                            <h3 class="card-title mb-3">
                                <i class="fas fa-paper-plane"></i> Email Alert System
                            </h3>
                            <p class="card-text text-muted mb-4">
                                Send electricity access alerts to multiple countries at once
                            </p>
                            <ul class="list-unstyled text-start mb-4">
                                <li class="mb-2">
                                    <i class="fas fa-check-circle text-success"></i> Select multiple countries
                                </li>
                                <li class="mb-2">
                                    <i class="fas fa-check-circle text-success"></i> Automated analysis
                                </li>
                                <li class="mb-2">
                                    <i class="fas fa-check-circle text-success"></i> Customized emails
                                </li>
                            </ul>
                            <a href="{% url 'objective8_dashboard' %}" class="btn btn-primary btn-lg">
                                <i class="fas fa-paper-plane"></i> Send Alerts
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Email Logs Card -->
                <div class="col-md-6 mb-4">
                    <div class="card shadow-lg border-0 h-100 hover-card">
                        <div class="card-body text-center p-5" style="background: white;">
                            <div class="icon-wrapper mb-4">
                                <i class="fas fa-list-alt fa-5x text-info"></i>
                            </div>
                            <h3 class="card-title mb-3">
                                <i class="fas fa-history"></i> Email Logs
                            </h3>
                            <p class="card-text text-muted mb-4">
                                View history of all sent email alerts
                            </p>
                            <ul class="list-unstyled text-start mb-4">
                                <li class="mb-2">
                                    <i class="fas fa-check-circle text-success"></i> Track sent emails
                                </li>
                                <li class="mb-2">
                                    <i class="fas fa-check-circle text-success"></i> View status
                                </li>
                                <li class="mb-2">
                                    <i class="fas fa-check-circle text-success"></i> Monitor delivery
                                </li>
                            </ul>
                            <a href="{% url 'email_logs_dashboard' %}" class="btn btn-info btn-lg">
                                <i class="fas fa-list-alt"></i> View Logs
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <!-- Send to Single Country Card -->
                <div class="col-md-4 mb-4">
                    <div class="card shadow border-0 h-100 hover-card">
                        <div class="card-body text-center p-4" style="background: white;">
                            <div class="icon-wrapper mb-3">
                                <i class="fas fa-flag fa-3x text-warning"></i>
                            </div>
                            <h5 class="card-title mb-3">
                                <i class="fas fa-envelope-open-text"></i> Single Country Alert
                            </h5>
                            <p class="card-text text-muted small mb-3">
                                Send alert to one specific country
                            </p>
                            <a href="{% url 'send_email_single_country' %}" class="btn btn-warning">
                                <i class="fas fa-paper-plane"></i> Send
                            </a>
                        </div>
                    </div>
                </div>

                <!-- Custom Alert Card -->
                <div class="col-md-4 mb-4">
                    <div class="card shadow border-0 h-100 hover-card">
                        <div class="card-body text-center p-4" style="background: white;">
                            <div class="icon-wrapper mb-3">
                                <i class="fas fa-edit fa-3x text-success"></i>
                            </div>
                            <h5 class="card-title mb-3">
                                <i class="fas fa-pen-fancy"></i> Custom Alert
                            </h5>
                            <p class="card-text text-muted small mb-3">
                                Create and send custom email alerts
                            </p>
                            <a href="{% url 'send_custom_alert_page' %}" class="btn btn-success">
                                <i class="fas fa-edit"></i> Create
                            </a>
                        </div>
                    </div>
                </div>

                <!-- XGBoost Alerts Card -->
                <div class="col-md-4 mb-4">
                    <div class="card shadow border-0 h-100 hover-card">
                        <div class="card-body text-center p-4" style="background: white;">
                            <div class="icon-wrapper mb-3">
                                <i class="fas fa-robot fa-3x text-danger"></i>
                            </div>
                            <h5 class="card-title mb-3">
                                <i class="fas fa-brain"></i> XGBoost Alerts
                            </h5>
                            <p class="card-text text-muted small mb-3">
                                AI-powered automatic alert system
                            </p>
                            <button class="btn btn-danger" onclick="sendXGBoostAlerts()">
                                <i class="fas fa-robot"></i> Auto Send
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Electric Animation Script -->
    <script src="{% static 'js/electric-animation.js' %}"></script>
    
    <script>
    function sendXGBoostAlerts() {
        if (!confirm('Send XGBoost alerts to all countries with low electricity access?')) {
            return;
        }
        
        fetch('/api/send-xgboost-alerts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(`Success! Sent ${data.emails_sent} alerts to countries with low access.`);
            } else {
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            alert('Error sending alerts: ' + error);
        });
    }
    </script>
</body>
</html>
'''

# Write the fixed template
with open('sustainable_energy/dashboard/templates/dashboard/admin_panel.html', 'w', encoding='utf-8') as f:
    f.write(template_content)

print("✅ Fixed admin panel template")