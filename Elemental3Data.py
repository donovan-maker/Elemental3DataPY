import json

# Function to find an element by ID or name
def find_element(identifier, data):
    for element in data:
        if element.get("type") == "table" and element.get("name") == "Elements":
            elements_data = element.get("data", [])
            for element in elements_data:
                if element["id"] == identifier or element["name"] == identifier:
                    return {
                        "id": element["id"],
                        "name": element["name"],
                        "birthTime": element["birthTime"],
                        "description": element["mark"]
                    }
    return None

# Main function
if __name__ == "__main__":
    with open("Elements.json", "r") as file:
        data = json.load(file)
    
    while True:
        user_input = input("Enter an ID or element name (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        element_info = find_element(user_input, data)
        if element_info:
            print(f"ID: {element_info['id']}")
            print(f"Name: {element_info['name']}")
            print(f"Birth Time: {element_info['birthTime']}")
            print(f"Description: {element_info['description']}")
        else:
            print("Element not found.")
