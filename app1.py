# Approach 1: BRUTE FORCE METHOD
# This involves having one user at a certain coordinate wrt origin, and various volunteers at coordinates wrt origin.
# This program scours through every single volunteer in determining the closest possible volunteer to client.
# Very time consuming if we consider in a global scale, but if we limit our bounding area to just a single city it still is very inefficient but gets the job done.

# Good for simplicity, bad for scalability.

volunteers = [
    {"name": "tanmay", "x": 40, "y": 5},
    {"name": "swastik", "x": 20, "y": 3},
    {"name": "aditya rout", "x": 100, "y": 4}
]
client = {"name": "devashrit", "x": 40, "y": 10}
distances = []

print(f"Devashrit is at: {client["x"]}, {client["y"]}")
print("Running through all volunteers...")

def sqr_dist(client, volunteer):
    x = volunteer["x"] - client["x"]
    y = volunteer["y"] - client["y"]
    return (x**2) + (y**2)

for volunteer in volunteers:
    dist = sqr_dist(client, volunteer)
    distances.append({"name": volunteer["name"], "distance": dist})

distances.sort(key=lambda item: item["distance"])

# 5. Print the closest
for i in range(len(distances)):
    print(f"{[i+1]} closest: {distances[i]["name"]} with distance {(distances[i]["distance"])**1/2}")