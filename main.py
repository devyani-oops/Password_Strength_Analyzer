from password_checker import check_password_strength, display_detailed_analysis
from wordlist_generator import generate_custom_wordlist, save_wordlist_to_file, preview_wordlist

def clear_screen():
    """Clear console screen"""
    print("\n" * 3)

def analyze_password():
    """Handle password analysis"""
    print("\n" + "="*40)
    print("PASSWORD STRENGTH CHECKER")
    print("="*40)
    
    password = input("Enter password to analyze: ")
    
    if not password:
        print("No password entered!")
        return
    
    print("\nAnalyzing password...")
    result = check_password_strength(password)
    display_detailed_analysis(result)
    
    # Option to save results
    save = input("\nSave results to file? (y/n): ").lower()
    if save == 'y':
        filename = input("Enter filename (e.g., result.txt): ")
        try:
            with open(filename, 'w') as f:
                f.write("Password Analysis Report\n")
                f.write("=" * 50 + "\n")
                f.write(f"Password: {result['password']}\n")
                f.write(f"Strength: {result['strength']} ({result['score']}/4)\n")
                f.write(f"Length: {result['length']} characters\n")
                f.write(f"Crack Time: {result['crack_time']}\n")
                f.write(f"Entropy: {result['entropy']} bits\n")
                f.write("\nCharacter Types:\n")
                f.write(f"  Lowercase: {result['has_lower']}\n")
                f.write(f"  Uppercase: {result['has_upper']}\n")
                f.write(f"  Numbers: {result['has_digit']}\n")
                f.write(f"  Special: {result['has_special']}\n")
                
                if result['feedback']:
                    f.write("\nSuggestions:\n")
                    for suggestion in result['feedback']:
                        f.write(f"  - {suggestion}\n")
            
            print(f"✓ Results saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

def generate_wordlist():
    """Handle wordlist generation"""
    print("\n" + "="*40)
    print("CUSTOM WORDLIST GENERATOR")
    print("="*40)
    
    print("Enter personal information to generate wordlist:")
    
    # Get base words
    names_input = input("Names (comma separated): ")
    names = [name.strip() for name in names_input.split(',') if name.strip()]
    
    pets_input = input("Pets name (comma separated): ")
    pets = [pet.strip() for pet in pets_input.split(',') if pet.strip()]
    
    other_input = input("Other keywords (hobbies, brands, etc.): ")
    other = [word.strip() for word in other_input.split(',') if word.strip()]
    
    # Combine all base words
    base_words = names + pets + other
    
    if not base_words:
        print("No base words provided!")
        return
    
    # Get custom years
    years_input = input("Years to include (comma separated, enter for default): ")
    custom_years = [year.strip() for year in years_input.split(',')] if years_input.strip() else None
    
    # Get birthdate for additional variations
    birthdate = input("Birthdate (DDMMYYYY or MMDDYYYY - optional): ").strip()
    if birthdate:
        base_words.append(birthdate)
        # Add parts of birthdate
        if len(birthdate) == 8:
            base_words.append(birthdate[:4])  # Year
            base_words.append(birthdate[4:])  # DayMonth
            base_words.append(birthdate[2:6]) # Middle part
    
    print(f"\nUsing {len(base_words)} base words...")
    print("Generating wordlist...")
    
    # Generate wordlist
    wordlist = generate_custom_wordlist(base_words, custom_years)
    
    # Show preview
    preview_wordlist(wordlist)
    
    # Save to file
    filename = input("\nEnter filename to save (e.g., my_wordlist.txt): ").strip()
    if filename:
        success, result = save_wordlist_to_file(wordlist, filename)
        if success:
            print(f"✓ Wordlist saved to {filename} with {result} words")
        else:
            print(f"✗ Error saving file: {result}")
    else:
        print("No filename provided - wordlist not saved")

def show_banner():
    """Display application banner"""
    banner = """
    ╔══════════════════════════════════════════════╗
    ║          PASSWORD SECURITY TOOL              ║
    ║          (No External Libraries)             ║
    ║                                              ║
    ║  1. Check Password Strength                  ║
    ║  2. Generate Custom Wordlist                 ║
    ║  3. Exit                                     ║
    ╚══════════════════════════════════════════════╝
    """
    print(banner)

def main():
    """Main application loop"""
    while True:
        clear_screen()
        show_banner()
        
        choice = input("Choose option (1-3): ").strip()
        
        if choice == "1":
            analyze_password()
        elif choice == "2":
            generate_wordlist()
        elif choice == "3":
            print("\nThank you for using Password Security Tool!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

# This is the correct way to call the main function
if __name__ == "__main__":
    main()
