import xml.etree.ElementTree as ET

root = ET.parse('sample.xml').getroot()
print('Root:', root)

for book in root:
    title = book.find('title').text
    author = book.find('author').text
    year = int(book.find('year').text)
    print(f'Book: {title} by {author} ({year})')