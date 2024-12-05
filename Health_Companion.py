import streamlit as st
import random
from PIL import Image

# App-wide customization
st.set_page_config(page_title="BFF", page_icon="🏋️", layout="centered")
st.markdown(
    """
    <style>
        body {
            background-color: #f9f9f9;
            color: #2c3e50;
        }
        .stButton > button {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #2980b9;
        }
        .score-bounties-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 20px;
        }
        .health-score {
            text-align: left;
            font-size: 1.5em;
            color: #333333;
        }
        .commitment-bounties {
            text-align: right;
            font-size: 1.5em;
            color: #333333;
        }
        .icon {
            font-size: 1.8em;
            color: #27ae60;
            margin-right: 10px;
        }
        .coin-icon {
            font-size: 1.8em;
            color: #f1c40f;
            margin-right: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title and subtitle
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 3em;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    <h1 class="title">🏋️BFF</h1>
    """,
    unsafe_allow_html=True
)

# Section: Health Score and Commitment Bounties on the Same Line
health_score = random.randint(50, 100)  # Simulated health score
icon = "✅" if health_score > 75 else "⚠️" if health_score > 50 else "❌"
bounty_amount = random.randint(10, 100)  # Simulated bounty amount
coin_icon = "🪙"

st.markdown(
    f"""
    <div class="score-bounties-container">
        <div class="health-score">
            <span class="icon">{icon}</span>
            <span style="font-size: 25px">Health Score: {health_score} / 100</span>
        </div>
        <div class="commitment-bounties">
            <span class="coin-icon">{coin_icon}</span>
            <span style="font-size: 25px">Commitment Bounties: ${bounty_amount}</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

#st.progress(health_score)

# Section 2: Food Image Upload
st.header("Your Culinary Chronicles")
uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.success("Image uploaded successfully! Analyzing...")
    st.write("Nutritional information feature coming soon!")

# Section 3: Video Section
st.header("🎥 A message from the future")
st.video("https://youtu.be/VbIaO30bv-s")  # Replace with your video URL

# Section 4: Call and Chat
st.header("📞 Connect with your future self")
col1, col2 = st.columns(2)
with col1:
    call_button = st.button("📞 Start Call")
    if call_button:
        st.success("Call feature will connect you shortly...")
with col2:
    chat_button = st.button("💬 Chat with BFF")
    if chat_button:
        st.text_input("Type your message here:")
        st.write("Chat feature is under development.")

# Sidebar for additional features
st.sidebar.title("💡 About the App")
st.sidebar.info(
    """
    This app helps manage obesity by tracking your health score, analyzing food intake, 
    and connecting with a health coach. It is designed for simplicity and effectiveness.
    """
)
st.sidebar.header("Quick Links")
st.sidebar.markdown("- 📈 [Health Tips](https://www.healthline.com/)")
st.sidebar.markdown("- 🥗 [Healthy Recipes](https://www.eatingwell.com/)")

# Footer
st.markdown("---")
st.markdown("**© 2024 Best Future Friend | All rights reserved.**")
