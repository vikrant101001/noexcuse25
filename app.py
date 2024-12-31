import streamlit as st
from openai import OpenAI
import time

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page configuration
st.set_page_config(
    page_title="No Excuse 25 🎯",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextInput, .stTextArea {
        background-color: black;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF2E2E;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    h1 {
        color: #FF4B4B;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 2rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# App header
st.title("No Excuse 25 🎯")
st.markdown("<p class='subtitle'>Transform Your 2025 with Personalized AI Guidance</p>", unsafe_allow_html=True)

# Input fields with custom styling
with st.container():
    personal_info = st.text_area(
        "Personal Information (Optional)",
        placeholder="You can enter your name, age, career if you want, we are not storing any data",
        height=100
    )
    
    year_2024 = st.text_area(
        "How was your 2024?",
        placeholder="Tell us about your year - your achievements, challenges, regrets, and learning experiences",
        height=150
    )
    
    goals_2025 = st.text_area(
        "What do you want to achieve in 2025?",
        placeholder="Share your vision for 2025 - your goals, aspirations, and dreams",
        height=150
    )

def get_advice(personal_info, year_2024, goals_2025):
    prompt = f"""As an expert life coach and strategic advisor, analyze the following information and provide 
    personalized, actionable advice for 2025. Focus on motivation, practical steps, and addressing potential obstacles.

    Personal Information: {personal_info}
    2024 Review: {year_2024}
    2025 Goals: {goals_2025}

    Provide advice in the following format:
    1. Key Insights from 2024 (2-3 points)
    2. Strategic Goals for 2025 (3-4 specific goals)
    3. Action Plan (3-4 concrete steps)
    4. Potential Obstacles and Solutions
    5. Monthly Milestone Suggestions
    6. Motivational Message

    Keep the response concise, practical, and inspiring."""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating advice: {str(e)}"

# Generate button with loading animation
if st.button("Generate My 2025 Roadmap 🚀"):
    if not year_2024 or not goals_2025:
        st.error("Please fill in your 2024 review and 2025 goals to continue.")
    else:
        with st.spinner("Crafting your personalized advice..."):
            advice = get_advice(personal_info, year_2024, goals_2025)
            
            # Display advice with animation
            st.success("Your personalized roadmap is ready!")
            st.markdown("### Your 2025 Success Blueprint 📋")
            st.markdown(advice)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>Made with ❤️ by Vikrant Thoidingjam | "
    "Your data is not stored or saved</p>",
    unsafe_allow_html=True
) 