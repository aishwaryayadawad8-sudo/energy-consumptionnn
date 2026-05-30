from django.urls import path
from . import views

urlpatterns = [
        path('co2-emissions/', views.co2_emissions_dashboard, name='co2_emissions_dashboard'),
        path('electricity/', views.electricity_dashboard, name='electricity_dashboard'),
        path('total-energy/', views.total_energy_dashboard, name='total_energy_dashboard'),
    path('', views.objective_selector, name='index'),  # Objective selector is now main page
        path('country-forecasts/', views.country_forecasts_page, name='country_forecasts'),
    path('explore/', views.index, name='explore_dashboard'),  # Moved Explore Dashboard to /explore/
    path('objective1/', views.objective1_dashboard, name='objective1_dashboard'),
    path('objective2/', views.objective2_dashboard, name='objective2_dashboard'),
    path('dashboard/', views.index, name='explore_dashboard_redirect'),  # Keep old URL working
    
    # Original dashboard APIs
    path('api/search/', views.search_country, name='search_country'),
    path('api/predict/', views.predict_future, name='predict_future'),
    path('api/countries/', views.get_all_countries, name='get_all_countries'),
    path('api/map-data/', views.get_map_data, name='get_map_data'),
    
    # Objective 1 APIs
    path('api/objective1/model-comparison/', views.objective1_model_comparison, name='objective1_model_comparison'),
    path('api/objective1/historical/', views.objective1_historical_data, name='objective1_historical_data'),
    path('api/objective1/predictions/', views.objective1_future_predictions, name='objective1_future_predictions'),
    path('api/objective1/countries/', views.objective1_countries, name='objective1_countries'),
    
    # Objective 2 APIs
    path('api/objective2/model-comparison/', views.objective2_model_comparison, name='objective2_model_comparison'),
    path('api/objective2/historical/', views.objective2_historical_data, name='objective2_historical_data'),
    path('api/objective2/predictions/', views.objective2_future_predictions, name='objective2_future_predictions'),
    path('api/objective2/countries/', views.objective2_countries, name='objective2_countries'),
    

    # Objective 3 APIs (Electricity Access Classification)
    path('objective3/', views.objective3_dashboard, name='objective3_dashboard'),
    path('api/objective3/model-comparison/', views.objective3_model_comparison, name='objective3_model_comparison'),
    path('api/objective3/historical/', views.objective3_historical_data, name='objective3_historical_data'),
    path('api/objective3/predictions/', views.objective3_future_predictions, name='objective3_future_predictions'),
    path('api/objective3/countries/', views.objective3_countries, name='objective3_countries'),
    path('api/objective3/distribution/', views.objective3_distribution, name='objective3_distribution'),
    path('api/objective3/combined/', views.objective3_combined_data, name='objective3_combined_data'),
    path('api/objective3/policy-markers/', views.objective3_policy_markers, name='objective3_policy_markers'),
    
    # Objective 4 APIs (SDG 7 Forecasting with Regression)
    path('objective4/', views.objective4_dashboard, name='objective4_dashboard'),
    path('api/objective4/model-comparison/', views.objective4_model_comparison, name='objective4_model_comparison'),
    path('api/objective4/historical/', views.objective4_historical_data, name='objective4_historical_data'),
    path('api/objective4/predictions/', views.objective4_future_predictions, name='objective4_future_predictions'),
    path('api/objective4/countries/', views.objective4_countries, name='objective4_countries'),
    path('api/objective4/combined/', views.objective4_combined_data, name='objective4_combined_data'),
    path('api/objective4/country-stats/', views.objective4_country_stats, name='objective4_country_stats'),
    path('api/objective4/global-stats/', views.objective4_global_stats, name='objective4_global_stats'),
    
    # Objective 5 APIs (renamed from objective6)
    path('objective5/', views.objective5_dashboard, name='objective5_dashboard'),
    path('api/objective5/model-comparison/', views.objective5_model_comparison, name='objective5_model_comparison'),
    path('api/objective5/historical/', views.objective5_historical_data, name='objective5_historical_data'),
    path('api/objective5/predictions/', views.objective5_future_predictions, name='objective5_future_predictions'),
    path('api/objective5/countries/', views.objective5_countries, name='objective5_countries'),
    path('api/objective5/combined/', views.objective5_combined_data, name='objective5_combined_data'),
    
    # Objective 6 APIs (renamed from objective7)
    path('objective6/', views.objective6_dashboard, name='objective6_dashboard'),
    path('api/objective6/model-comparison/', views.objective6_model_comparison, name='objective6_model_comparison'),
    path('api/objective6/historical/', views.objective6_historical_data, name='objective6_historical_data'),
    path('api/objective6/predictions/', views.objective6_future_predictions, name='objective6_future_predictions'),
    path('api/objective6/countries/', views.objective6_countries, name='objective6_countries'),
    path('api/objective6/combined/', views.objective6_combined_data, name='objective6_combined_data'),
    
    # Objective 7 APIs (renamed from objective8)
    path('objective7/', views.objective7_dashboard, name='objective7_dashboard'),
    path('api/objective7/model-comparison/', views.objective7_model_comparison, name='objective7_model_comparison'),
    path('api/objective7/historical/', views.objective7_historical_data, name='objective7_historical_data'),
    path('api/objective7/predictions/', views.objective7_future_predictions, name='objective7_future_predictions'),
    path('api/objective7/countries/', views.objective7_countries, name='objective7_countries'),
    path('api/objective7/combined/', views.objective7_combined_data, name='objective7_combined_data'),
    
    # Objective 8: Sustainable Investment Strategy Support
    path('objective8/', views.objective8_dashboard, name='objective8_dashboard'),
    path('api/objective8/model-comparison/', views.objective8_model_comparison, name='objective8_model_comparison'),
    path('api/objective8/historical/', views.objective8_historical_data, name='objective8_historical_data'),
    path('api/objective8/predictions/', views.objective8_future_predictions, name='objective8_future_predictions'),
    path('api/objective8/countries/', views.objective8_countries, name='objective8_countries'),
    path('api/objective8/combined/', views.objective8_combined_data, name='objective8_combined_data'),
    
    # Email Alert System (Admin Panel)
    path('api/send-email-alerts/', views.send_email_alerts, name='send_email_alerts'),
    
    # Admin Panel: Email Alert System with Country Selection (Admin Only)
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('email-admin/', views.email_admin_system, name='email_admin_system'),
    path('api/send-email-alerts-selected/', views.send_email_alerts_selected, name='send_email_alerts_selected'),
    
    # Email Logs Admin Page
    path('email-logs/', views.email_logs_dashboard, name='email_logs_dashboard'),
    path('api/email-logs/', views.get_email_logs, name='get_email_logs'),
    
    # Send Email to Single Country
    path('send-email-country/', views.send_email_single_country, name='send_email_single_country'),
    
    # Send Custom Alert to Country
    path('send-custom-alert/', views.send_custom_alert_page, name='send_custom_alert_page'),
    path('api/send-custom-alert/', views.send_custom_alert_api, name='send_custom_alert_api'),
    
    # Send Alerts to Multiple Countries
    path('send-alerts-multi/', views.send_alerts_multi_page, name='send_alerts_multi_page'),
    
    # XGBoost Automatic Alert System
    path('api/send-xgboost-alerts/', views.send_xgboost_alerts, name='send_xgboost_alerts'),
    
    # Comprehensive ML Comparison (All 8 Objectives)
    path('comprehensive-comparison/', views.comprehensive_comparison_dashboard, name='comprehensive_comparison_dashboard'),
    path('api/comprehensive-comparison/', views.comprehensive_comparison_api, name='comprehensive_comparison_api'),
    
    # Full Analysis (Dashboard + ML Comparison Combined)
    path('full-analysis/', views.full_analysis_dashboard, name='full_analysis_dashboard'),
]
