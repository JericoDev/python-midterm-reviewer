# Basic fare details
base_fare = 40  # Flat rate for the first kilometer
rate_per_km = 10  # Rate per kilometer after the first one

# User input for distance
distance = float(input("Enter the distance traveled (in kilometers): "))

# Fare calculation
if distance <= 1:
    total_fare = base_fare  # Flat fare for 1 km or less
    extra_km = 0  # No extra kilometers for distances <= 1 km
else:
    extra_km = distance - 1
    total_fare = base_fare + (extra_km * rate_per_km)

# Display the total fare and additional information
print("\n===== Fare Breakdown =====")
print(f"Base fare for the first kilometer: PHP {base_fare:.2f}")
print(f"Rate per additional kilometer: PHP {rate_per_km:.2f}")
print(f"Distance traveled: {distance:.2f} km")
print(f"Extra kilometers charged: {extra_km:.2f} km")
print(f"Total fare: PHP {total_fare:.2f}")
print("==========================")
