dream_destination = {}

print("Let's plan your dream destinations!")
print("Enter 'done' when you're finished.")

while True:
    country = input("Which country would you like to visit? ")
    
    if country.lower() == 'done':
        break
    
    note = input(f"Why do you want to visit {country}? ")
    
    dream_destination[country] = note if note else "No specific plans"

    print('Got it! Let\'s keep going or type "done" to finish.')

print("\nYour Dream Travel Itinerary:")
for country, note in dream_destination.items():
    print(f"- {country}: {note}")

print("\nHappy travels! Keep dreaming and exploring the world!")