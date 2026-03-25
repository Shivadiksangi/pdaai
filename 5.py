import streamlit as st

st.title("welcome to streamlit app")

num1= st.number_input("Enter the first number")
num2= st.number_input("Enter the second number")
selected_operation= st.selectbox("Select the operation", ["Addition", "Subtraction", "Multiplication", "Division"])
if st.button("Calculate"):
    if selected_operation=="Addition":
        st.write("Result:", num1+num2)
    elif selected_operation=="Subtraction":
        st.write("Result:", num1-num2)
    elif selected_operation=="Multiplication":
        st.write("Result:", num1*num2)
    elif selected_operation=="Division":
        if num2!=0:
            st.write("Result:", num1/num2)
        else:
            st.write("Error: Division by zero is not allowed")
