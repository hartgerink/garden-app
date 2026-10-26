# Gardening advice for each season
season_advice = {
    "spring": "Plant seeds and seedlings once the risk of frost has passed.",
    "summer": "Water your plants regularly and provide some shade.",
    "autumn": "Clear fallen leaves and plant bulbs for next spring.",
    "winter": "Protect your plants from frost with covers.",
}

# Gardening advice for each type of plant
plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Pick leaves often to encourage new growth.",
}

# Ask the user for the season and plant type, listing the choices
# from the dictionary keys. strip() and lower() let "Summer " match
# "summer".
season_choices = ", ".join(season_advice)
plant_choices = ", ".join(plant_advice)
season = input(f"Enter the season ({season_choices}): ").strip().lower()
plant_type = input(f"Enter the plant type ({plant_choices}): ").strip().lower()

# Look up the advice, falling back to a default message when the
# season or plant type is not in its dictionary
advice = season_advice.get(season, "No advice for this season.")
advice += "\n"
advice += plant_advice.get(plant_type, "No advice for this type of plant.")

# Print the generated advice
print(advice)
