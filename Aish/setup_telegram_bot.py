"""
Quick Setup Script for Telegram Bot
Run this to configure your Telegram alert system
"""

print("=" * 70)
print("🤖 Telegram Bot Setup for SDG 7 Energy Alerts")
print("=" * 70)

print("\n📱 Step 1: Create Your Bot")
print("-" * 70)
print("1. Open Telegram and search for: @BotFather")
print("2. Send the command: /newbot")
print("3. Choose a name: SDG7 Energy Alert Bot")
print("4. Choose a username: sdg7_energy_bot (must end with 'bot')")
print("5. Copy the bot token (looks like: 123456789:ABCdef...)")

bot_token = input("\n✏️  Paste your bot token here: ").strip()

if not bot_token or len(bot_token) < 20:
    print("❌ Invalid token. Please run the script again.")
    exit(1)

print("\n✅ Bot token received!")

print("\n📝 Step 2: Get Chat IDs")
print("-" * 70)
print("To get chat IDs:")
print("1. Search for your bot in Telegram")
print("2. Send /start to your bot")
print("3. Visit: https://api.telegram.org/bot" + bot_token + "/getUpdates")
print("4. Look for 'chat':{'id': YOUR_CHAT_ID}")

print("\n💡 For testing, you can use your own chat ID first")
test_chat_id = input("✏️  Enter a test chat ID (or press Enter to skip): ").strip()

# Update telegram_config.py
config_content = f'''"""
Telegram Bot Configuration for SDG 7 Energy Alerts
"""

# Your bot token from @BotFather
TELEGRAM_BOT_TOKEN = '{bot_token}'

# Country chat IDs - Users get these by messaging your bot with /start
# Format: 'Country Name': 'chat_id'
COUNTRY_CHAT_IDS = {{
    # Test entry
    'Test Country': '{test_chat_id}' if test_chat_id else '',
    
    # Add real countries as they subscribe
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
}}

# Bot settings
BOT_USERNAME = '@your_bot_username'  # Update with your bot's username
ENABLE_TELEGRAM_ALERTS = {'True' if test_chat_id else 'False'}  # Set to True when ready
'''

try:
    with open('sustainable_energy/telegram_config.py', 'w', encoding='utf-8') as f:
        f.write(config_content)
    print("\n✅ Configuration saved to: sustainable_energy/telegram_config.py")
except Exception as e:
    print(f"\n❌ Error saving config: {e}")
    exit(1)

print("\n📦 Step 3: Install Required Package")
print("-" * 70)
print("Run: pip install requests")

import subprocess
try:
    subprocess.run(['pip', 'install', 'requests'], check=True, capture_output=True)
    print("✅ Package installed successfully")
except:
    print("⚠️  Please run manually: pip install requests")

print("\n🧪 Step 4: Test Your Bot")
print("-" * 70)
print("Run: python sustainable_energy/ml_models/telegram_alerts.py")

if test_chat_id:
    print("\n✅ Your bot is configured and ready to test!")
    print(f"Bot Token: {bot_token[:10]}...")
    print(f"Test Chat ID: {test_chat_id}")
    print("\nTo test:")
    print("1. Open Telegram and find your bot")
    print("2. Send /start to your bot")
    print("3. Run: python sustainable_energy/ml_models/telegram_alerts.py")
else:
    print("\n⚠️  Bot configured but alerts are disabled")
    print("To enable:")
    print("1. Get your chat ID from the bot")
    print("2. Update COUNTRY_CHAT_IDS in telegram_config.py")
    print("3. Set ENABLE_TELEGRAM_ALERTS = True")

print("\n" + "=" * 70)
print("🎉 Setup Complete!")
print("=" * 70)
print("\n📚 Next Steps:")
print("1. Read: TELEGRAM_ALERT_API_GUIDE.md")
print("2. Test: python sustainable_energy/ml_models/telegram_alerts.py")
print("3. Integrate: Add to your Django views")
print("\n💡 Your bot is ready to send energy alerts! 📱⚡")
