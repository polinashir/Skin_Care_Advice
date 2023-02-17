import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sparql
st.write("Please select")
col1, col2, col3, col4 = st.columns(4)

with col1:
    skin_type=st.selectbox("Your skin type", ['Combination Skin', 'Dry Skin', 'Normal Skin', 'Oily Skin', 'Sensitive Skin'])

with col2:
    if(skin_type=='Combination Skin'):
        skin_conditions=st.multiselect("A desired effect", ['Acne fighting', 'Anti Aging', 'Brightening', 'Control Sebum', 'Exfoliating', 'Moisturizing and Hydratation', 'Sun Protection'])
    if (skin_type == 'Oily Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Acne fighting', 'Anti Aging', 'Brightening', 'Control Sebum', 'Exfoliating', 'Sun Protection'])
    if (skin_type == 'Dry Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Anti Aging', 'Emollients', 'Moisturizing and Hydratation', 'Sun Protection'])
    if (skin_type == 'Normal Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Anti Aging', 'Antioxidant', 'Moisturizing and Hydratation', 'Sun Protection'])
    if (skin_type == 'Sensitive Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Anti Aging', 'Anti Redness', 'Moisturizing and Hydratation', 'Sun Protection'])
with col3:
    product_type = st.multiselect("A desired product type", ['Oil', 'Lotion', 'Wash', 'Cleanser', 'Cream', 'Gel', 'Serum', 'Scrub', 'Astringent', 'Moisturizer', 'Toner', 'Solution', 'Essence', 'Treatment', 'Spray', 'Pads', 'Mask', 'Powder',  'Sunscreen', 'Exfoliant', 'Butter'])
with col4:
    price_range = st.multiselect("A desired price range", ['Low_range_Products', 'Mid_range_Products', 'High_range_Products'])

def word_transform(word):
    return word.replace(' ', '_').lower()
def list_transform(list):
    new_list=[]
    for word in list:
        new_list.append(word_transform(word))
    return new_list

def show_results(list_prod, i):
    st.write(i,') Product name :', list_prod[i][1])
    st.write('The main actif :', list_prod[i][0])
    st.write('Brand :', list_prod[i][2])
    st.write('Usage :', list_prod[i][5])
    st.write('Price :', list_prod[i][4])
    if (list_prod[i][3] != 'None'):
        st.write('Product concentration :', list_prod[i][3])
list_prod=[]
if st.button('Search', type="primary", key='search'):
    #st.write(word_transform(skin_type), list_transform(skin_conditions), list_transform(product_type))
    print(skin_conditions)
    list_prod=sparql.all_products(list_transform(skin_conditions), product_type, price_range)
    col4, col5, col6 = st.columns(3)
    for i in range(len(list_prod)):
        show_results(list_prod, i)


