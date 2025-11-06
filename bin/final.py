import random

def get_tarot_deck():
    return [
        "The Fool", "The Magician", "The High Priestess", "The Empress",
        "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
        "Strength", "The Hermit", "Wheel of Fortune", "Justice",
        "The Hanged Man", "Death", "Temperance", "The Devil",
        "The Tower", "The Star", "The Moon", "The Sun",
        "Judgement", "The World"
    ]

def draw_cards(num_cards):
    deck = get_tarot_deck()
    if num_cards > len(deck):
        print("Error: Too many cards requested.")
        return []

    # 'random.sample' ensures all drawn cards are unique
    drawn = random.sample(deck, num_cards)
    return drawn

def run_tarot_reading():
    """Main function to run the interactive tarot reading."""
    print("✨ Welcome to the Digital Tarot Reading! ✨")
    
    while True:
        print("\n**How many cards would you like to draw?**")
        print("1. One Card (Focus/Advice)")
        print("3. Three Cards (Past/Present/Future)")
        print("0. Exit")
        
        choice = input("Enter 1, 3, or 0: ").strip()

        if choice == '0':
            print("\nThank you for seeking guidance. Goodbye!")
            break
        elif choice == '1':
            cards = draw_cards(1)
            if cards:
                print("\n--- Your One-Card Reading ---")
                print(f"**Focus/Advice:** {cards[0]}")
                print("----------------------------")
        elif choice == '3':
            cards = draw_cards(3)
            if cards:
                print("\n--- Your Three-Card Spread ---")
                # Assign cards to positions
                print(f"**Past Influence:** {cards[0]}")
                print(f"**Current Situation:** {cards[1]}")
                print(f"**Future Potential:** {cards[2]}")
                print("------------------------------")
        else:
            print("\nInvalid choice. Please enter 1, 3, or 0.")

# Execute the program
if __name__ == "__main__":
    run_tarot_reading()