import streamlit as st 

def main_logic():
    st.title("Welcome to the main page!")
    st.write("This is the main content of the page.")

    user_input=st.text_input("Enter your name" )

    if(user_input):
        st.write(f"Hello, {user_input} Welcome to streamlit application!")



if __name__ == '__main__':
   main_logic()