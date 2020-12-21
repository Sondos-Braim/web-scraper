import requests
from bs4 import BeautifulSoup

url='https://en.wikipedia.org/wiki/Automation'

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    cite_elems = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return (len(cite_elems))
    
def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    paragraphs=[]
    for result in results:
        if result not in paragraphs:
            paragraphs.append(result.findParent().text.strip())
    paragraphs = list(dict.fromkeys(paragraphs))

    with open('sentences.text','r') as file:
        content=file.readlines()
    str=''
    content=str.join(content)
    sentences=content.split('[citation needed]')  
    return sentences
if __name__ == "__main__":
    print(get_citations_needed_report(url))