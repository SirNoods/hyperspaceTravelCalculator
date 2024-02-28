
region_to_region_travel_times = {
    "Deep Core": {
        "Deep Core": 12,
        "Core Worlds": 18,
        "Colonies": 24,
        "Inner Rim": 48,
        "Expansion Region": 72,
        "Mid Rim": 96,
        "Outer Rim": 120,
        "Wild Space": 144,
    },
    "Core Worlds": {
        "Deep Core": 24,
        "Core Worlds": 6,
        "Colonies": 24,
        "Inner Rim": 36,
        "Expansion Region": 60,
        "Mid Rim": 84,
        "Outer Rim": 96,
        "Wild Space": 120,
    },
    "Colonies": {
        "Deep Core": 48,
        "Core Worlds": 24,
        "Colonies": 12,
        "Inner Rim": 24,
        "Expansion Region": 48,
        "Mid Rim": 72,
        "Outer Rim": 96,
        "Wild Space": 120,
    },
    "Inner Rim": {
            "Deep Core": 72,
            "Core Worlds": 36,
            "Colonies": 24,
            "Inner Rim": 18,
            "Expansion Region": 24,
            "Mid Rim": 48,
            "Outer Rim": 72,
            "Wild Space": 96,
    },
    "Expansion Region": {
            "Deep Core": 96,
            "Core Worlds": 60,
            "Colonies": 48,
            "Inner Rim": 24,
            "Expansion Region": 24,
            "Mid Rim": 24,
            "Outer Rim": 48,
            "Wild Space": 72,
    },
    "Mid RIm": {
            "Deep Core": 120,
            "Core Worlds": 84,
            "Colonies": 72,
            "Inner Rim": 48,
            "Expansion Region": 24,
            "Mid Rim": 36,
            "Outer Rim": 24,
            "Wild Space": 48,
    },
    "Outer Rim": {
            "Deep Core": 144,
            "Core Worlds": 96,
            "Colonies": 96,
            "Inner Rim": 72,
            "Expansion Region": 48,
            "Mid Rim": 24,
            "Outer Rim": 48,
            "Wild Space": 24,
    },
    "Wild Space": {
            "Deep Core": 168,
            "Core Worlds": 120,
            "Colonies": 120,
            "Inner Rim": 96,
            "Expansion Region": 72,
            "Mid Rim": 48,
            "Outer Rim": 24,
            "Wild Space": 12,
    }
}


class StarWarsMap:
    def __init__(self):
        # Adjusting the map to hold more detailed information about each planet
        self.map = {}  # key: planet name, value: dict with territory and connections

    def add_planet(self, planet, territory):
        if planet not in self.map:
            self.map[planet] = {"territory": territory, "connections": []}

    def add_hyperspace_lane(self, start, end, lane_type):
        # Ensure both planets exist before adding a connection
        if start in self.map and end in self.map:
            self.map[start]["connections"].append((end, lane_type))
            # Assuming lanes are bidirectional; if not, remove the next line
            self.map[end]["connections"].append((start, lane_type))
        else:
            print(f"One or both planets {start} and {end} do not exist in the map.")

    def get_connections(self, planet):
        # Return the connections for the specified planet
        if planet in self.map:
            return self.map[planet]["connections"]
        else:
            return None

    def get_territory(self, planet):
        # Return the territory of the specified planet
        if planet in self.map:
            return self.map[planet]["territory"]
        else:
            return None

# Usage

galaxy_map = StarWarsMap()
planets = open("colonies.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Colonies")
planets.close()
planets = open("coreworlds.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Core Worlds")
planets.close()
planets = open("deepcore.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Deep Core")
planets.close()
planets = open("expansionregion.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Expansion Region")
planets.close()
planets = open("innerrrim.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Inner Rim")
planets.close()
planets = open("midrim.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Mid Rim")
planets.close()
planets = open("outerrim.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Outer Rim")
planets.close()
planets = open("wildspace.txt", "r")
for planet in planets:
    print(planet)
    galaxy_map.add_planet(planet.strip(), "Wild Space")
planets.close()