"""
Number to Words Converter
Converts any integer into its English word representation.
Supports numbers from -nonillion to +nonillion.
"""

def number_to_words(n: int) -> str:
    """
    Convert an integer to its English word representation.
    
    Args:
        n (int): The number to convert (positive or negative)
    
    Returns:
        str: The number in words (e.g., "one hundred twenty-three")
    
    Examples:
        >>> number_to_words(123)
        'one hundred and twenty-three'
        >>> number_to_words(-4567)
        'minus four thousand, five hundred and sixty-seven'
    """
    # Handle zero as a special case
    if n == 0:
        return "zero"
    
    # Handle negative numbers
    negative = n < 0
    n = abs(n)  # Work with positive numbers internally
    
    # Word lists for different number components
    units = ["", "one", "two", "three", "four", "five", "six", "seven", 
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", 
             "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", 
             "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", 
            "seventy", "eighty", "ninety"]
    
    scales = ["", "thousand", "million", "billion", "trillion", 
              "quadrillion", "quintillion", "sextillion", "septillion", 
              "octillion", "nonillion"]
    
    def three_digit_words(num: int) -> str:
        """
        Convert a 3-digit number (0-999) to words.
        
        Args:
            num (int): A number between 0 and 999
        
        Returns:
            str: The 3-digit number in words
        """
        words = []
        
        # Process hundreds place
        hundreds_digit = num // 100
        remainder = num % 100
        
        if hundreds_digit > 0:
            words.append(units[hundreds_digit])
            words.append("hundred")
            if remainder > 0:
                words.append("and")  # British English format
        
        # Process tens and units (1-99)
        if remainder > 0:
            if remainder < 20:
                # Direct mapping from units list
                words.append(units[remainder])
            else:
                # Split into tens and units
                tens_digit = remainder // 10
                units_digit = remainder % 10
                
                if tens_digit > 0:
                    words.append(tens[tens_digit])
                
                if units_digit > 0:
                    # Handle hyphenated numbers (twenty-one, thirty-four, etc.)
                    if tens_digit > 0:
                        words[-1] = f"{words[-1]}-{units[units_digit]}"
                    else:
                        words.append(units[units_digit])
        
        # Join words with spaces, excluding empty strings
        return " ".join(filter(None, words))
    
    # Process the number in chunks of 3 digits (thousands, millions, etc.)
    word_parts = []
    scale_index = 0
    
    while n > 0:
        # Extract the last 3 digits
        chunk = n % 1000
        
        if chunk > 0:
            # Convert the 3-digit chunk to words
            chunk_words = three_digit_words(chunk)
            
            # Add scale name (thousand, million, etc.) if needed
            scale_name = scales[scale_index]
            if scale_name:
                word_parts.append(f"{chunk_words} {scale_name}")
            else:
                word_parts.append(chunk_words)
        
        # Remove the processed 3 digits and move to next scale
        n //= 1000
        scale_index += 1
    
    # Combine all parts in reverse order (largest scale first)
    result = ", ".join(reversed(word_parts))
    
    # Add "minus" prefix for negative numbers
    if negative:
        result = f"minus {result}"
    
    return result


def main():
    """
    Main program loop with user interface.
    """
    print("=" * 40)
    print("      NUMBER TO WORDS CONVERTER")
    print("=" * 40)
    print("Enter numbers to convert them to English words.")
    print("Enter 'q' to quit the program.\n")
    
    while True:
        try:
            # Get user input
            user_input = input("Enter a number (or 'q' to quit): ").strip()
            
            # Check for quit command
            if user_input.lower() in ('q', 'quit', 'exit'):
                print("\nThank you for using Number to Words Converter!")
                break
            
            # Validate and convert input
            if not user_input:
                print("❌ Please enter a number.")
                continue
            
            # Handle negative numbers
            is_negative = user_input.startswith('-')
            numeric_part = user_input[1:] if is_negative else user_input
            
            if not numeric_part.isdigit():
                print("❌ Invalid input. Please enter a valid integer.")
                continue
            
            # Convert to integer and process
            number = int(user_input)
            words = number_to_words(number)
            
            # Display result with formatting
            print(f"\n{'─' * 50}")
            print(f"🔢 Number: {number:,}")
            print(f"📝 In words: {words}")
            print(f"{'─' * 50}\n")
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except OverflowError:
            print("❌ Number is too large to process.")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")


# Standard Python idiom to run the main function
if __name__ == "__main__":
    main()
