from scrapeWhales import *
from pprint import pp

data = (get_data("https://en.wikipedia.org/wiki/Whale"))

data = {
    hed: f"{len(cont)} |"+("" if len(cont)==0 else (cont[0][:30]+"..."))
    for hed, cont in data.items() if len(cont)>0
}

pp(data)