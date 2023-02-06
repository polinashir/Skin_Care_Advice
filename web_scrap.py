import requests
from bs4 import BeautifulSoup
import pickle
def scrap():
    url_list=['hyaluronic-acid', 'glycerin', 'urea', 'ascorbic-acid', 'tocopherol', 'epigallocatechin-gallate', 'resveratrol', 'ferulic-acid', 'ethylhexyl-salicylate', 'octocrylene', 'benzophenone-3', 'butyl-methoxydibenzoylmethane', 'bis-ethylhexyloxyphenol-methoxyphenyl-triazine', 'methylene-bis-benzotriazolyl-tetramethylbutylphenol', 'zinc-oxide', 'titanium-titanium-dioxide', 'glycolic-acid', 'lactic-acid', 'mandelic-acid', 'citric-acid', 'malic-acid', 'tartaric-acid', 'salicylic-acid', 'capryloyl-salicylic-acid', 'gluconolactone', 'lactobionic-acid', 'niacinamide', 'zinc', 'benzoyl-peroxide', 'salicylic-acid', 'retinol', 'retinal', 'adapalene', 'tretinoin', 'tazarotene', 'shea-butter-glyceride', 'cocoa-butter-glyceryl-esters', 'ceramide-ng', 'ceramide-ns', 'ceramide-eos', 'azelaic-acid', 'allantoin', 'bisabolol', 'avocado-peptides', 'soy-rice-peptides', 'copper-tripeptide-1']
    all_links=[]
    for url in url_list:
        URL = "https://incidecoder.com/ingredients/"+url
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="content")
        products = results.find_all("div", class_="cardingtitle titlebox-v2 lilac")
        list_produits=[]
        for product in products:
            list_produits.append(product.text.strip())
        #print(list_produits)
        more_products=results.find_all("a", class_="klavika simpletextlistitem")
        for product in more_products:
            list_produits.append(product.text.strip())
        #print(list_produits)
        all_links.append(list_produits)
    with open('outfile', 'wb') as fp:
        pickle.dump(all_links, fp)
    return all_links


