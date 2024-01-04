import requests

def get_website_size(url):
    try:
        response = requests.head(url, allow_redirects=True)
        size_in_bytes = int(response.headers.get('content-length', 0))
        size_in_mb = size_in_bytes / (1024 * 1024)
        return size_in_mb
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

url = 'https://example.com'
website_size = get_website_size(url)

if website_size is not None:
    print(f"The size of {url} is approximately {website_size:.2f} MB.")
else:
    print(f"Failed to retrieve the size of {url}.")