import streamlit as st
from about import about
from camera import camera
from add_family import add_family
from boundary_cam import boundary_cam

# Function to display different pages based on selection
def main():
    # Sidebar for page selection
    page = st.sidebar.selectbox("Choose a page", ("About🏠", "Camera", "Add Family", "boundary_cam"))
    
    # Call the respective page function based on selection
    if page == "About🏠":
        about()
    elif page == "Camera":
        camera()
    elif page == "boundary_cam":
        boundary_cam()
    else:
        add_family()

# Run the app
if __name__ == "__main__":
    main()





# -- Create the database
# CREATE DATABASE IF NOT EXISTS facial_recognition;

# -- Switch to the facial_recognition database
# USE facial_recognition;

# -- Create the users table
# CREATE TABLE IF NOT EXISTS users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     image LONGBLOB NOT NULL
# );
