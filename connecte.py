from pymongo import MongoClient
from PIL import Image
import streamlit as st
def getData(url,index):
    client = MongoClient(url)
    db = client.Index
    col=db.Index

    x = col.find_one({"index": index})
    cluster=x['cluster']
    edge_value=x['edge_value']
    return cluster,edge_value

def image_from_dir(index):
    dir_path = "C:/Users/21622/PycharmProjects/Index_Recherche/thumbnails/thumbnails/0"
    path=dir_path + "/" + str(index) +".jpg"
    img=Image.open(path)
    return(img)


def load_image(image_file):
	img = Image.open(image_file)
	return img

def mongoconn(url):
    Client=MongoClient(url)
    try:
        conn=MongoClient()
        st.success('Connected Successfully To Mongo')
    except:
        st.warning('Could not connect')

def collection():
    client=MongoClient('mongodb://localhost:27017')
    db=client.Index
    collection=db.Index
    return(collection)