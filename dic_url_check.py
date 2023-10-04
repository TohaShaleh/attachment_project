import requests
print('')

# Function to read URLs from a file and check status codes
def check_status_codes(filename):
    print(f'{filename}\n')

    with open(filename, 'r') as file:
       urls = file.read().splitlines() 

    dic1={

        'fb':'https://www.facebook.com',
        'yt':'https://www.youtube.com',
        'gfg':'https://www.geeksforgeeks.com',
        'wa':'https://www.whatsapp.com',
        'ab':'https://aboltabol.com',
        'er':'https://example.com/page1'
    }
   
    dic2={}
    a=input('Enter the Original url : ')
    b=input('Enter the short form of the Url : ')
    print('\n')
    dic2[b]=a

    dic={}
    h=0
    for i in urls:
        value=i
        key1='a';
        key2=chr(ord(key1[-1]) + h)
        key=key1+key2
        dic[key]=i
        h=h+1

    for i,j in dic.items():
        print(f'The key is : {i} & its url value is : {j}')
    print('\n')
    for i,j in dic1.items():
        print(f'The key is : {i} & its url value is : {j}')

    dic2.update(dic1)
    dic2.update(dic)
    
    print(f'\n{dic2}\n')
    print('\n')
    for i in range(0,3):
        try:
            url=input('enter the short url : ')
            s=dic2[url]
            response = requests.get(s)
            print(f"Original URL Name: {s} and it's Status Code: {response.status_code}\n")
            if response.status_code==200:
                print('The url link is successful and live\n')
            if response.status_code==404:
                print('The url link is not found..It gives Error\n')

        except requests.ConnectionError:
            print(f'{s} is unreachable\n')
            print('')
            print('')

input_file = 'urls.txt'

check_status_codes(input_file)