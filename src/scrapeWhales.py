import requests
from bs4 import BeautifulSoup
from pprint import pp

__all__=[
    'get_data'
]

# Fetch the page
def get_data(url):
    # url = "https://en.wikipedia.org/wiki/Whale"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = {}
    heading = soup.find("h1")
    cont = []

    for section in heading.find_all_next(['p', 'h2', 'h3','h4']):
        if section.name in ['h2', 'h3', 'h4']:  # Stop at the next section
            break
        cont.append(section.text.strip())
    cont = [txt for txt in cont if txt.strip()!=""]

    data[heading.text.strip()] = cont 
    for section in soup.find_all(['h2', 'h3', 'h4']):
        section_title = section.text.strip()
        content = []
        for sibling in section.parent.find_next_siblings():
            if sibling.name in ['h2', 'h3', 'h4']:  # Stop at the next section
                break
            if sibling.name == 'p':
                content.append(sibling.text.strip())
        content = [txt for txt in content if txt.strip()!=""]
        data[section_title]=content
    # Figure out nested titles

    data = {
        hed:cont
        for hed, cont in data.items() if len(cont)>0
    }
    return data
    # data = {
    #     hed: f"{len(cont)} |"+("" if len(cont)==0 else (cont[0][:30]+"..."))
    #     for hed, cont in data.items() if len(cont)>0
    # }
    

