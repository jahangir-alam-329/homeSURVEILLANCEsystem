import streamlit as st


def about():
    
    from PIL import Image

    # Streamlit Page Configuration
    

    # Customizing the page with markdown
    st.markdown("""
        <style>
            .title {
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                color: #2e7d32;
            }
            .subtitle {
                font-size: 20px;
                text-align: center;
                color: #555555;
            }
            .description {
                font-size: 18px;
                color: #333333;
                margin-top: 20px;
            }
            .image-container {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Project Title
    st.markdown('<div class="title">Smart Home Surveillance System</div>', unsafe_allow_html=True)

    # Project Subtitle
    st.markdown('<div class="subtitle">A Secure and Intelligent Monitoring System for Your Home</div>', unsafe_allow_html=True)

    # Add the local image (home_safety.jpg) from the same folder
    image_path = "home_safety.jpg"  # Ensure this image is in the same folder as the script
    img = Image.open(image_path)
    st.image(img, caption="Smart Home Surveillance",  use_container_width=True)

    # Project Description
    st.markdown("""
        <div class="description">
            The **Smart Home Surveillance System** is a cutting-edge solution designed to provide home owners 
            with real-time monitoring, increased security, and peace of mind. 
            This system integrates multiple smart cameras within your home, 
            allowing you to access live footage, receive alerts, and even control the system remotely from 
            your smartphone or computer. With the use of machine learning, 
            the system can distinguish between regular and suspicious activities, 
            providing more efficient and automated security features.
                


            
            Key Features:
            - Real-time monitoring through live video feeds.
            - Motion detection and automated alerts.
            - Remote access and control via smartphone or computer.
            - Facial recognition and object detection for enhanced security.
            

            Whether you're at home or away, the Smart Home Surveillance System keeps you connected and ensures your 
            home remains safe and secure.
        </div>
    """, unsafe_allow_html=True)
