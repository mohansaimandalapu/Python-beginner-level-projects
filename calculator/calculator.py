import streamlit as st
import math

st.markdown('<h1 align="center"> CALCULATOR </h1>',unsafe_allow_html=True)

operator = st.selectbox("",("Addition","Subraction","Division","Multiplication","modulous","tan","sin","cos"))
simple_arthimatic = ["Addition","Subraction","Division","Multiplication","modulous"]
scientific_functions = ["tan","sin","cos"]

if operator in simple_arthimatic :
    first_number = st.text_input("enter first number",value="")
    second_number = st.text_input("enter second number",value="")
    if operator  == "Addition":
        st.write( int(first_number) + int(second_number))
    elif operator == "Subraction":
        st.write( int(first_number) - int(second_number))
    elif operator == "Division":
        st.write( int(first_number) / int(second_number))
    elif operator == "Multiplication":
        st.write( int(first_number) * int(second_number))
    elif operator == "modulous":
        st.write( int(first_number) % int(second_number))

elif operator in scientific_functions:
    number = st.text_input("enter number",value="")
    if operator == "tan":
        st.write(math.tan(int(number)))
    elif operator == "sin":
        st.write(math.sin(int(number)))
    elif operator == "cos":
        st.write(math.cos(int(number)))

        
