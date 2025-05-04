import streamlit as st
import requests
import markdown as md

API_URL = "http://127.0.0.1:8000"

# Session state
if "token" not in st.session_state:
    st.session_state.token = None
if "username" not in st.session_state:
    st.session_state.username = None

# ----------------------
# SIGNUP and LOGIN
# ----------------------
st.sidebar.title("Authentication")

auth_choice = st.sidebar.radio("Choose", ["Signup", "Login"])

if auth_choice == "Signup":
    st.sidebar.subheader("Signup")
    new_user = st.sidebar.text_input("Username")
    new_pass = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Create Account"):
        res = requests.post(f"{API_URL}/signup", json={"username": new_user, "password": new_pass})
        st.sidebar.success(res.json().get("message", "Signup successful."))

elif auth_choice == "Login":
    st.sidebar.subheader("Login")
    user = st.sidebar.text_input("Username")
    pw = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        res = requests.post(f"{API_URL}/login", json={"username": user, "password": pw})
        if res.status_code == 200:
            st.session_state.token = res.json()["token"]
            st.session_state.username = user
            st.sidebar.success("Login successful.")
        else:
            st.sidebar.error(res.json().get("error", "Login failed."))

# ----------------------
# MAIN APP
# ----------------------
st.title("📝 Falcon Blog")

if st.session_state.token:
    st.success(f"Logged in as {st.session_state.username}")
    
    menu = st.selectbox("Choose action", ["Create Post", "View Posts"])

    if menu == "Create Post":
        st.subheader("📌 Create a New Blog Post")
        title = st.text_input("Title")
        content = st.text_area("Content (Markdown supported)", height=200)
        if st.button("Publish"):
            headers = {"Authorization": st.session_state.token}
            data = {"title": title, "content": content}
            res = requests.post(f"{API_URL}/posts", headers=headers, json=data)
            if res.status_code == 200:
                st.success("Post published.")
            else:
                st.error("Error publishing post.")
    
    elif menu == "View Posts":
        st.subheader("📚 All Posts")
        res = requests.get(f"{API_URL}/posts")
        if res.status_code == 200:
            for post in res.json():
                st.markdown(f"### {post['title']} by `{post['author']}`")
                st.markdown(post['content_html'], unsafe_allow_html=True)

                with st.expander("💬 Comments"):
                    # Show comments
                    cres = requests.get(f"{API_URL}/posts/{post['id']}/comments")
                    if cres.status_code == 200:
                        for c in cres.json():
                            st.markdown(f"- **{c['author']}**: {c['content']}")
                    else:
                        st.write("No comments")

                    # Add a comment
                    if st.session_state.token:
                        comment = st.text_input(f"Add Comment to Post #{post['id']}", key=post['id'])
                        if st.button("Submit Comment", key=f"btn_{post['id']}"):
                            headers = {"Authorization": st.session_state.token}
                            data = {"content": comment}
                            res = requests.post(f"{API_URL}/posts/{post['id']}/comments", headers=headers, json=data)
                            if res.status_code == 200:
                                st.success("Comment added")
                            else:
                                st.error("Error adding comment")
else:
    st.warning("Please login or sign up to use the app.")
