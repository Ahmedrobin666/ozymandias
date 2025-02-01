import requests

def test_payloads(base_url, payloads_file):
    """
    Test payloads from a file against a base URL and print the ones that work.

    :param base_url: The base URL of the site (e.g., https://example.com).
    :param payloads_file: Path to the file containing payloads.
    """
    # Ensure base_url does not end with a '/'
    if base_url.endswith('/'):
        base_url = base_url.rstrip('/')

    # Read payloads from the file
    try:
        with open(payloads_file, 'r') as file:
            payloads = file.read().splitlines()  # Read all lines into a list
    except FileNotFoundError:
        print(f"Error: Payloads file '{payloads_file}' not found.")
        return

    print("Testing payloads...")
    working_payloads = []

    # Test each payload
    for payload in payloads:
        try:
            # Send a GET request with the payload as a query parameter
            full_url = f"{base_url}?input={payload}"  # Adjust the parameter name as needed
            response = requests.get(full_url)

            # Check if the response is successful (2xx status code)
            if response.status_code // 100 == 2:
                working_payloads.append(payload)
                print(f"Working payload: {payload} -> Status: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Error testing payload '{payload}': {e}")

    # Print all working payloads at the end
    if working_payloads:
        print("\nThe following payloads are working:")
        for payload in working_payloads:
            print(payload)
    else:
        print("\nNo working payloads found.")

def main():
    base_url = input("Enter the base URL of the site: ").strip()
    payloads_file = input("Enter the path to the payloads file: ").strip()

    if not base_url.startswith(('http://', 'https://')):
        base_url = 'https://' + base_url  # Add 'https://' if missing

    test_payloads(base_url, payloads_file)

if __name__ == "__main__":
    main()
