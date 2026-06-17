import streamlit as st

from database.user_service import login_user


def login_page():

    st.title("🔐 Login")

    email = st.text_input(
        "Email",
        key="login_email"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login"):

        success, user = login_user(
            email,
            password
        )

        if success:

            st.session_state["user"] = {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }

            st.success(
                f"Welcome {user.name}"
            )

            st.session_state["page"] = "Dashboard"
            st.rerun()

        else:

            st.error(
                "Invalid Credentials"
            )