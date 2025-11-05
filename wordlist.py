def simple_leet_speak(word):
    leet_map = {
        'a': ['4', '@'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7']
    }
    
    variations = [word]
    
    for original, replacements in leet_map.items():
        for replacement in replacements:
            if original in word.lower():
                new_word = word.lower().replace(original, replacement)
                variations.append(new_word)
                if len(new_word) > 0:
                    variations.append(new_word.capitalize())
    
    return variations

def generate_custom_wordlist(base_words, custom_years=None):
    if custom_years is None:
        custom_years = ['2020', '2021', '2022', '2023', '2024']
    
    common_suffixes = ['', '123', '!', '1', '12', '1234']
    
    wordlist = set()
    
    for base_word in base_words:
        base_word = base_word.strip()
        if not base_word:
            continue
        
        # Basic variations
        wordlist.add(base_word)
        wordlist.add(base_word.lower())
        wordlist.add(base_word.upper())
        wordlist.add(base_word.capitalize())
        
        # Leet speak
        leet_words = simple_leet_speak(base_word)
        wordlist.update(leet_words)
        
        # Add suffixes
        for suffix in common_suffixes:
            wordlist.add(base_word + suffix)
            wordlist.add(base_word.lower() + suffix)
        
        # Add years
        for year in custom_years:
            wordlist.add(base_word + year)
            wordlist.add(base_word.lower() + year)
    
    return sorted(list(wordlist))

def save_wordlist_to_file(wordlist, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for word in wordlist:
                file.write(word + '\n')
        return True, len(wordlist)
    except Exception as e:
        return False, str(e)

def preview_wordlist(wordlist, max_preview=20):
    print(f"\nGenerated {len(wordlist)} total words")
    print("Preview (first 20 words):")
    print("-" * 30)
    
    for i, word in enumerate(wordlist[:max_preview]):
        print(f"  {i+1:2d}. {word}")
    
    if len(wordlist) > max_preview:
        print(f"  ... and {len(wordlist) - max_preview} more words")
