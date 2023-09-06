from bs4 import BeautifulSoup

html_doc = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dancan Beautifulsoupp</title>
</head>
<body>
<h1>I love django</h1>
    <p>hello am a frontend developer too</p>

    <div class="list-items">
        <ul>
            <li><a href="#">Home</a></li>
            li><a href="#">About Us</a></li>
            li><a href="#">Contact Us</a></li>
        </ul>
    </div>
    
    
</body>'''

soup = BeautifulSoup(html_doc, 'html.parser')

title = soup.title.text
h1  = soup.h1.text
paragraph = soup.p.text
list_items = [li.text for li in soup.ul.find_all('li')]

print("Title:", title)
print("H1:", h1)
print("Paragraph:", paragraph)
print("List Items:", list_items)
