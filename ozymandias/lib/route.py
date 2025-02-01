import requests

def add_and_test_routes(base_url, routes_file):
    """
    Add routes from a file to a base URL and print the ones that work.

    :param base_url: The base URL of the site (e.g., https://example.com).
    :param routes_file: Path to the file containing routes.
    """
    # Ensure base_url does not end with a '/'
    if base_url.endswith('/'):
        base_url = base_url.rstrip('/')

    # Read routes from the file
    try:
        with open(routes_file, 'r') as file:
            routes = file.read().splitlines()  # Read all lines into a list
    except FileNotFoundError:
        print(f"Error: Routes file '{routes_file}' not found.")
        return

    print("Testing routes...")
    working_routes = []

    # Test each route
    for route in routes:
        # Ensure route starts with a '/'
        if not route.startswith('/'):
            route = '/' + route

        full_url = base_url + route  # Combine base URL and route
        try:
            # Send a GET request to the route
            response = requests.get(full_url)
            if response.status_code // 100 == 2:  # Check if status code is 2xx (success)
                working_routes.append(route)
                print(f"Working route: {route} -> Status: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error testing route '{route}': {e}")

    # Print all working routes at the end
    if working_routes:
        print("\nThe following routes are working:")
        for route in working_routes:
            print(route)
    else:
        print("\nNo working routes found.")

def main():
    base_url = input("Enter the base URL of the site: ").strip()
    routes_file = input("Enter the path to the routes file: ").strip()

    if not base_url.startswith(('http://', 'https://')):
        base_url = 'https://' + base_url  # Add 'https://' if missing

    add_and_test_routes(base_url, routes_file)

if __name__ == "__main__":
    main()
