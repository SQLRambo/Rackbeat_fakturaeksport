import requests
import csv

# Base URL for the API
BASE_URL = "https://app.rackbeat.com/api/customer-invoices/{customerInvoice_number}/notes"

# Function to fetch notes for a specific invoice number
def fetch_invoice_notes(invoice_number, bearer_token):
    url = BASE_URL.format(customerInvoice_number=invoice_number)
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json"
    }
    params = {
        "fields": "note_text"
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 206:
        return response.json()  # Assuming the API returns JSON data
    else:
        print(f"Failed to fetch notes for invoice {invoice_number}. Status code: {response.status_code}")
        return None

# Function to read invoice numbers from a semicolon-separated CSV file
def read_invoice_numbers_from_csv(file_path):
    invoice_numbers = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row:  # Ensure the row is not empty
                    invoice_numbers.append(row[0])  # Assuming invoice numbers are in the first column
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return invoice_numbers

# Main function to iterate over invoice numbers and fetch their notes
def main():
    # Prompt the user to enter the bearer token
    bearer_token = input("Enter your bearer token: ").strip()
    if not bearer_token:
        print("Bearer token is required.")
        return

    # Option to read invoice numbers from a CSV file
    csv_file_path = input("Enter the path to the semicolon-separated CSV file (or press Enter to use hardcoded list): ").strip()
    if csv_file_path:
        invoice_numbers = read_invoice_numbers_from_csv(csv_file_path)
    else:
        # Hardcoded list of invoice numbers
        invoice_numbers = [
            "1301",
            "1302",
            "1299"
        ]

    output_file_path = input("Enter the path to save the output CSV file: ").strip()
    try:
        with open(output_file_path, mode='w', encoding='utf-8', newline='') as output_file:
            writer = csv.writer(output_file, delimiter=';')
            writer.writerow(["Invoice Number", "Notes"])  # Write header row

            for invoice_number in invoice_numbers:
                print(f"Fetching notes for invoice: {invoice_number}")
                notes = fetch_invoice_notes(invoice_number, bearer_token)
                if notes:
                    writer.writerow([invoice_number, notes])  # Write invoice number and notes
                else:
                    writer.writerow([invoice_number, "No notes found"])
                print("-" * 50)
        print(f"Output saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

if __name__ == "__main__":
    main()