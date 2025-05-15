import streamlit as st
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.logged_in = False
    def login(self):
        self.logged_in = True
    def logout(self):
        self.logged_in = False
class Service:
    def __init__(self, title, description, price, seller):
        self.title = title
        self.description = description
        self.price = price
        self.seller = seller
    def display(self):
        st.subheader(self.title)
        st.write(self.description)
        st.write(f"💖 Seller: {self.seller}")
        st.button(f"Buy for ${self.price}", key=self.title)
class DatabaseSimulator:
    def __init__(self):
        self.users = []
        self.services = []
    def add_user(self, user):
        self.users.append(user)
    def add_service(self, service):
        self.services.append(service)
    def get_services(self):
        return self.services
db = DatabaseSimulator()
demo_user = User("alisha", "alisha@example.com")
db.add_user(demo_user)
db.add_service(Service("Resume", "Get 1-min voice note on your CV.", 1, "alisha"))
db.add_service(Service("Logo Design", "One idea for your logo in PNG.", 1, "alisha"))
st.title("💖 Marketplace")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    st.subheader("Continue")
    username = st.text_input("Username")
    if st.button("Login"):
        if username == "alisha":
            st.session_state.logged_in = True
            st.success("Login Successful 💖")
        else:
            st.error("User not found 💖")
else:
    st.success("Welcome Alisha 💖")
    if st.button("Logout"):
        st.session_state.logged_in = False
    st.header("💖 Services")
    for svc in db.get_services():
        svc.display()
st.markdown("---")


