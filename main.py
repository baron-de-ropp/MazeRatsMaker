import MazeRats
import QueryGpt
import json
import datetime



def get_new_genre():
    return input("Please enter a genre for a new version of maze rats: ")



def generate_new_items(property_name, items_list, genre):
    prompt = f"""Here is an example of what a list of standard issue fantasy genre items looks like for the theme '{property_name}': {items_list}. Now, please give me a json list of 100 items for the genre '{genre}' that reflect the theme '{property_name}' output the json in the following format:
    
        {{
            "{property_name}": [
            "list item 1",
            "list item 2"
            ]
        }}
    """
    message = [{"role": "user", "content": prompt}]
    new_items = json.loads(QueryGpt.query_chatgpt(message, return_json=True)).get(property_name, [])
    return new_items



def create_document(data, genre):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"RandomTables-{genre}-{timestamp}.txt"
    with open(filename, "w") as file:
        for property_name, items in data.items():
            file.write(f"{property_name}:\n")
            for item in items:
                file.write(f" - {item}\n")
            file.write("\n")
    print(f"Data has been written to {filename}")



def main():
    genre = get_new_genre()
    maze_rats = MazeRats.MazeRats()
    properties = dir(maze_rats)
    data = {}

    for property_name in properties:
        if not property_name.startswith("_"):  # Ignore private and special methods/attributes
            try:
                value = getattr(maze_rats, property_name)
                if isinstance(value, list):
                    print(f"Processing property: {property_name}")
                    new_items = generate_new_items(property_name, value, genre)
                    data[property_name] = new_items
                    print(new_items)
            except AttributeError:
                pass

    create_document(data, genre)

if __name__ == "__main__":
    main()
