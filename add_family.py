import streamlit as st

def add_family():
    from PIL import Image

    st.markdown(
        """
        <style>
        .title {
            color: #FFA500;  /* Orange color */
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            background-color: #FFF3E5;  /* Light orange background */
            padding: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
        }
        </style>
        <div class="title">
            Add Family Member
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add a description about the page
    st.markdown("""
        Welcome to the **Add Family Member** page! Here you can easily register new family members by uploading their images and providing their names.
        
        These details will be stored in the database, and the camera system will later be able to identify them when they come into view.
        
        ### How It Works:
        1. Upload a photo of the family member.
        2. Provide their name for recognition purposes.
        3. The photo and name are saved to the database for later use.
        4. The camera will recognize known family members as they appear in front of the camera.

        This process helps make your home security system smarter and more personal by recognizing the faces of the people who live there.
    """)
    # Display image related to the system (example image)
    image_path = "member.jpg"  # Make sure the image is in the same folder
    st.image(image_path, caption="-------------------------------------------------------------------------",  use_container_width=True)






    import cv2
    import numpy as np
    import face_recognition
    import mysql.connector
    import io
    from PIL import Image

    # Database connection setup
    def connect_to_database():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # XAMPP default password is empty
            database="facial_recognition"
        )


    # Function to insert an image into the database
    def insert_image_to_db(name, image):
        conn = connect_to_database()
        cursor = conn.cursor()
        
        # Convert image to binary
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_data = img_byte_arr.getvalue()
        
        query = "INSERT INTO users (name, image) VALUES (%s, %s)"
        cursor.execute(query, (name, img_data))
        conn.commit()
        cursor.close()
        conn.close()


        # Option to upload new image
    uploaded_image = st.file_uploader("Upload a New Image for Registration", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        # Show uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        name = st.text_input("Enter Name for this Image")

        if st.button("Save Image to Database"):
            if name:
                img = Image.open(uploaded_image)
                insert_image_to_db(name, img)
                st.success(f"Image for {name} saved to the database!")
            else:
                st.error("Please enter a name!")