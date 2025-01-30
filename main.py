# -*- coding: utf-8 -*-
"""translator app streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h2kGAgC9ANKOSIBueMP1V7Qnzt-ekLKx
"""

import sys
import streamlit as st
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Add main directory to path
from translator_utils import translate

st.set_page_config(
    page_title = "Language Translator app",
    page_icon = "🤖",
    layout = "centered"
)

#streamlit page title

st.title("Language Translator app")

col1, col2 = st.columns(2)

with col1:
  input_language_list = {"English", "French", "Hindi", "Urdu", "Spanish", "Arabic"}
  input_language = st.selectbox(label = "Input the language", options = input_language_list)

with col2:
  output_language_list = [x for x in input_language_list if x != input_language]
  output_language = st.selectbox(label = "Output language", options = output_language_list)

input_text = st.text_area(label = "Please enter the text")

if st.button("Translate"):
  translate_text = translate(input_language, output_language, input_text)
  st.success(translate_text)
