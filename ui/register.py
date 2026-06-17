import streamlit as st

from database.user_service import register_user


def register_page():

    st.title("📝 Register")

    name = st.text_input(
        "Full Name",
        key="register_name"
    )

    email = st.text_input(
        "Email",
        key="register_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="register_password"
    )

    if st.button("Register"):

        success, message = register_user(
            name,
            email,
            password
        )

        if success:
            st.success(message)

        else:
            st.error(message)