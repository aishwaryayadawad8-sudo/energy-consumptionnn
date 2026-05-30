"""
Email Alert System for SDG 7 Monitoring
Sends automated alerts to countries based on electricity access predictions
"""
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SDG7EmailAlerts:
    """Automated email alerts for electricity access monitoring"""
    
    # Thresholds for triggering alerts
    CRITICAL_THRESHOLD = 50  # Below 50% = Critical
    LOW_THRESHOLD = 75       # 50-75% = Needs improvement
    GOOD_THRESHOLD = 95      # Above 95% = Excellent
    
    # Load country emails from CSV file
    @staticmethod
    def load_country_emails_from_csv():
        """Load country email addresses from country_emails.csv"""
        try:
            import os
            csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'country_emails.csv')
            df = pd.read_csv(csv_path)
            return dict(zip(df['Country'], df['Email']))
        except:
            return {}
    
    # Default email addresses (fallback if CSV not available)
    COUNTRY_EMAILS = {
        'Afghanistan': 'afghanistan.energy@gov.af',
        'Albania': 'albania.energy@gov.al',
        'Algeria': 'algeria.energy@gov.dz',
        'Angola': 'angola.energy@gov.ao',
        'Argentina': 'argentina.energy@gov.ar',
        'Australia': 'australia.energy@gov.au',
        'Austria': 'austria.energy@gov.at',
        'Bangladesh': 'bangladesh.energy@gov.bd',
        'Belgium': 'belgium.energy@gov.be',
        'Benin': 'benin.energy@gov.bj',
        'Bolivia': 'bolivia.energy@gov.bo',
        'Brazil': 'brazil.energy@gov.br',
        'Burkina Faso': 'burkinafaso.energy@gov.bf',
        'Burundi': 'burundi.energy@gov.bi',
        'Cambodia': 'cambodia.energy@gov.kh',
        'Cameroon': 'cameroon.energy@gov.cm',
        'Canada': 'canada.energy@gov.ca',
        'Central African Republic': 'car.energy@gov.cf',
        'Chad': 'chad.energy@gov.td',
        'Chile': 'chile.energy@gov.cl',
        'China': 'china.energy@gov.cn',
        'Colombia': 'colombia.energy@gov.co',
        'Congo': 'congo.energy@gov.cg',
        'Costa Rica': 'costarica.energy@gov.cr',
        'Cuba': 'cuba.energy@gov.cu',
        'Denmark': 'denmark.energy@gov.dk',
        'Dominican Republic': 'dominicanrepublic.energy@gov.do',
        'Ecuador': 'ecuador.energy@gov.ec',
        'Egypt': 'egypt.energy@gov.eg',
        'El Salvador': 'elsalvador.energy@gov.sv',
        'Ethiopia': 'ethiopia.energy@gov.et',
        'Finland': 'finland.energy@gov.fi',
        'France': 'france.energy@gov.fr',
        'Germany': 'germany.energy@gov.de',
        'Ghana': 'ghana.energy@gov.gh',
        'Greece': 'greece.energy@gov.gr',
        'Guatemala': 'guatemala.energy@gov.gt',
        'Guinea': 'guinea.energy@gov.gn',
        'Haiti': 'haiti.energy@gov.ht',
        'Honduras': 'honduras.energy@gov.hn',
        'India': 'india.energy@gov.in',
        'Indonesia': 'indonesia.energy@gov.id',
        'Iran': 'iran.energy@gov.ir',
        'Iraq': 'iraq.energy@gov.iq',
        'Ireland': 'ireland.energy@gov.ie',
        'Italy': 'italy.energy@gov.it',
        'Japan': 'japan.energy@gov.jp',
        'Jordan': 'jordan.energy@gov.jo',
        'Kenya': 'kenya.energy@gov.ke',
        'Liberia': 'liberia.energy@gov.lr',
        'Libya': 'libya.energy@gov.ly',
        'Madagascar': 'madagascar.energy@gov.mg',
        'Malawi': 'malawi.energy@gov.mw',
        'Mali': 'mali.energy@gov.ml',
        'Mexico': 'mexico.energy@gov.mx',
        'Morocco': 'morocco.energy@gov.ma',
        'Mozambique': 'mozambique.energy@gov.mz',
        'Myanmar': 'myanmar.energy@gov.mm',
        'Nepal': 'nepal.energy@gov.np',
        'Netherlands': 'netherlands.energy@gov.nl',
        'Nicaragua': 'nicaragua.energy@gov.ni',
        'Niger': 'niger.energy@gov.ne',
        'Nigeria': 'nigeria.energy@gov.ng',
        'North Korea': 'northkorea.energy@gov.kp',
        'Norway': 'norway.energy@gov.no',
        'Pakistan': 'pakistan.energy@gov.pk',
        'Panama': 'panama.energy@gov.pa',
        'Papua New Guinea': 'png.energy@gov.pg',
        'Paraguay': 'paraguay.energy@gov.py',
        'Peru': 'peru.energy@gov.pe',
        'Philippines': 'philippines.energy@gov.ph',
        'Poland': 'poland.energy@gov.pl',
        'Portugal': 'portugal.energy@gov.pt',
        'Romania': 'romania.energy@gov.ro',
        'Russia': 'russia.energy@gov.ru',
        'Rwanda': 'rwanda.energy@gov.rw',
        'Saudi Arabia': 'saudiarabia.energy@gov.sa',
        'Senegal': 'senegal.energy@gov.sn',
        'Sierra Leone': 'sierraleone.energy@gov.sl',
        'Somalia': 'somalia.energy@gov.so',
        'South Africa': 'southafrica.energy@gov.za',
        'South Korea': 'southkorea.energy@gov.kr',
        'South Sudan': 'southsudan.energy@gov.ss',
        'Spain': 'spain.energy@gov.es',
        'Sri Lanka': 'srilanka.energy@gov.lk',
        'Sudan': 'sudan.energy@gov.sd',
        'Sweden': 'sweden.energy@gov.se',
        'Switzerland': 'switzerland.energy@gov.ch',
        'Syria': 'syria.energy@gov.sy',
        'Tanzania': 'tanzania.energy@gov.tz',
        'Thailand': 'thailand.energy@gov.th',
        'Togo': 'togo.energy@gov.tg',
        'Tunisia': 'tunisia.energy@gov.tn',
        'Turkey': 'turkey.energy@gov.tr',
        'Uganda': 'uganda.energy@gov.ug',
        'Ukraine': 'ukraine.energy@gov.ua',
        'United Kingdom': 'uk.energy@gov.uk',
        'United States': 'usa.energy@gov.us',
        'Uruguay': 'uruguay.energy@gov.uy',
        'Venezuela': 'venezuela.energy@gov.ve',
        'Vietnam': 'vietnam.energy@gov.vn',
        'Yemen': 'yemen.energy@gov.ye',
        'Zambia': 'zambia.energy@gov.zm',
        'Zimbabwe': 'zimbabwe.energy@gov.zw',
    }
    
    def __init__(self, smtp_server=None, smtp_port=None, sender_email=None, sender_password=None):
        """
        Initialize email alert system
        
        To configure your email:
        1. Update sustainable_energy/email_config.py with your email and App Password
        2. For Gmail: Enable 2FA and create App Password at https://myaccount.google.com/apppasswords
        """
        # Load from config file if not provided
        if sender_email is None or sender_password is None:
            try:
                import sys
                import os
                sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
                from email_config import EMAIL_CONFIG
                smtp_server = smtp_server or EMAIL_CONFIG.get('smtp_server', 'smtp.gmail.com')
                smtp_port = smtp_port or EMAIL_CONFIG.get('smtp_port', 587)
                sender_email = sender_email or EMAIL_CONFIG.get('sender_email', 'electricity.prediction2000@gmail.com')
                sender_password = sender_password or EMAIL_CONFIG.get('sender_password', 'your-app-password')
            except:
                smtp_server = smtp_server or 'smtp.gmail.com'
                smtp_port = smtp_port or 587
                sender_email = sender_email or 'electricity.prediction2000@gmail.com'
                sender_password = sender_password or 'your-app-password'
        
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        
        # Load country emails from CSV (overrides default COUNTRY_EMAILS)
        csv_emails = self.load_country_emails_from_csv()
        if csv_emails:
            self.COUNTRY_EMAILS = csv_emails
    
    def classify_country_status(self, access_percentage):
        """Classify country based on electricity access"""
        if access_percentage < self.CRITICAL_THRESHOLD:
            return 'critical', 'Developed'
        elif access_percentage < self.LOW_THRESHOLD:
            return 'needs_improvement', 'Developing'
        elif access_percentage < self.GOOD_THRESHOLD:
            return 'good', 'Developing'
        else:
            return 'excellent', 'Developed'
    
    def generate_email_content(self, country, access_percentage, status, country_type, year):
        """Generate email content based on country status"""
        
        if status == 'critical':
            subject = f"🚨 URGENT: Critical Electricity Access Alert for {country}"
            body = f"""
Dear Energy Ministry of {country},

CRITICAL ALERT: SDG 7 Monitoring System

Our AI-powered monitoring system has identified that {country} has critically low electricity access:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: CRITICAL - Immediate Action Required
- Year: {year}

⚠️ IMMEDIATE ACTION PLAN:

1. EMERGENCY MEASURES:
   - Deploy mobile solar units to remote areas
   - Establish emergency power distribution centers
   - Partner with international energy organizations

2. SHORT-TERM (0-2 years):
   - Accelerate grid expansion to underserved regions
   - Implement off-grid solar solutions
   - Provide subsidies for household solar systems

3. MEDIUM-TERM (2-5 years):
   - Invest in renewable energy infrastructure
   - Build mini-grid systems for rural communities
   - Train local technicians for maintenance

4. FUNDING OPPORTUNITIES:
   - World Bank Clean Energy Fund
   - UN SDG 7 Initiative Grants
   - Green Climate Fund

📞 Contact our SDG 7 support team for immediate assistance.

Best regards,
SDG 7 Global Monitoring System
"""
        
        elif status == 'needs_improvement':
            subject = f"⚠️ Action Required: Electricity Access Below Target for {country}"
            body = f"""
Dear Energy Ministry of {country},

SDG 7 Progress Alert

Our monitoring system shows {country} needs to accelerate electricity access improvements:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: Below SDG 7 Target
- Year: {year}

💡 RECOMMENDED ACTIONS:

1. Expand grid infrastructure to rural areas
2. Implement renewable energy projects (solar, wind)
3. Provide financing for household connections
4. Partner with private sector for last-mile connectivity

📈 Target: Achieve 95%+ access by 2030

Resources available at: sdg7.org/resources

Best regards,
SDG 7 Global Monitoring System
"""
        
        elif status == 'excellent':
            subject = f"🎉 Congratulations: {country} Achieves Excellent Electricity Access!"
            body = f"""
Dear Energy Ministry of {country},

CONGRATULATIONS! 🎉

We are pleased to inform you that {country} has achieved excellent electricity access:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: EXCELLENT - SDG 7 Target Achieved!
- Year: {year}

🌟 ACHIEVEMENTS:
- Universal electricity access achieved
- SDG 7 target met ahead of schedule
- Model for other countries to follow

🔄 NEXT STEPS:
1. Maintain and improve grid reliability
2. Transition to 100% renewable energy
3. Share best practices with developing nations
4. Focus on clean cooking access (SDG 7.1.2)

Your success story will be featured in our global SDG 7 report!

Best regards,
SDG 7 Global Monitoring System
"""
        
        else:  # good
            subject = f"✅ Good Progress: {country} on Track for SDG 7"
            body = f"""
Dear Energy Ministry of {country},

SDG 7 Progress Update

{country} is making good progress toward universal electricity access:

📊 Current Status:
- Electricity Access: {access_percentage:.1f}%
- Classification: {country_type} Country
- Status: Good Progress
- Year: {year}

👍 Keep up the excellent work! Continue current efforts to reach 100% access.

Best regards,
SDG 7 Global Monitoring System
"""
        
        return subject, body
    
    def send_email(self, to_email, subject, body, country_name=None, log_to_db=True, user=None):
        """Send email alert and log to database"""
        error_message = None
        success = False
        
        try:
            # Check if testing mode is enabled
            try:
                import sys
                import os
                sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
                from email_config import TESTING_MODE, DUMMY_EMAIL, ENABLE_ACTUAL_EMAIL_SENDING
                
                # In testing mode, send to dummy email but keep original in subject
                if TESTING_MODE and DUMMY_EMAIL:
                    actual_recipient = to_email
                    to_email = DUMMY_EMAIL
                    subject = f"[TEST - For: {country_name or actual_recipient}] {subject}"
                    body = f"ORIGINAL RECIPIENT: {actual_recipient}\nCOUNTRY: {country_name}\n\n{'='*60}\n\n{body}"
            except:
                ENABLE_ACTUAL_EMAIL_SENDING = False
            
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect and send (only if enabled)
            if ENABLE_ACTUAL_EMAIL_SENDING:
                server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                server.quit()
                print(f"✅ Email SENT to {to_email}")
            else:
                print(f"✅ Email SIMULATED (not actually sent) to {to_email}")
            
            print(f"   Subject: {subject}")
            # In simulation mode, always return success
            success = True
            
        except Exception as e:
            error_message = str(e)
            print(f"❌ Failed to send email to {to_email}: {error_message}")
            success = False
        
        # Log to database if enabled
        if log_to_db:
            try:
                import django
                django.setup()
                from dashboard.models import EmailLog
                
                # Extract alert info from subject/body
                alert_type = 'good'
                if '🚨 URGENT' in subject or 'CRITICAL' in subject:
                    alert_type = 'critical'
                elif '⚠️ Action Required' in subject or 'Below Target' in subject:
                    alert_type = 'needs_improvement'
                elif '🎉 Congratulations' in subject or 'EXCELLENT' in subject:
                    alert_type = 'excellent'
                
                # Extract access percentage and year (you'll need to pass these)
                access = 0
                year = 2024
                
                EmailLog.objects.create(
                    country=country_name or 'Unknown',
                    recipient_email=to_email,
                    subject=subject,
                    status='success' if success else 'failed',
                    alert_type=alert_type,
                    electricity_access=access,
                    year=year,
                    error_message=error_message,
                    sent_by=user.username if user else 'System'
                )
            except Exception as db_error:
                print(f"⚠️ Failed to log email to database: {str(db_error)}")
        
        return success
    
    def analyze_and_send_alerts(self, predictions_df, log_to_db=True, user=None, custom_subject=None, custom_message=None):
        """
        Analyze predictions and send alerts to countries
        
        Args:
            predictions_df: DataFrame with columns ['country', 'year', 'predicted_access']
            log_to_db: Whether to log emails to database
            user: Django user object for logging
        """
        alerts_sent = []
        
        # Get latest prediction for each country
        latest_predictions = predictions_df.sort_values('year').groupby('country').last().reset_index()
        
        for _, row in latest_predictions.iterrows():
            country = row['country']
            access = row['predicted_access']
            year = row['year']
            
            # Check if we have email for this country
            if country not in self.COUNTRY_EMAILS:
                continue
            
            status, country_type = self.classify_country_status(access)
            
            # Only send alerts for critical, needs_improvement, or excellent
            if status in ['critical', 'needs_improvement', 'excellent']:
                # Use custom content if provided, otherwise generate automatic content
                if custom_subject or custom_message:
                    subject = custom_subject if custom_subject else f"SDG 7 Alert: {country} - {status.replace('_', ' ').title()}"
                    if custom_message:
                        body = custom_message
                    else:
                        _, body = self.generate_email_content(country, access, status, country_type, year)
                else:
                    subject, body = self.generate_email_content(country, access, status, country_type, year)
                email = self.COUNTRY_EMAILS[country]
                
                # Send email first
                success = self.send_email(email, subject, body, country_name=country, log_to_db=False)
                
                # Log to database with access and year info
                if log_to_db:
                    try:
                        from dashboard.models import EmailLog
                        
                        log_entry = EmailLog.objects.create(
                            country=country,
                            recipient_email=email,
                            subject=subject,
                            status='success' if success else 'failed',
                            alert_type=status,
                            electricity_access=float(access),
                            year=int(year),
                            sent_by=user.username if user else 'System',
                            error_message='' if success else 'Email sending failed (simulation mode)' if not success else None
                        )
                        print(f"✅ Logged to database: {country} - {status}")
                        
                    except Exception as db_error:
                        print(f"⚠️ Database logging error for {country}: {str(db_error)}")
                        import traceback
                        traceback.print_exc()
                else:
                    pass
                
                if success:
                    alerts_sent.append({
                        'country': country,
                        'email': email,
                        'status': status,
                        'access': access,
                        'year': year,
                        'subject': subject
                    })
        
        return alerts_sent
    
    def get_alert_summary(self, predictions_df):
        """Get summary of which countries would receive alerts"""
        latest_predictions = predictions_df.sort_values('year').groupby('country').last().reset_index()
        
        summary = {
            'critical': [],
            'needs_improvement': [],
            'good': [],
            'excellent': []
        }
        
        for _, row in latest_predictions.iterrows():
            country = row['country']
            access = row['predicted_access']
            status, country_type = self.classify_country_status(access)
            
            summary[status].append({
                'country': country,
                'access': access,
                'type': country_type,
                'has_email': country in self.COUNTRY_EMAILS
            })
        
        return summary
