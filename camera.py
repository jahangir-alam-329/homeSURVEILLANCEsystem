import streamlit as st

def camera():
    from PIL import Image

   


    
    

    

    # Custom styling using HTML for title color
    st.markdown("""
        <h1 style="color: #FF5733; text-align: center;">🚪 Main Door Camera Access</h1>
    """, unsafe_allow_html=True)

    # Add a short description
    st.write("""
        Welcome to the **Main Door Camera Access System**, a secure system that uses **Facial Recognition** to grant access to authorized individuals.
        
        The camera identifies faces in real-time and checks them against a database of registered faces. If the person is recognized, access is granted. If not, access is denied.
        
        
    """)

    # Display image related to the system (example image)
    image_path = "door.jpg"  # Make sure the image is in the same folder
    st.image(image_path, caption="Main Door Camera in Action",  use_container_width=True)

    


    






    # ..........................................................


    

    
    import cv2
    import numpy as np
    import face_recognition
    import mysql.connector
    import io
    

    # Database connection setup
    # create database in xampp server i.e, "facial_recognition" and table name "users"
    def connect_to_database():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # XAMPP default password is empty
            database="facial_recognition"
        )




    #...................................................................................................
    # # Function to insert an image into the database
    # def insert_image_to_db(name, image):
    #     conn = connect_to_database()
    #     cursor = conn.cursor()
        
    #     # Convert image to binary
    #     img_byte_arr = io.BytesIO()
    #     image.save(img_byte_arr, format='JPEG')
    #     img_data = img_byte_arr.getvalue()
        
    #     query = "INSERT INTO users (name, image) VALUES (%s, %s)"
    #     cursor.execute(query, (name, img_data))
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    # ................................................................................................





    # Function to retrieve all stored images from the database
    def retrieve_images_from_db():
        conn = connect_to_database()
        cursor = conn.cursor()
        
        query = "SELECT name, image FROM users"
        cursor.execute(query)
        
        users = cursor.fetchall()
        known_encodings = []
        known_names = []
        
        for user in users:
            name, image_data = user
            # Convert image binary back to numpy array
            img = Image.open(io.BytesIO(image_data))
            img = np.array(img)
            encoding = face_recognition.face_encodings(img)
            
            if encoding:  # Ensure at least one face is detected
                known_encodings.append(encoding[0])
                known_names.append(name)
        
        cursor.close()
        conn.close()
        
        return known_encodings, known_names

    # Function to recognize faces from webcam video feed
    def recognize_faces_in_frame(frame, known_encodings, known_names):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        names = []
        for encoding, location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            face_distances = face_recognition.face_distance(known_encodings, encoding)

            name = "Unknown"
            if True in matches:
                best_match_index = np.argmin(face_distances)
                name = known_names[best_match_index]

            # Draw a box around the face
            top, right, bottom, left = location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

            names.append(name)
        return frame, names

    
       # .............................................................................................






    # Display video feed and recognize faces
    known_encodings, known_names = retrieve_images_from_db()

    if known_encodings and known_names:
        st.write("Loaded stored images from database...")

        # Placeholder for video feed
        frame_placeholder = st.empty()

        # Start webcam feed for real-time recognition
        cap = cv2.VideoCapture(0)  # 0 for default webcam

        while True:
            ret, frame = cap.read()

            if not ret:
                st.write("Error capturing video.")
                break

            # Recognize faces in the frame
            processed_frame, recognized_names = recognize_faces_in_frame(frame, known_encodings, known_names)

            # Convert frame to RGB for Streamlit display
            rgb_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

            # Display the frame in Streamlit
            frame_placeholder.image(rgb_frame, channels="RGB",  use_container_width=True)

        cap.release()
        frame_placeholder.empty()
    else:
        st.write("No faces in the database yet.") 



