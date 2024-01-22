import streamlit as st
import numpy as np
import cv2
from keras.models import load_model
from io import BytesIO
import matplotlib.image as mpimg

def rgb2gray(rgb):
    value = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140]) ;
    return value ;

st.sidebar.markdown("<h1 style='text-align: center;'>Image Colorizer</h1>",
            unsafe_allow_html=True)

# Filepath from root
path = "/home/diwas/Downloads/" ;

option = st.sidebar.selectbox("Choose Image Type", ["Person", "Animal", "Flower", "Landscape"])
option  = option.lower()

img_file = st.sidebar.file_uploader(
    "Upload Image", type=["jpg", "jpeg", "png"])
print(img_file)

select = "No" ;

jitter = st.sidebar.checkbox(label="Does it need denoising ? [Jitters/Marks]") ;
if jitter:
    select = st.sidebar.selectbox("Choose a denoiser", ["Normal", "Extreme [WARNING: Blur effect]"])


# Load colorizer model
image = [] ;
colorizer = '' ;
denoiser = load_model

if option == "person":
    del colorizer ;
    colorizer = load_model(f'{path}/Streamlit App/models/autoEncoderCNN_colorizer_celebs.h5') ;
elif option == "landscape":
    del colorizer ;
    colorizer = load_model(f'{path}/Streamlit App/models/autoEncoderCNN_colorizer_landscape.h5') ;
else:
    del colorizer ;
    colorizer = load_model(f'{path}/Streamlit App/models/autoEncoderCNN_colorizer_augmented_linnaeus5.h5') ;

# Load denoiser model
denoiser = '' ;

if select == "Normal":
    del denoiser ;
    denoiser = load_model(f'{path}/Streamlit App/models/autoEncoderCNN_denoiser_celebs_lownoise.h5') ;
elif select == "No":
    st.sidebar.write('No denoiser selected !') ;
else:
    del denoiser ;
    denoiser = load_model(f'{path}/Streamlit App/models/autoEncoderCNN_denoiser_linnaeus5.h5') ;

if img_file is not None:
    try:
        image = np.array(mpimg.imread(img_file), dtype=np.float32) ;
        print(img_file.type) ;
        if img_file.type != "image/png":
            image = image/255 ;
        if image.ndim > 2:
            image = rgb2gray(image) ;
        print(image) ;
        image = cv2.resize(image, (128,128)) ;
        btn = st.sidebar.button('Colorize') ;

        if btn:
            colored = colorizer.predict(image.reshape(1,128,128,1)) ;
            colored = np.clip(colored[0], 0.0, 1.0) ;
            if jitter:
                denoised = denoiser.predict(colored.reshape(1,128,128,3)) ;
                colored = np.clip(denoised[0], 0.0, 1.0) ;

            if img_file.type != "png":
                colored = (colored*255).astype(np.uint8) ;

            col1, col2 = st.columns(2)
            with col1:
                st.image(image, width=200, caption="Original")
            with col2:
                st.image(colored, width=200, caption="Colored")

            

            print(img_file.name) ;
            mpimg.imsave(f'{path}/Streamlit App/uploads/colored_{img_file.name}', colored) ;




    except Exception as e:
        st.write(e)
        st.write("Unable to open file")