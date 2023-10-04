import requests
print('\n')

# Function to read URLs from a file and check status codes
def check_status_codes(filename):
    print(f'{filename}\n')

    with open(filename, 'r') as file:
       urls = file.read().splitlines() 
    print(urls)

    print('')
    for url in urls:
        url = url.strip()  # Remove any leading whitespace
        try:
            response = requests.get(url)
            print(f"URL: {url}, Status Code: {response.status_code}")
            print('\n')
        except requests.exceptions.RequestException as e:
            print(f"URL: {url}, Error: {e}")
            print('\n')

input_file = 'urls.txt'

check_status_codes(input_file)
