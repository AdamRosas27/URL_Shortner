import pyshorteners


url_to_shorten = input("Enter the URL you would like to shorten")

type_tiny = pyshorteners.Shortener()
shortened_url = type_tiny.tinyurl.short(url_to_shorten)

print("Shortened URL: " + shortened_url)
