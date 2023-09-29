import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.short_length = 6  # Change this to set the desired length of the short URL

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(self.short_length))

    def shorten_url(self, long_url):
        if long_url in self.url_map:
            return self.url_map[long_url]

        short_code = self.generate_short_code()
        self.url_map[long_url] = short_code
        return short_code

    def resolve_url(self, short_code):
        for long_url, code in self.url_map.items():
            if code == short_code:
                return long_url
        return None

if __name__ == '__main__':
    url_shortener = URLShortener()

    while True:
        print("1. Shorten URL")
        print("2. Resolve URL")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            long_url = input("Enter the URL to shorten: ")
            short_code = url_shortener.shorten_url(long_url)
            print(f"Shortened URL: http://example.com/{short_code}")
        elif choice == '2':
            short_code = input("Enter the short code: ")
            long_url = url_shortener.resolve_url(short_code)
            if long_url:
                print(f"Original URL: {long_url}")
            else:
                print("Short code not found.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
