import streamlit as st
import os
from PIL import Image

# Configure page for mobile responsiveness
st.set_page_config(
    layout="centered",
    initial_sidebar_state="collapsed",
    page_icon="🖼️"
)

# Custom CSS for responsive image display
st.markdown("""
<style>
    /* Remove all padding and margins */
    .block-container, .stApp {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    /* Full-width container */
    .image-container {
        display: flex;
        flex-direction: column;
        width: 100%;
        gap: 0;
    }
    
    /* Responsive image styling */
    .stImage img {
        width: 100% !important;
        height: auto !important;
        display: block !important;
        margin-bottom: 0 !important;
    }
    
    /* Hide Streamlit UI elements */
    header, footer, [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* Remove space between images */
    .stImage {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# List of images to display
image_files = ["i1.png", "i1.png", "i4.png", "i2.jpg"]

# Main app
with st.container():
    for image_file in image_files:
        try:
            # Check if file exists
            if not os.path.exists(image_file):
                st.error(f"File not found: {image_file}")
                continue
                
            # Display image
            st.image(
                image_file,
                use_container_width=True,
                caption="",
                output_format="auto"
            )
        except Exception as e:
            st.error(f"Error loading {image_file}: {str(e)}")