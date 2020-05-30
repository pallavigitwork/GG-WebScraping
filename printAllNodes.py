from bs4 import BeautifulSoup
from lxml import html
import requests

#This function is used to provide and calculate the absolute xpath for a web element
def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if siblings == [child] else
            '%s[%d]' % (child.name, 1 + siblings.index(child))
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)

url=input("Provide the url of your application: ")
tag=input("Provide the tag, use True if you want all tags: ")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

#display the tag and all attributes
if(tag=="True"):
    tag=True
for child in soup.find_all(tag):
    print(child.name)
    attrib=child.attrs
    for p,k in attrib.items():
        print(p,": ",k)
    print("abs xml path: ", xpath_soup(child))
    print("----------------------")
        
    