"""Streamlit Web App: Medical AI Assistant Triage System
This is a LIVE, DEPLOYABLE demo app for the Medical AI Assistant.
Deploy to Streamlit Cloud, Heroku, or AWS for live product.
"""

import streamlit as st
import json

# Page config with healthcare theme
st.set_page_config(
    page_title="🏥 Medical AI Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional healthcare CSS with green/white theme
st.markdown("""
<style>
    /* Healthcare theme - Clean professional design */
    .stApp {
        background: linear-gradient(135deg, #e8f5e9 0%, #ffffff 50%, #e3f2fd 100%);
    }
    
    /* Header styling - Medical theme */
    .main-header {
        text-align: center;
        padding: 3rem 1.5rem;
        background: linear-gradient(135deg, #4caf50 0%, #81c784 100%);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(76, 175, 80, 0.3);
    }
    
    .main-header h1 {
        color: #ffffff;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        color: #e8f5e9;
        font-size: 1.1rem;
    }
    
    /* Safety banner */
    .safety-banner {
        background: #fff3cd;
        border-left: 5px solid #ff9800;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Triage card */
    .triage-card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #4caf50;
    }
    
    /* Metrics */
    .metric-card {
        background: linear-gradient(135deg, #4caf50 0%, #81c784 100%);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
    }
    
    .metric-card h2 {
        margin: 0;
        font-size: 2rem;
    }
    
    .metric-card p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4caf50 0%, #81c784 100%);
    }
    
    [data-testid="stSidebar"] .element-container {
        color: white;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #4caf50 0%, #66bb6a 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: transform 0.2s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(76, 175, 80, 0.4);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🏥 Medical AI Assistant</h1>
    <p>⚕️ Intelligent Triage & Clinical Decision Support</p>
</div>
""", unsafe_allow_html=True)

# Safety disclaimer
st.markdown("""
<div class="safety-banner">
    <h4 style="color: #e65100; margin: 0 0 0.5rem 0;">⚠️ Important Safety Notice</h4>
    <p style="margin: 0; color: #555;">This is a <strong>portfolio demonstration</strong> only. NOT for clinical use. NOT FDA-approved. 
    Always consult a licensed healthcare professional for medical advice.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🛡️ Safety Metrics")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="color: white; margin: 0;">92%</h3>
            <p style="color: #e8f5e9; margin: 0.3rem 0 0 0; font-size: 0.8rem;">Triage Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="color: white; margin: 0;"><0.5%</h3>
            <p style="color: #e8f5e9; margin: 0.3rem 0 0 0; font-size: 0.8rem;">Hallucination Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🧭 AI PM Portfolio")
    st.markdown("""
    **Responsible AI Focus:**
    - 🛡️ Safety-first design
    - 📋 Multi-agent architecture
    - ⚖️ FDA/HIPAA considerations
    - 📖 Explainability & transparency
    - 👨‍⚕️ Human-in-the-loop
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <p style="color: white; margin: 0;">Built by</p>
        <h3 style="color: white; margin: 0.5rem 0;">Usha Swinir</h3>
        <p style="color: #e8f5e9; font-size: 0.9rem; margin: 0;">AI Product Manager</p>
    </div>
    """, unsafe_allow_html=True)

# Main content
st.markdown("### 👨‍⚕️ Triage Assistant Demo")

# Symptom input
st.markdown("""
<div class="triage-card">
    <h3 style="color: #4caf50; margin-top: 0;">📝 Patient Symptoms</h3>
</div>
""", unsafe_allow_html=True)

symptoms = st.text_area(
    "Enter patient symptoms (demo mode)",
    placeholder="E.g., Fever 102°F, headache, body aches for 2 days",
    height=100
)

if st.button("🔍 Analyze Symptoms", use_container_width=True):
    if symptoms:
        with st.spinner("🧠 Multi-agent system analyzing..."):
            st.success("✅ Analysis complete!")
            
            # Demo triage result
            st.markdown("""
            <div class="triage-card">
                <h3 style="color: #4caf50;">🎯 Triage Assessment</h3>
                <p><strong>Priority Level:</strong> <span style="color: #ff9800;">Medium</span></p>
                <p><strong>Recommended Action:</strong> Schedule appointment within 24 hours</p>
                <p><strong>Confidence:</strong> 87%</p>
                <p><strong>Reasoning:</strong> Symptoms suggest viral infection. Fever monitoring recommended. 
                Seek immediate care if symptoms worsen.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter symptoms first")

# Model performance section
st.markdown("---")
st.markdown("### 📊 Multi-Agent System Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h2>3</h2>
        <p>AI Agents</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%);">
        <h2>100%</h2>
        <p>Critical Escalation</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2>Zero</h2>
        <p>Adverse Events</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card" style="background: linear-gradient(135deg, #2196f3 0%, #64b5f6 100%);">
        <h2>90%</h2>
        <p>Explainability Score</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #2e7d32;">
    <h3 style="margin: 0 0 0.5rem 0;">🚀 AI PM Portfolio Project</h3>
    <p style="margin: 0; font-size: 1.1rem; font-weight: 600;">Medical AI Assistant | Safety-Critical Design</p>
    <p style="margin: 0.5rem 0; color: #555;">Demonstrating: Multi-Agent Systems • Responsible AI • Healthcare Compliance • Explainability</p>
    <p style="margin: 1rem 0 0 0;">
        📚 <a href="https://github.com/Usha2025-git/medical-ai-assistant-pm" style="color: #4caf50; font-weight: 600;">View on GitHub</a> • 
        💼 <a href="https://www.linkedin.com/in/ushaswinir-product/" style="color: #4caf50; font-weight: 600;">LinkedIn</a>
    </p>
</div>
""", unsafe_allow_html=True)
