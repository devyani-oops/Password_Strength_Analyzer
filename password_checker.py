import re
import math

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Character variety checks
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', password))
    
    # Score based on character types
    char_types = sum([has_lower, has_upper, has_digit, has_special])
    if char_types >= 4:
        score += 2
    elif char_types >= 3:
        score += 1
    else:
        feedback.append("Use mix of uppercase, lowercase, numbers, and special characters")
    
    # Common patterns to avoid
    common_patterns = [
        '123', 'abc', 'password', 'qwerty', 'admin', 'welcome'
    ]
    
    password_lower = password.lower()
    for pattern in common_patterns:
        if pattern in password_lower:
            score -= 1
            feedback.append(f"Avoid common pattern: '{pattern}'")
            break
    
    # Entropy calculation
    entropy = calculate_entropy(password)
    
    # Final score adjustment
    if entropy > 60:
        score += 1
    elif entropy < 30:
        score = max(0, score - 1)
        feedback.append("Password is too predictable")
    
    # Ensure score is between 0-4
    score = max(0, min(4, score))
    
    # Strength labels
    strength_levels = {
        0: "Very Weak",
        1: "Weak", 
        2: "Fair",
        3: "Good",
        4: "Strong"
    }
    
    # Crack time estimation
    crack_times = {
        0: "Instantly",
        1: "Seconds to minutes", 
        2: "Hours to days",
        3: "Weeks to months",
        4: "Years to centuries"
    }
    
    return {
        'password': password,
        'score': score,
        'strength': strength_levels[score],
        'feedback': feedback,
        'crack_time': crack_times[score],
        'entropy': entropy,
        'length': len(password),
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_special': has_special
    }

def calculate_entropy(password):
    char_sets = {
        'lower': bool(re.search(r'[a-z]', password)),
        'upper': bool(re.search(r'[A-Z]', password)),
        'digits': bool(re.search(r'[0-9]', password)),
        'special': bool(re.search(r'[^a-zA-Z0-9]', password))
    }
    
    pool_size = 0
    if char_sets['lower']: pool_size += 26
    if char_sets['upper']: pool_size += 26  
    if char_sets['digits']: pool_size += 10
    if char_sets['special']: pool_size += 32
    
    if pool_size == 0:
        pool_size = 26
    
    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return round(entropy, 2)

def display_detailed_analysis(analysis):
    print("\n" + "="*50)
    print("PASSWORD STRENGTH ANALYSIS")
    print("="*50)
    print(f"Password: {analysis['password']}")
    print(f"Length: {analysis['length']} characters")
    print(f"Strength Score: {analysis['score']}/4 ({analysis['strength']})")
    print(f"Estimated Crack Time: {analysis['crack_time']}")
    print(f"Password Entropy: {analysis['entropy']} bits")
    
    print("\nCharacter Types Used:")
    print(f"  ✓ Lowercase letters: {analysis['has_lower']}")
    print(f"  ✓ Uppercase letters: {analysis['has_upper']}") 
    print(f"  ✓ Numbers: {analysis['has_digit']}")
    print(f"  ✓ Special characters: {analysis['has_special']}")
    
    if analysis['feedback']:
        print("\nSuggestions for Improvement:")
        for suggestion in analysis['feedback']:
            print(f"  • {suggestion}")
    else:
        print("\n✓ Good job! Your password meets basic security requirements.")
    
    print("="*50)
