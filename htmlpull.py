import requests

url = 'https://www.cnn.com'

# Send GET request to retrieve the HTML content
response = requests.get(url)

if response.status_code == 200:
    # Save the HTML content to a text file
    with open('cnn_html.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
        print("HTML content saved to cnn_html.txt")
else:
    print(f"Error: {response.status_code}")