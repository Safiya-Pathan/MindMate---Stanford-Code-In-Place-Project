import random
import time

# Global storage for journal entries
JOURNAL_ENTRIES = []

def print_header(title):
    print("\n" + "=" * 50)
    print(f"       MINDMATE WELLNESS COMPANION - {title}")
    print("=" * 50)

def mood_validation():
    print_header("MOOD VALIDATION")
    print("How is your heart feeling right now?")
    print("1. Positive & High Energy")
    print("2. Calm & Peaceful")
    print("3. Feeling Low / Blue")
    print("4. Stressed & Overwhelmed")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    print("\n--- Guidance ---")
    if choice == "1":
        print("💡 It's wonderful to see you shining! Keep spreading that positive energy.")
    elif choice == "2":
        print("💡 Embrace this tranquility. Peace is your natural state of mind.")
    elif choice == "3":
        print("💡 It's okay to feel low. Be gentle with yourself today; brighter days are ahead.")
    elif choice == "4":
        print("💡 You don't have to carry the whole world today. Take a deep breath. One thing at a time.")
    else:
        print("💡 Take a deep breath and remember you're doing your best.")

def water_tracker():
    print_header("WATER INTAKE TRACKER")
    glasses = 0
    while True:
        print(f"\nCurrent Water Intake: {glasses} / 8 glasses")
        action = input("Type 'drink' to log a sip, or 'exit' to go back: ").strip().lower()
        if action == 'drink':
            glasses += 1
            print(f"-> Great job! Total sips: {glasses}")
        elif action == 'exit':
            break
        else:
            print("Please type 'drink' or 'exit'.")

def breathing_session():
    print_header("BREATHING & RELAXATION")
    print("Starting your guided 5-second breathing cycle...")
    
    print("\n🌿 Breathe IN slowly... (Expanding)")
    time.sleep(2)
    print("🌿 Hold your breath gently...")
    time.sleep(1.5)
    print("🌿 Breathe OUT and release tension...")
    time.sleep(2)
    print("\n✨ Wonderful! Notice how your body feels lighter.")

def venting_journal():
    print_header("SECURE VENTING JOURNAL")
    while True:
        print("\n1. View Saved Entries")
        print("2. Add New Entry")
        print("3. Back to Main Menu")
        
        choice = input("\nChoose an option (1-3): ").strip()
        
        if choice == "1":
            print("\n--- Your Journal Vault ---")
            if not JOURNAL_ENTRIES:
                print("No entries saved yet.")
            else:
                for idx, entry in enumerate(JOURNAL_ENTRIES, 1):
                    print(f"[{idx}] {entry}")
        elif choice == "2":
            entry = input("Type your thoughts securely: ").strip()
            if entry:
                JOURNAL_ENTRIES.append(entry)
                print("-> Success! Entry saved to local state.")
            else:
                print("-> Entry cannot be empty.")
        elif choice == "3":
            break

def daily_motivation():
    print_header("DAILY BOOST")
    quotes = [
        "“You are stronger than you think.”",
        "“Just let go and trust the process.”",
        "“You don't have to control everything.”",
        "“Every single small step forward is progress.”"
    ]
    print(f"\n✨ {random.choice(quotes)}")

def main():
    while True:
        print_header("DASHBOARD")
        print("Select a feature to demonstrate:")
        print("1. Mood Validation Logic")
        print("2. Water Intake Tracker")
        print("3. Breathing Cycle Simulation")
        print("4. Secure Journal Vault")
        print("5. Daily Motivation")
        print("6. Exit")
        
        choice = input("\nEnter your option (1-6): ").strip()
        
        if choice == "1":
            mood_validation()
        elif choice == "2":
            water_tracker()
        elif choice == "3":
            breathing_session()
        elif choice == "4":
            venting_journal()
        elif choice == "5":
            daily_motivation()
        elif choice == "6":
            print("\nThank you for exploring MindMate logic!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == '__main__':
    main()
