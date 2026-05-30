"""
Add this code to sustainable_energy/dashboard/views.py
This integrates XGBoost with automatic alert sending
"""

# Add these imports at the top of views.py
"""
from ml_models.xgboost_alert_system import XGBoostAlertSystem
from ml_models.email_templates import EmailTemplates
"""

# Add this new view function

def send_xgboost_alerts(request):
    """
    API: Train XGBoost model, show comparison, and send automatic alerts
    """
    try:
        from ml_models.xgboost_alert_system import XGBoostAlertSystem
        from ml_models.email_alerts import SDG7EmailAlerts
        from ml_models.email_templates import EmailTemplates
        
        # Step 1: Initialize XGBoost system
        xgboost_system = XGBoostAlertSystem(CSV_PATH)
        
        # Step 2: Train XGBoost model
        xgboost_system.train_xgboost_model()
        
        # Step 3: Get predictions for all countries
        predictions = xgboost_system.predict_all_countries()
        
        # Step 4: Initialize email system
        email_system = SDG7EmailAlerts()
        
        # Step 5: Send alerts based on XGBoost predictions
        alerts_sent = []
        
        for pred in predictions:
            country = pred['country']
            access = pred['predicted_access']
            status = pred['status']
            alert_type = pred['alert_type']
            year = pred['year']
            
            # Check if we have email for this country
            if country not in email_system.COUNTRY_EMAILS:
                continue
            
            # Only send for critical, needs_improvement, or excellent
            if status in ['critical', 'needs_improvement', 'excellent']:
                # Get appropriate template
                subject, body = EmailTemplates.get_template_by_type(
                    alert_type, country, access, year
                )
                
                email = email_system.COUNTRY_EMAILS[country]
                
                # Send email
                success = email_system.send_email(
                    email, subject, body, country_name=country, log_to_db=True
                )
                
                if success:
                    alerts_sent.append({
                        'country': country,
                        'email': email,
                        'status': status,
                        'alert_type': alert_type,
                        'access': float(access),
                        'year': year,
                        'subject': subject,
                        'model': 'XGBoost',
                        'template_used': alert_type
                    })
        
        # Step 6: Get model info
        model_info = xgboost_system.get_model_info()
        
        # Step 7: Return results
        return JsonResponse({
            'success': True,
            'model': 'XGBoost',
            'model_accuracy': model_info['accuracy'],
            'model_mse': model_info['mse'],
            'total_predictions': len(predictions),
            'alerts_sent': len(alerts_sent),
            'alerts': alerts_sent,
            'message': f'XGBoost model trained with {model_info["accuracy"]:.2f}% accuracy. Sent {len(alerts_sent)} automatic alerts!'
        })
        
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print("="*60)
        print("ERROR in send_xgboost_alerts:")
        print(error_details)
        print("="*60)
        return JsonResponse({
            'success': False,
            'error': str(e),
            'details': error_details
        }, status=500)


# Add this URL pattern to urls.py
"""
path('api/send-xgboost-alerts/', views.send_xgboost_alerts, name='send_xgboost_alerts'),
"""
