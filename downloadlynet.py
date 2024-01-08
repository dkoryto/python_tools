import subprocess

def install_package(package):
    try:
        subprocess.check_call(["python3", "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package {package}: {str(e)}")

def extract_links(url):
    try:
        import requests
    except ImportError:
        install_package('requests')
        import requests

    try:
        from bs4 import BeautifulSoup
    except ImportError:
        install_package('beautifulsoup4')
        from bs4 import BeautifulSoup

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)

        # Filtrowanie linków zawierających 'dl[1-9].downloadly.ir' oraz kończących się na .rar lub .zip
        filtered_links = [link['href'] for link in links if any(f'dl{i}.downloadly.ir' in link['href'] for i in range(1, 10)) and (link['href'].endswith('.rar') or link['href'].endswith('.zip'))]

        return filtered_links
    except requests.RequestException as e:
        print(f"Error during requests to {url}: {str(e)}")
        return None

def save_links_to_file(links, filename='download.txt'):
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')

# Ask user for URL input
url = input("Enter the URL to extract links from: ")

links = extract_links(url)
if links:
    save_links_to_file(links)
    print("Links found and saved to download.txt:")
    for link in links:
        print(link)
else:
    print("No links found or error occurred.")
