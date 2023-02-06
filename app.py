import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sparql
st.write("Please select")
col1, col2, col3 = st.columns(3)

with col1:
    skin_type=st.selectbox("Your skin type", ['Combination Skin', 'Dry Skin', 'Normal Skin', 'Oily Skin', 'Sensitive Skin'])

with col2:
    if(skin_type=='Combination Skin'):
        skin_conditions=st.multiselect("A desired effect", ['Acne fighting', 'Anti Aging', 'Brightening', 'Control Sebum', 'Exfoliating', 'Moisturizing', 'Sun Protection'])
    if (skin_type == 'Oily Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Acne fighting', 'Anti Aging', 'Brightening', 'Control Sebum', 'Exfoliating', 'Sun Protection'])
    if (skin_type == 'Dry Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Anti Aging', 'Emollients', 'Moisturizing', 'Sun Protection'])
    if (skin_type == 'Normal Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Anti Aging', 'Antioxidant', 'Moisturizing', 'Sun Protection'])
    if (skin_type == 'Sensitive Skin'):
        skin_conditions = st.multiselect("A desired effect", ['Anti Aging', 'Anti Redness', 'Moisturizing', 'Sun Protection'])
with col3:
    product_type = st.multiselect("A desired product type", ['Oil', 'Lotion', 'Wash', 'Cleanser', 'Cream', 'Gel', 'Serum', 'Scrub', 'Astringent', 'Moisturizer', 'Toner', 'Solution', 'Essence', 'Treatment', 'Spray', 'Pads', 'Mask', 'Powder',  'Sunscreen', 'Exfoliant', 'Butter'])

def word_transform(word):
    return word.replace(' ', '_').lower()
def list_transform(list):
    new_list=[]
    for word in list:
        new_list.append(word_transform(word))
    return new_list


st.write(word_transform(skin_type), list_transform(skin_conditions), list_transform(product_type))
st.write(sparql.all_products(list_transform(skin_conditions)))