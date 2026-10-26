# Ask the user for the season and plant type.
# strip() and lower() let "Summer " match "summer".
season = input("Enter the season (summer or winter): ").strip().lower()
plant_type = (
    input("Enter the plant type (flower or vegetable): ").strip().lower()
)

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:

# - Add detailed comments explaining each block of code.

# - Refactor the code into functions for better readability and
#   modularity.

# - Store advice in a dictionary for multiple plants and seasons and
#   recommend plants based on the entered season.
