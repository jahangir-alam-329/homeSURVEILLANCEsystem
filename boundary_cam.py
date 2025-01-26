import streamlit as st



def boundary_cam():

    
   
    

    # Add a colorful heading
    st.markdown(
        """
        <style>
        .title {
            color: #FF5733;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            background-color: #FFEC40;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 15px rgba(0,0,0,0.2);
        }
        </style>
        <div class="title">
            Main Boundary Side Camera
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add a small description about the camera
    st.markdown("""
        The **Main Boundary Side Camera** is equipped with motion detection capabilities. 
        It is designed to detect any unusual movements such as an individual trying to climb the boundary wall.
        When such movement is detected, the camera triggers an alert and sends an SMS message to the homeowner or security personnel to take necessary action.

        
    """)

    

    

    








# .........................................................................




    import cv2
    import time
    from twilio.rest import Client
    import keys
    import numpy as np
    sms=0

    # Initialize variables
    cap = cv2.VideoCapture(0)  # Use 0 for webcam or specify a video file
    human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')  # Load the cascade for detecting humans



    
    # Twilio setup
    client = Client(keys.account_sid, keys.auth_token)

    def send_alert_sms():
        """Function to send SMS alert."""
        message = client.messages.create(
            body="CHECK YOUR CCTV PLEASE....! Check",
            from_=keys.twilio_number,
            to=keys.my_phone_number
        )
        print(f"SMS Sent: {message.body}")
        return message.body  # Return the message body for feedback in Streamlit

    def detect_humans(frame):
        """Detect humans and draw bounding boxes."""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        humans = human_cascade.detectMultiScale(gray, 1.9, 1)
        for (x, y, w, h) in humans:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame, len(humans) > 0  # Return frame and if humans were detected

    # Streamlit app interface
    #st.title("Human Detection with SMS Alert")

    # Option to enable/disable SMS alerts
    sms_alert_enabled = st.checkbox('Enable SMS Alert', value=True)

    # Placeholder for video stream
    frame_placeholder = st.empty()

    # To track the state of human detection
    previous_detection = False  # To track if humans were detected in the previous frame

    # Loop through the video frames and display them
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            st.write("Error reading frame or video ended.")
            break

        # Detect humans in the frame
        processed_frame, human_detected = detect_humans(frame)

        # Send SMS if a human is detected and SMS is enabled
        if human_detected and sms_alert_enabled and not previous_detection:
            sms_response = send_alert_sms()
            st.write(sms_response)  # Display SMS status in Streamlit

        # Update previous_detection flag for the next frame
        previous_detection = human_detected

        # Convert frame from BGR to RGB (Streamlit expects RGB)
        processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

        # Display the processed frame in Streamlit
        frame_placeholder.image(processed_frame_rgb, channels="RGB",  use_container_width=True)

        # Optionally add a wait time to control the frame rate
        time.sleep(0.1)  # Adjust this value for desired frame rate (in seconds)

    # Release the capture when done
    cap.release()
    frame_placeholder.empty()  # Clear the frame placeholder
    st.write("Video stream finished.")