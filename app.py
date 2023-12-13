import streamlit as st


import app_modules.uber_pickups
import app_modules.bg_remover
import app_modules.calculator
import app_modules.other_example_links

st.set_page_config(layout="wide", page_title="Image Background Remover")

tab1, tab2, tab3, tab4 = st.tabs(["Uber Pickups NYC", "Image Background Remover", "Calculator to Calc Things", "Further Example Links"])

with tab1:
   app_modules.uber_pickups.show_module()


with tab2:
   app_modules.bg_remover.show_module()

with tab3:
   app_modules.calculator.show_module()

with tab4:
   app_modules.other_example_links.show_module()