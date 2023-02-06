import parse_to_tree
import web_scrap
import pickle

#all_links=web_scrap.scrap()
with open ('outfile', 'rb') as fp:
    all_links= pickle.load(fp)

def cut_before_capital(s):
    for i, c in enumerate(s):
        if c.isupper():
            return s[i:]
    return s
def get_percentage(all_links):
    new_all_links=[]
    new_list_products=[]
    for list_products in all_links:
        for s in list_products:
            before=s.split('%')[0]
            if(if_float(before)):
                new_list_products.append(before)
            else:
                new_list_products.append('NaN')
        new_all_links.append(new_list_products)
    return new_all_links

def if_float(element):
    try:
        float(element)
    except ValueError:
        return False
    return True

def text_formatting(all_links):
    new_links=[]
    for list_products in all_links:
        list_products_corrected = [s.replace('-', '') for s in list_products]
        list_products_corrected = [s.replace(' ', '_') for s in list_products_corrected]
        list_products_corrected = [s.replace('"', '') for s in list_products_corrected]
        list_products_corrected = [s.replace('™', '') for s in list_products_corrected]
        list_products_corrected = [s.replace('|_', '') for s in list_products_corrected]
        list_products_corrected = [cut_before_capital(s) for s in list_products_corrected]
        new_links.append(list_products_corrected)
    return new_links
def extract_products(all_links, product_types):
    products=[]
    all_products=[]
    for list_products in all_links:
        list_products_corrected = [s.replace('-', '') for s in list_products]
        all_products.append(list_products_corrected)
    flat_list = [item for sublist in all_products for item in sublist]
    for type in product_types:
        type_products = []
        for subtype in type:
            for prod in flat_list:
                if(subtype in prod):
                    type_products.append(prod)
        products.append(type_products)
    return products

ontology_actifs=['hyaluronic_acid', 'glycerin', 'urea', 'vitamin_c', 'vitamin_e', 'egcg/green_tea', 'resveratrol', 'ferulic_acid', 'octysalate', 'octocrylene', 'oxybenzone', 'avobenzone', 'tinosorb_s', 'tinosorb_m', 'zinc_oxyde', 'titanium_dioxyde', 'glycolic_acid', 'lactic_acid', 'mandelic_acid', 'citric_acid', 'malic_acid', 'tartaric_acid', 'salicylic_acid', 'capryloyl_salicylic_Acid', 'gluconolactone', 'lactobionic_acid', 'niacinamide', 'zinc', 'benzoyl_peroxide', 'salicylic_acid', 'retinol', 'retinal', 'adapalene', 'tretinoin', 'tazarotene', 'shea_butter', 'cocoa_butter', 'ceramide_ng', 'ceramide_ns', 'ceramide_eos', 'azelaic_acid', 'allantoin', 'bisabolol', 'avocado_peptides', 'soy-rice_peptides', 'copper_peptides']
product_types=['Oil', 'Lotion', 'Wash', 'Cleanser', 'Cream', 'Gel', 'Serum', 'Scrub', 'Astringent', 'Moisturizer', 'Toner', 'Solution', 'Essence', 'Treatment', 'Spray', 'Pads', 'Mask', 'Powder',  'Sunscreen', 'Exfoliant', 'Butter']
product_types_all=[['Oil'], ['Lotion'], ['Wash', 'Facewash'], ['Cleanser'], ['Cream'], ['Gel'], ['Serum'], ['Scrub', 'Enzyme'], ['Astringent'], ['Moisturizer', 'Moisturizing'], ['Toner'], ['Solution'], ['Essence'], ['Treatment'], ['Spray'], ['Pads'], ['Mask'], ['Powder'],  ['Sunscreen', 'SPF', 'Sun block'], ['Exfoliant'], ['Butter']]
products=extract_products(all_links, product_types_all)
products_formatted=text_formatting(products)
#products_formatted_flat=[item for sublist in products_formatted for item in sublist]
percantages = get_percentage(all_links)
product_list=text_formatting(all_links)
#clean_product_list=[]
#for list_products in product_list:
#    clean_product_sublist=[x for x in list_products if x in set(products_formatted_flat)]
    #clean_product_list.append(clean_product_sublist)
#print(products)

for i in range(len(product_types)):
    parse_to_tree.add_product(products_formatted[i], product_types[i])
    print('added product', i)
for i in range(len(ontology_actifs)):
    parse_to_tree.add_products_for_class(product_list[i], "has_active_substance", ontology_actifs[i])
    print('added link', i)
for i in range(len(percantages)):
   parse_to_tree.add_percantage(product_list[i], "concentration", percantages[i])
   print('added concentration', i)
parse_to_tree.save()
