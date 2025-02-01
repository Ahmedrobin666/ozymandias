from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time  # Ensure time module is imported

def find_csrf_token(form):
    """
    Find and extract the CSRF token from the form.
    """
    csrf_token = form.find('input', {'name': 'csrf_token'})
    if csrf_token:
        return csrf_token.get('value')
    return None

def form(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    retries = 3  # Number of retries
    timeout = 10  # Timeout in seconds

    for attempt in range(retries):
        try:
            print(f"Attempt {attempt + 1} of {retries}...")
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()  # Raise an error for bad status codes
            print("Request successful! Parsing the page...")

            soup = BeautifulSoup(response.text, 'lxml')
            forms = soup.find_all('form')  # Find all <form> tags

            if not forms:
                print("No forms found on the page.")
            else:
                print(f"Found {len(forms)} forms:")
                for form in forms:
                    action = form.get('action')  # Get the 'action' attribute
                    method = form.get('method', 'POST').upper()  # Default to POST if method is not specified
                    print(f"\nForm Action: {action}, Method: {method}")

                    # Find all input fields
                    inputs = form.find_all(['input', 'textarea', 'select'])
                    if not inputs:
                        print("  No input fields found in this form.")
                    else:
                        print("  Input fields:")
                        params = {}  # Dictionary to store parameters
                        for input_tag in inputs:
                            input_name = input_tag.get('name')  # Get the 'name' attribute
                            input_type = input_tag.get('type', 'text')  # Get the 'type' attribute (default to text)
                            input_value = input_tag.get('value', '')  # Get the 'value' attribute (default to empty)
                            print(f"    Name: {input_name}, Type: {input_type}, Value: {input_value}")

                            # Add the parameter to the dictionary
                            if input_name:
                                params[input_name] = input_value

                        # Find and add CSRF token if present
                        csrf_token = find_csrf_token(form)
                        if csrf_token:
                            print(f"  CSRF Token found: {csrf_token}")
                            params['csrf_token'] = csrf_token

                        # Allow the user to modify or add parameters
                        modify_params = input("\nDo you want to modify or add parameters? (yes/no): ").strip().lower()
                        if modify_params == 'yes':
                            while True:
                                param_name = input("Enter parameter name (or 'done' to finish): ").strip()
                                if param_name.lower() == 'done':
                                    break
                                param_value = input(f"Enter value for '{param_name}': ").strip()
                                param_inject = input(f"Enter value to inject for '{param_name}' (after \"\"): ").strip()

                                # Updated to send without quotes, so `||` is appended directly to the string
                                params[param_name] = f"{param_value}|{param_inject}"

                        # Construct the full URL for the action
                        submit_url = urljoin(url, action) if action else url
                        print(f"\nSubmitting form to: {submit_url}")
                        print(f"Parameters: {params}")

                        # Send a POST request with the parameters
                        try:
                            if method == 'GET':
                                response = requests.get(submit_url, params=params, headers=headers)
                            else:
                                response = requests.post(submit_url, data=params, headers=headers)

                            print(f"Response Status Code: {response.status_code}")
                            print(f"Response Content:\n{response.text[:500]}...")  # Show first 500 characters
                        except requests.exceptions.RequestException as e:
                            print(f"Error submitting form: {e}")

            break  # Exit the loop if successful

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(5)  # Wait before retrying
            else:
                print("All attempts failed. Please try again later.")

def main():
    url = input("Enter site URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    form(url)

if __name__ == "__main__":
    main()

