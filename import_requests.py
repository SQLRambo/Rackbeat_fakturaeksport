import requests

def fetch_invoice_notes(api_url, invoice_numbers, api_key):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    invoice_notes = []
    
    for invoice_number in invoice_numbers:
        response = requests.get(f"{api_url}/{invoice_number}/notes", headers=headers)
        
        if response.status_code == 200:
            invoice_notes.append(response.json())
        else:
            print(f"Failed to fetch notes for invoice {invoice_number}: {response.status_code}")
    
    return invoice_notes

if __name__ == "__main__":
    api_url = "https://app.rackbeat.com/api/customer-invoices/{customerInvoice_number}/notes"
    invoice_numbers = ["1301", "1302", "1299"]  # Replace with your actual invoice numbers
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiY2MxODY0MmU4MGVlMGNiYWFlNDc0NzUyZjE4M2U4ZjdiOWI5ZDNlOWZjYzYwODIwNjM5MjE5NmFlMzAwZTkwYjE4M2E1M2JjMjU4MDI1MzQiLCJpYXQiOjE3MDkxMzA2NTMuNTU1MTYsIm5iZiI6MTcwOTEzMDY1My41NTUxNjMsImV4cCI6MjAyNDc0OTg1My41MzQ4NTEsInN1YiI6IjEwMTEyIiwic2NvcGVzIjpbXX0.MXBwV43MOCu8564XhA7KCDqBKLll_Z996hXGykrGg_MPHPkbMPDYnFF4_lWKVGb5oiNvC5KKgQAQ0Fi5zpX9XLVlFJU-pfAhbURuuldAd-l9NyMFDXibTlDHbvd-VNtoJM4mjNq98DrXS-vPQwEMXIwlj0Sd2EyJW7vcqi0_WG01ejsbQ2WezpVa9KX5jzGWrOO2qq_xV2GfeMxh8CKpibz6g-q_s193zRvOcOQrXNOtJht_VkGZi9JBgmzxy6CbAcNVYkl7tAETDO9m_8BET6g9_tJYR-d1vayCs9imkgQrWG6cMM3MkqSTOZT95eni7VwQH1w3mV8PlehBrkulI2fnqr-a1SrS8g9qHKzssbcBbFB3mg7JyfoDvJUIEXapAQCof_WvOfDryWDwmKOTpfb8DcJFmIRqBJydxyIbLIVsbAHoQENs6jsb0rE4NfSZL-ZcYSMqkbmF61UY7BfLcP6k2AO9xTdvOP3o-ksGm15q3gSvpchAzL1MrXtOkmog3_2mak05Ml37AQF-0-UH7xab5ehMmc-j9F7XD3coNmPnbjYNevhPBZg2mYPOe9qkFl_KBPvJz3AWOfAnUvh4fk53vr8gM1D-c6P80xcF6_1LEeOE0-ICiGkM_Wc1XQfIH5wKUXRFiWdJLI0_tt-2dPRAB2Fbukvcrz1ZuoC-ubY"  # Replace with your actual API key
    
    notes = fetch_invoice_notes(api_url, invoice_numbers, api_key)
    print(notes)