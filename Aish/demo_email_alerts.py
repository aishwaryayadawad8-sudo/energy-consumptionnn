"""
Demo: Send Email Alerts to Countries
Automatically sends alerts to a few example countries
"""
import subprocess
import sys

# Example countries to test
test_countries = "India, Nigeria, Kenya, Chad"

print("\n" + "=" * 60)
print("DEMO: Email Alert System")
print("=" * 60)
print()
print(f"Sending alerts to: {test_countries}")
print()
print("This will:")
print("1. Analyze electricity access for each country")
print("2. Classify their status (Critical/Needs Improvement/Good/Excellent)")
print("3. Show what email would be sent")
print("4. Simulate sending (no actual emails sent)")
print()
input("Press Enter to continue...")
print()

# Create input for the script
input_data = f"{test_countries}\nyes\n"

# Run the script with input
process = subprocess.Popen(
    [sys.executable, 'send_email_simple.py'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

output, error = process.communicate(input=input_data)

print(output)

if error:
    print("Errors:", error)

print("\n" + "=" * 60)
print("Demo Complete!")
print("=" * 60)
print()
print("To send alerts to your own selection of countries, run:")
print("  python send_email_simple.py")
print()
