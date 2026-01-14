"""Streamlit Web App: Medical AI Assistant Triage System

This is a LIVE, DEPLOYABLE demo app for the Medical AI Assistant.
Deploy to Streamlit Cloud, Heroku, or AWS for live product.
"""

import streamlit as st
import json
from src.triage_agent import TriageAgent

# Configure page
st.set_page_config(
    page_title="Medical AI Triage System",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #f0f8ff;
}
.metric-box {
    background-color: #e6f2ff;
    padding: 20px;
    border-radius: 10px;
    margin: 10px 0;
}
.critical {
    background-color: #ffcccc;
    color: #cc0000;
    font-weight: bold;
}
.warning {
    background-color: #ffffcc;
    color: #ff9900;
}
.safe {
    background-color: #ccffcc;
    color: #009900;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    st.session_state.agent = TriageAgent(confidence_threshold=0.70)

if 'results' not in st.session_state:
    st.session_state.results = None

# Header
st.title("🏥 Medical AI Assistant: Triage System")
st.markdown("**AI-powered Emergency Severity Index (ESI) Classification**")
st.markdown("---")

# Sidebar - Instructions
with st.sidebar:
    st.header("📋 Instructions")
    st.write("""
    1. Enter patient's chief complaint
    2. Input vital signs
    3. Click 'Analyze Patient'
    4. AI will provide ESI triage level
    5. Review confidence score and recommendations
    """)
    
    st.markdown("---")
    st.header("ℹ️ ESI Levels")
    st.write("""
    - **Level 1**: Immediate life-saving intervention
    - **Level 2**: High-risk situation
    - **Level 3**: Stable, single resource needed
    - **Level 4**: Stable, single resource (simple)
    - **Level 5**: Stable, minimal resources
    """)
    
    st.markdown("---")
    st.info("🔒 All patient data is processed locally and NOT stored.")

# Main content - Two columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Patient Information")
    
    # Chief Complaint
    chief_complaint = st.text_input(
        "Chief Complaint",
        placeholder="e.g., Difficulty breathing, Chest pain, Fever",
        help="Describe the patient's main complaint"
    )
    
    # Vital Signs
    st.subheader("Vital Signs")
    vital_cols = st.columns(5)
    
    with vital_cols[0]:
        rr = st.number_input(
            "Respiratory Rate\n(breaths/min)",
            min_value=0,
            max_value=60,
            value=16,
            step=1
        )
    
    with vital_cols[1]:
        hr = st.number_input(
            "Heart Rate\n(bpm)",
            min_value=0,
            max_value=200,
            value=72,
            step=1
        )
    
    with vital_cols[2]:
        sbp = st.number_input(
            "Systolic BP\n(mmHg)",
            min_value=0,
            max_value=300,
            value=118,
            step=1
        )
    
    with vital_cols[3]:
        temp = st.number_input(
            "Temperature\n(°C)",
            min_value=35.0,
            max_value=42.0,
            value=36.8,
            step=0.1
        )
    
    with vital_cols[4]:
        o2 = st.number_input(
            "O2 Saturation\n(%)",
            min_value=70,
            max_value=100,
            value=98,
            step=1
        )
    
    # Analyze Button
    if st.button("🔍 Analyze Patient", key="analyze", use_container_width=True):
        if not chief_complaint:
            st.error("⚠️ Please enter a chief complaint")
        else:
            patient_data = {
                'chief_complaint': chief_complaint,
                'vitals': {
                    'respiratory_rate': rr,
                    'heart_rate': hr,
                    'systolic_bp': sbp,
                    'temperature': temp,
                    'o2_saturation': o2
                }
            }
            
            st.session_state.results = st.session_state.agent.classify(patient_data)
            st.success("✅ Analysis complete!")

# Results Section
if st.session_state.results:
    st.markdown("---")
    st.subheader("📊 Triage Results")
    
    results = st.session_state.results
    esi_level = results['esi_level']
    confidence = results['confidence']
    escalate = results['escalate']
    
    # Color coding
    if esi_level in ['1', '2']:
        color_class = "critical"
        emoji = "🚨"
    elif esi_level == '3':
        color_class = "warning"
        emoji = "⚠️"
    else:
        color_class = "safe"
        emoji = "✅"
    
    # Display results in columns
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(
            "ESI Level",
            esi_level,
            f"{emoji} {results['recommendation']}"
        )
    
    with res_col2:
        st.metric(
            "Model Confidence",
            f"{confidence:.1%}",
            f"Threshold: {st.session_state.agent.confidence_threshold:.0%}"
        )
    
    with res_col3:
        status = "⚠️ ESCALATE" if escalate else "✅ PROCEED"
        st.metric(
            "Clinical Action",
            status,
            "Manual Review" if escalate else "AI Decision"
        )
    
    # Detailed explanation
    st.info(f"**AI Reasoning**: {results['reasoning']}")
    
    if escalate:
        st.warning(
            "⚠️ **ESCALATION ALERT**: Model confidence is below threshold. "
            "This case should be reviewed by a clinician immediately."
        )
    
    # Show patient data
    with st.expander("📋 View Patient Data"):
        st.json(patient_data)
    
    # Show model explanation
    with st.expander("🧠 Model Details"):
        st.write("""
        **Triage Algorithm:**
        - Analyzes vital signs against clinical thresholds
        - Flags critical chief complaints
        - Provides confidence scores
        - Escalates uncertain cases to clinicians
        
        **Guardrails:**
        - Zero tolerance for hallucinations
        - Human-in-the-loop for low-confidence predictions
        - Real-time bias monitoring
        """)

# Footer
st.markdown("---")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.caption("📊 [View Metrics](https://github.com/Usha2025-git/medical-ai-assistant-pm/blob/main/METRIC_PLAN.md)")

with col_b:
    st.caption("📄 [Read PRD](https://github.com/Usha2025-git/medical-ai-assistant-pm/blob/main/PRD.md)")

with col_c:
    st.caption("🔬 [Responsible AI](https://github.com/Usha2025-git/medical-ai-assistant-pm)")

st.caption("🚀 *This is a live AI product demo. Deploy to Streamlit Cloud, Heroku, or AWS.*")
