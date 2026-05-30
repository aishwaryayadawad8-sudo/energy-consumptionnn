"""
List All Available Countries with Email Addresses
"""
import pandas as pd

def list_countries():
    """Display all countries with their email addresses"""
    print("\n" + "=" * 70)
    print("Available Countries for Email Alerts")
    print("=" * 70)
    print()
    
    try:
        # Load country emails
        df = pd.read_csv('country_emails.csv')
        
        print(f"Total Countries: {len(df)}")
        print()
        print(f"{'Country':<35} {'Email':<35}")
        print("-" * 70)
        
        for _, row in df.iterrows():
            print(f"{row['Country']:<35} {row['Email']:<35}")
        
        print()
        print("=" * 70)
        print("\nTo send alerts, run:")
        print("  python send_email_by_country.py")
        print()
        print("Example usage:")
        print("  Enter countries: India, Nigeria, Brazil")
        print()
        
    except FileNotFoundError:
        print("❌ Error: country_emails.csv not found")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    list_countries()
