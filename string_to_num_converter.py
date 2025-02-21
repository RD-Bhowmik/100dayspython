def word_to_number(number_string):
    """
    Convert a number expressed in words to its integer value.
    Examples: 'one hundred', 'three million', 'twenty-five thousand six hundred'
    """
    # Dictionary mapping words to values
    word_values = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1_000,
        'million': 1_000_000,
        'billion': 1_000_000_000,
        'trillion': 1_000_000_000_000
    }
    
    # Clean and normalize input
    number_string = number_string.lower().replace('-', ' ').replace(' and ', ' ')
    words = number_string.split()
    
    # Process the words
    total = 0
    current_number = 0
    
    for word in words:
        if word in word_values:
            # Check if it's a multiplier (hundred, thousand, etc.)
            if word_values[word] >= 100:
                # If no number before multiplier, assume 1 (e.g., "thousand" = 1000)
                current_number = current_number or 1
                # Multiply current number by the multiplier
                current_number *= word_values[word]
                
                # For large numbers (thousand, million, etc.), add to total and reset
                if word_values[word] >= 1000:
                    total += current_number
                    current_number = 0
            else:
                # Add value to current number
                current_number += word_values[word]
        else:
            # Handle hyphenated numbers (e.g., "twenty-one")
            if '-' in word:
                parts = word.split('-')
                if parts[0] in word_values and parts[1] in word_values:
                    current_number += word_values[parts[0]] + word_values[parts[1]]
    
    # Add any remaining current_number to total
    total += current_number
    
    return total

# Example usage
def main():
    while True:
        user_input = input("\nEnter a number in words (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            result = word_to_number(user_input)
            print(f"The numeric value is: {result:,}")
        except Exception as e:
            print(f"Error: {e}. Please try again with a valid number word.")

if __name__ == "__main__":
    main()