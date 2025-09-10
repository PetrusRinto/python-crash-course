# Patrick 10.09.2025
# My own list of vehicles (I'm a car guy)

brand = ['Nissan','Toyota','Mitsubishi','Alfa Romeo','Ferrari','Porsche']
kind = ['R-34','MR2 2GR Edition','Evo V','Quadrifoglio V6','296 GTB']

# Hard coded since I need more loop experience
vehicle_0 = (f"{brand[0]} {kind[0]}")
vehicle_1 = (f"{brand[1]} {kind[1]}")
vehicle_2 = (f"{brand[2]} {kind[2]}")
vehicle_3 = (f"{brand[3]} {kind[3]}")
vehicle_4 = (f"{brand[4]} {kind[4]}") # In retrospect this can help me loop it in a way I actually know

# Making a list of vehicles with brand and kind compined
vehicles = [vehicle_0,vehicle_1,vehicle_2,vehicle_3,vehicle_4]

# Looping time
for vehicle in vehicles:
    print(f"I want to own a {vehicle} some day.") # Success