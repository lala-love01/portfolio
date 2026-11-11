import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

photos=["carroussel1.png","caroussel2.png","caroussel3.png","caroussel4.jpeg"]
slides_html=""
for i,photo in enumerate(photos):
    image_path = Path(__file__).resolve().parents[1] / "assets" / "carroussel" / photo
    with open(image_path, "rb") as img_file:
        image_data = base64.b64encode(img_file.read()).decode("utf-8")
    image_format = "jpeg" if photo.lower().endswith((".jpg", ".jpeg")) else "png"
    active_class = "active" if i == 0 else ""
    slides_html += f"""
    <div class="slide {active_class}">
        <img src="data:image/{image_format};base64,{image_data}" alt="Slide Image">
        <div class="caption">
            <h1>ALCIMA Dieula</h1>
            <p>Informaticienne</p>
        </div>
    </div>
    """

html_code = f"""
<html>
<head>
    <style>
    .slide {{
        display: none;
        position: relative;
        width: 100%;
        height: 100vh;
        min-height: 400px;
        overflow: hidden;
    }}
        .slide.active {{
            display: block;
        }}  
        .slide img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        
        .caption {{
            position: absolute;
            bottom: 40px;
            left: 30%;
            transform: translate(-50%, -50%);
            text-align: center;
            color: white;
            background-color: rgba(0, 0, 0, 0.4);
            padding: 20px 30px;
        }}
    </style>
</head>
<body>
    {slides_html}
    
    <script>
        const slides = document.querySelectorAll(".slide");
        let currentIndex = 0;
        
        setInterval(function(){{
        slides[currentIndex].classList.remove("active");
        currentIndex = (currentIndex + 1) % slides.length;
        slides[currentIndex].classList.add("active");
        }}, 3000);
    </script>
</body>
</html>
"""
components.html(html_code, height=500, scrolling=False)
