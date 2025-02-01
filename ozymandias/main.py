from lib.test import form
from lib.payloadtest import test_payloads
from lib.route import add_and_test_routes
from lib.upload import upload_file_as_image

def main():
    while True:
        print("\n--- Menu ---")
        print("1: Test Payloads (URL Injection)")
        print("2: Test Routes (Fuzzing)")
        print("3: Find and Test Forms (POST Injection)")
        print("4: Upload File (Image Upload)")
        print("5: Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Test Payloads
            base_url = input("Enter the base URL of the site: ").strip()
            if not base_url.startswith(('http://', 'https://')):
                base_url = 'https://' + base_url
            payloads_file = input("Enter the path to the payloads file: ").strip()
            test_payloads(base_url, payloads_file)

        elif choice == '2':
            # Test Routes
            base_url = input("Enter the base URL of the site: ").strip()
            if not base_url.startswith(('http://', 'https://')):
                base_url = 'https://' + base_url
            routes_file = input("Enter the path to the routes file: ").strip()
            add_and_test_routes(base_url, routes_file)

        elif choice == '3':
            # Find and Test Forms
            base_url = input("Enter the base URL of the site: ").strip()
            if not base_url.startswith(('http://', 'https://')):
                base_url = 'https://' + base_url
            form(base_url)

        elif choice == '4':
            # Upload File (Image Upload)
            base_url = input("Enter the base URL of the site: ").strip()
            if not base_url.startswith(('http://', 'https://')):
                base_url = 'https://' + base_url
            file_path = input("Enter the path to the file to upload: ").strip()
            file_field_name = input("Enter the name of the file upload field: ").strip()
            upload_file_as_image(base_url, file_path, file_field_name)

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
