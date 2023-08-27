import hashlib
import string
import random

class URLShortener:
    def _init_(self):
        self.url_map = {}
        self.short_length = 8
        self.base_url = "http://short.url/"

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.short_length))

    def shorten_url(self, long_url):
        hash_object = hashlib.sha256(long_url.encode())
        hash_hex = hash_object.hexdigest()
        
        if hash_hex in self.url_map:
            return self.url_map[hash_hex]
        
        short_code = self.generate_short_code()
        short_url = f"{self.base_url}{short_code}"
        
        self.url_map[hash_hex] = short_url
        return short_url

    def expand_url(self, short_url):
        short_code = short_url.replace(self.base_url, '')
        for hash_hex, stored_short_url in self.url_map.items():
            if stored_short_url.endswith(short_code):
                return stored_short_url
        return "Short URL not found"

# Example usage
url_shortener = URLShortener()

long_url1 = "https://www.example.com/page1"
short_url1 = url_shortener.shorten_url(long_url1)
print(f"Shortened URL for {long_url1}: {short_url1}")

long_url2 = "https://www.example.com/page2"
short_url2 = url_shortener.shorten_url(long_url2)
print(f"Shortened URL for {long_url2}: {short_url2}")

expanded_url = url_shortener.expand_url(short_url1)
print(f"Expanded URL for {short_url1}: {expanded_url}")

# Trying to expand a non-existent short URL
non_existent_short_url = "http://short.url/nonexistent"
expanded_non_existent = url_shortener.expand_url(non_existent_short_url)
print(f"Expanded URL for {non_existent_short_url}: {expanded_non_existent}")