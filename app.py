import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np


def predict(image):
    model = tf.keras.models.load_model("model")
    image = image.resize((256, 256))
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    result = model.predict(img_array)[0][0]
    rounded_result = round(result, 2)
    return "The height of the child is {:.2f} cm".format(rounded_result)

st.title("Child Height Detection")
upload_file = st.file_uploader("Upload depthmap image of the child", type = ['jpg', 'png', 'jpeg'])
generate_pred = st.button("Predict")

if generate_pred:
    image = Image.open(upload_file)
    with st.expander('image', expanded=True):
        st.image(image, use_column_width=True)
    st.markdown(f"<h2>{predict(image)}</h2>", unsafe_allow_html=True)

