"""
Telegram Bot Configuration for SDG 7 Energy Alerts
"""

# Get your bot token from @BotFather on Telegram
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'  # Replace with your actual token

# Country chat IDs - Users get these by messaging your bot with /start
# Format: 'Country Name': 'chat_id'
COUNTRY_CHAT_IDS = {
    # Example entries - replace with actual chat IDs
    'India': '',
    'Kenya': '',
    'Germany': '',
    'United States': '',
    'Brazil': '',
    'China': '',
    'South Africa': '',
    'Nigeria': '',
    'Indonesia': '',
    'Bangladesh': '',
    # Add more countries as they subscribe
}

# Bot settings
BOT_USERNAME = '@your_bot_username'  # Your bot's username
ENABLE_TELEGRAM_ALERTS = False  # Set to True after configuration
