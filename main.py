from web_scraping import load_data

print("Search File:", end= " ")
search = input()
print("Limit File:", end= " ")
limit = input()

url = 'https://arxiv.org/search/?query='+ search + '&searchtype=all&source=header'

text = load_data(url, int(limit))

for file_name, text in text.items():
  print("TEXT FROM ", file_name + ": ", text)



