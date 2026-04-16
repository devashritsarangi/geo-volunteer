# Approach 2: RANGE SEARCHING METHOD
# This still iterates through all points, but this is more efficient for n points than brute forcing the 
# distances. Forms a bounding box around the point of consideration, and calculates IF points are within 
# this defined bounding box or not. Then we can proceed by notifying those present within the box.
# If they deny, the bounding box will expand to cover more points.

volunteers = [
    {"name": "tanmay", "x": 40, "y": 5},
    {"name": "swastik", "x": 20, "y": 3},
    {"name": "aditya rout", "x": 100, "y": 4}
]
client = {"name": "devashrit", "x": 40, "y": 10}
distances = []
inRectangle = []

print(f"Devashrit is at: {client["x"]}, {client["y"]}")
print("Running through all volunteers with a square of sides 20 from center...")

# Bounding Box
def boundingBox(clientPoint, size):
    global inRectangle
    # left edge < point x < right edge
    # bottom edge < point y < top edge
    rectLeft = clientPoint["x"] - size
    rectRight = clientPoint["x"] + size
    rectTop = clientPoint["y"] + size
    rectBottom = clientPoint["y"] - size
    
    for i in volunteers:
        if (rectLeft <= i["x"] <= rectRight) and (rectBottom <= i["y"] <= rectTop):
            inRectangle.append(i)

    for j in inRectangle:
        clientX = clientPoint["x"]
        clientY = clientPoint["y"]
        X = j["x"]
        Y = j["y"]
        distance = (clientX - X)**2 + (clientY - Y)**2
        distances.append({"name": j["name"], "distance": distance})

boundingBox(client, 20)
distances.sort(key=lambda item: item["distance"])

# 5. Print the 1st, 2nd, and 3rd closest
for i in range(len(distances)):
    print(f"{[i+1]} closest: {distances[i]["name"]} with distance {(distances[i]["distance"])**1/2}")