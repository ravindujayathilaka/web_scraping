import requests as re

response = re.get('https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNRGsyTTJvMWVnc0tDUzl0THpBNU5qTnFOU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNRGsyTTJvMUtBQVABUAE?hl=en-US&gl=US&ceid=US%3Aen')
html = response.text

print(html)