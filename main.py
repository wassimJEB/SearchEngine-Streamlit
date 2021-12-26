import streamlit as st
from KMeans_Meth import *
from connecte import *
from Color import *

url='mongodb://localhost:27017/'
collection =collection()





def main():


    st.markdown("<h1 style='text-align: center; color: red;'>Indexation Par Contenue</h1>", unsafe_allow_html=True)
    rf = rgb_feature.ColorDescriptor((8, 8, 8))


    c = st.selectbox("Choisir une option", ["Télécharger une image", "Télecharger CSV"]);
    if c == "Télécharger une image":
        img_file_buffer = st.file_uploader("Upload  image", type=["png", "jpg", "jpeg"])

        if img_file_buffer is not None:
            name=img_file_buffer.name
            type=img_file_buffer.type
            file_details = {"FileName":name, "FileType": type}
            #st.write(file_details)
            img = load_image(img_file_buffer)
            features = rf.describe(img_file_buffer)
            st.success("Done!")
            with st.expander("Similaires"):
                st.image(img, width=250)


        submit = st.button("Run")
        value=st.slider('Combien de photos similaire ', min_value=0, max_value=100)

        if submit:
            print(value)
            mongoconn(url)

            client = MongoClient('mongodb://localhost:27017/Index')
            #print(items)
            index = int(name.split('.')[0])
            #st.text(index)
            cluster,edge_img = getData(url,index)
            #print(cluster)
            similar_picture = [{"result": 0, "index": index}]


            similar_picture_chi = [{"result": 0, "index": index}]
            for col in collection.find({"cluster": cluster}):
                if col["index"] == index:
                    continue
                else:
                    edge = col["edge_value"]
                    dist = calcDistance(edge_img, edge)
                    dist_chi = chi2_distance(edge_img, edge)
                    similar_picture.append({"result": dist, "index": col["index"]})
                    similar_picture_chi.append({"result": dist_chi, "index": col["index"]})


            #st.write(cluster)
            with st.expander("the similar images:"):
                similar_picture = sorted(similar_picture, key=lambda x: x["result"])
                similar_picture_chi = sorted(similar_picture_chi, key=lambda x: x["result"])
                if len(similar_picture) > value:
                    similar_picture = similar_picture[:value+1]

                for i in range(0, value, 2):
                    col = st.columns(2)
                    index = similar_picture[i + 1]["index"]
                    col[0].image(image_from_dir(str(index)))
                    index = similar_picture[i + 2]["index"]
                    col[1].image(image_from_dir(str(index)))  # use_column_width=True)
            with st.expander("ch2_distance"):
                for i in range(0, value, 2):
                    col = st.columns(2)
                    index = similar_picture_chi[i + 1]["index"]
                    col[0].image(image_from_dir(str(index)))
                    index = similar_picture_chi[i + 2]["index"]
                    col[1].image(image_from_dir(str(index)))  # use_column_width=True)


        st.markdown("<h5 style='text-align: center; color: red;'>'Wassim JEBALI & Hassin CHAHED INDP3_AIM '</h5>", unsafe_allow_html=True)


if __name__=='__main__':
    main()




