# Image Colorizer
Image Colorizer &amp; Denoiser for Faces, Landscapes &amp; Animals

How to Run ? 
--------------------------------------------------------------------------------------------
- Make two new folders: 'uploads' & 'models' !
- Change drive path in Jupyter Notebook for your dataset and storage of model !
- Run every model generation and training notebook on Jupyter Notebook or any cloud platform like Google Colab or Kaggle !
- Store the generated .h5 models in the 'models' directory for every type of dataset !
- Run GUI using 'streamlit run app.py' on terminal ! (Requirements: pip3 install tensorflow streamlit)
- ![image](https://github.com/Lunatico97/ImageColorizer/assets/60886553/255fc60c-3169-4f8c-999d-3e848c87918e)

1. Model Architecture (Image Colorizer) 
- UNet-128 Autoencoder (Skip Connections)
![image](https://github.com/Lunatico97/ImageColorizer/assets/60886553/a11da112-aab5-4709-af67-637ab0214d93)
- Plots
 ![image](https://github.com/Lunatico97/ImageColorizer/assets/60886553/9dffa96d-de50-48ad-86c9-77e716d520f1)

2. Model Architecture (Image Denoiser) 
- Autoencoder-128 (No Skip Connections & Concatenations)
![image](https://github.com/Lunatico97/ImageColorizer/assets/60886553/28f7eb68-2b87-45cc-8f1e-8cac9b5c7cda)
- Plots
 ![image](https://github.com/Lunatico97/ImageColorizer/assets/60886553/05dfaa4a-279c-4552-9704-022ebd8b3ec2)




