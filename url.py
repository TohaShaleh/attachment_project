import requests
print('\n')

def check_urls(urls):
    for url in urls:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                print(f'{url} is live')
                print('')

            elif response.status_code == 404:
                print(f'{url} is live but returns status code 404 (Not Found)')
                print('')
        
            else:
                print(f'{url} is returning status code {response.status_code}')
                print('')

        except requests.ConnectionError:
            print(f'{url} is unreachable')
            print("")

def main():
    urls = [
        'https://example.com',
        'https://google.com',
        'https://nonexistenturl123456789.com',
        'https://example.com/blahblah',
        'https://facebook.com',
        'https://youube.com',
        'https://geeksforgeeks.com',
        'https://example.com/nonexistent-page'
    ]
    check_urls(urls)

print('\n')

if __name__ == '__main__':
    main()
