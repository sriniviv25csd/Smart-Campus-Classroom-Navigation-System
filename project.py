# Combined Data Structure & Map Logic
class CampusNavigationSystem:
    # Data structure containing all campus room records
    ROOMS_DATA = [
        # Ground Floor - CC Block
        {"room_number": "008", "building": "CC Block", "floor": "Ground Floor", "room_type": "Lab", "x": 50, "y": 40, "w": 120, "h": 160, "doorX": 110, "doorY": 210},
        {"room_number": "001", "building": "CC Block", "floor": "Ground Floor", "room_type": "Lab", "x": 180, "y": 40, "w": 120, "h": 160, "doorX": 240, "doorY": 210},
        {"room_number": "015", "building": "CC Block", "floor": "Ground Floor", "room_type": "Lab", "x": 310, "y": 40, "w": 120, "h": 160, "doorX": 370, "doorY": 210},
        {"room_number": "012", "building": "CC Block", "floor": "Ground Floor", "room_type": "Lab", "x": 490, "y": 40, "w": 120, "h": 160, "doorX": 550, "doorY": 210},
        {"room_number": "013", "building": "CC Block", "floor": "Ground Floor", "room_type": "Lab", "x": 620, "y": 40, "w": 120, "h": 160, "doorX": 680, "doorY": 210},
        {"room_number": "096", "building": "CC Block", "floor": "Ground Floor", "room_type": "Classroom", "x": 750, "y": 40, "w": 120, "h": 160, "doorX": 810, "doorY": 210},

        # Floor 1 - A Block
        {"room_number": "101", "building": "A Block", "floor": "1", "room_type": "Scholar", "x": 50, "y": 40, "w": 120, "h": 160, "doorX": 110, "doorY": 210},
        {"room_number": "102", "building": "A Block", "floor": "1", "room_type": "Drawing", "x": 180, "y": 40, "w": 120, "h": 160, "doorX": 240, "doorY": 210},
        {"room_number": "103", "building": "A Block", "floor": "1", "room_type": "Classroom", "x": 310, "y": 40, "w": 120, "h": 160, "doorX": 370, "doorY": 210},
        {"room_number": "106", "building": "A Block", "floor": "1", "room_type": "Classroom", "x": 490, "y": 40, "w": 120, "h": 160, "doorX": 550, "doorY": 210},
        {"room_number": "184", "building": "A Block", "floor": "1", "room_type": "Classroom", "x": 620, "y": 40, "w": 120, "h": 160, "doorX": 680, "doorY": 210},
        {"room_number": "127A", "building": "A Block", "floor": "1", "room_type": "Classroom", "x": 750, "y": 40, "w": 120, "h": 160, "doorX": 810, "doorY": 210},

        # Floor 2 - B Block
        {"room_number": "219", "building": "B Block", "floor": "2", "room_type": "Classroom", "x": 50, "y": 40, "w": 120, "h": 160, "doorX": 110, "doorY": 210},
        {"room_number": "219A", "building": "B Block", "floor": "2", "room_type": "Classroom", "x": 180, "y": 40, "w": 120, "h": 160, "doorX": 240, "doorY": 210},
        {"room_number": "215", "building": "B Block", "floor": "2", "room_type": "Lab", "x": 310, "y": 40, "w": 120, "h": 160, "doorX": 370, "doorY": 210},
        {"room_number": "217", "building": "B Block", "floor": "2", "room_type": "Lab", "x": 490, "y": 40, "w": 120, "h": 160, "doorX": 550, "doorY": 210},
        {"room_number": "216", "building": "B Block", "floor": "2", "room_type": "Lab", "x": 620, "y": 40, "w": 120, "h": 160, "doorX": 680, "doorY": 210},
        {"room_number": "213", "building": "B Block", "floor": "2", "room_type": "Faculty", "x": 750, "y": 40, "w": 120, "h": 160, "doorX": 810, "doorY": 210},
        {"room_number": "201", "building": "B Block", "floor": "2", "room_type": "Classroom", "x": 50, "y": 260, "w": 110, "h": 140, "doorX": 105, "doorY": 250},
        {"room_number": "202", "building": "B Block", "floor": "2", "room_type": "Classroom", "x": 170, "y": 260, "w": 110, "h": 140, "doorX": 225, "doorY": 250},
        {"room_number": "204", "building": "B Block", "floor": "2", "room_type": "Classroom", "x": 290, "y": 260, "w": 110, "h": 140, "doorX": 345, "doorY": 250},
        {"room_number": "206", "building": "B Block", "floor": "2", "room_type": "Classroom", "x": 520, "y": 260, "w": 110, "h": 140, "doorX": 575, "doorY": 250},
        {"room_number": "206A", "building": "B Block", "floor": "2", "room_type": "Classroom", "x": 640, "y": 260, "w": 110, "h": 140, "doorX": 695, "doorY": 250},
        {"room_number": "205", "building": "B Block", "floor": "2", "room_type": "Office", "x": 760, "y": 260, "w": 55, "h": 140, "doorX": 785, "doorY": 250},
        {"room_number": "207", "building": "B Block", "floor": "2", "room_type": "Lab", "x": 820, "y": 260, "w": 50, "h": 140, "doorX": 845, "doorY": 250},

        # Floor 3 - C Block
        {"room_number": "301", "building": "C Block", "floor": "3", "room_type": "Classroom", "x": 370, "y": 40, "w": 180, "h": 160, "doorX": 460, "doorY": 210}
    ]

    def __init__(self):
        self.rooms = self.ROOMS_DATA

    def search(self, query):
        """Search by room number, building, or room type."""
        query = str(query).strip().lower()
        return [
            r for r in self.rooms 
            if query in r["room_number"].lower() or query in r["room_type"].lower() or query in r["building"].lower()
        ]

    def get_route(self, room_number):
        """Get navigation instructions and SVG path line for a room."""
        room = next((r for r in self.rooms if r["room_number"].lower() == str(room_number).lower()), None)
        if not room:
            return f"Room {room_number} not found."

        path_d = f"M 460 410 L 460 230 L {room['doorX']} 230 L {room['doorX']} {room['doorY']}"
        return {
            "room_number": room["room_number"],
            "building": room["building"],
            "floor": room["floor"],
            "room_type": room["room_type"],
            "svg_path": path_d,
            "directions": f"Walk along the main hallway. Target Room {room['room_number']} ({room['room_type']}) is located on {room['floor']} in {room['building']}."
        }


# Quick Execution Test
if __name__ == "__main__":
    nav = CampusNavigationSystem()
    
    # Example search
    print("Search Results for 'Lab':", nav.search("Lab"))
    
    # Example route lookup
    print("\nNavigation Route for Room 219:")
    print(nav.get_route("219"))