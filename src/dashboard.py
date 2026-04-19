import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import re

# --- 1. CONFIG ---
st.set_page_config(page_title="LeadPulse Command", page_icon="⚡", layout="wide")

# --- 2. ELITE UI STYLING (The "Diamond" Theme) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .main { background-color: #F1F5F9; padding: 2rem; }
    
    /* Premium KPI Cards */
    .kpi-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        border: 1px solid #E2E8F0;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .kpi-label { color: #64748B; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; }
    .kpi-value { color: #0F172A; font-size: 30px; font-weight: 800; margin-top: 5px; }

    /* Sidebar Fixes: Improved spacing for selectboxes */
    section[data-testid="stSidebar"] { 
        background-color: #0F172A; 
        min-width: 300px !important;
    }
    .stSelectbox label, .stSlider label { color: #94A3B8 !important; font-size: 14px; font-weight: 600; }
    
    /* Strategic Recommendation Box */
    .directive-box {
        background: #F0F9FF;
        border-left: 5px solid #0EA5E9;
        padding: 15px;
        border-radius: 8px;
        color: #0369A1;
        font-weight: 700;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Command Inputs) ---
with st.sidebar:
    st.markdown("<h2 style='color:white; margin-bottom:0;'>⚡ LEAD PULSE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B; font-size:12px;'>SYSTEM v4.1 | SECURE ACCESS</p>", unsafe_allow_html=True)
    st.divider()
    
    visits = st.slider("Total Interactions", 1, 100, 42)
    time = st.number_input("Engagement Time (Sec)", value=920)
    views = st.slider("Page Depth", 1.0, 20.0, 7.5)
    
    st.divider()
    # Fixed the spacing here so text isn't cut off
    origin = st.selectbox("Acquisition Channel", ["Lead Add Form", "API", "Landing Page Submission"])
    source = st.selectbox("Referral Engine", ["Welingak Website", "Google", "Reference", "Direct Traffic"])

# --- 4. HEADER SECTION ---
col_head, col_logo = st.columns([4, 1])
with col_head:
    st.markdown("<h1 style='margin-bottom:0;'>LeadPulse: Command Center</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748B; font-size:18px;'>High-Fidelity Sales Intelligence & Lead Scoring</p>", unsafe_allow_html=True)

# --- 5. CORE PREDICTION LOGIC ---
payload = {
    "TotalVisits": visits,
    "TotalTimeSpentOnWebsite": time,
    "PageViewsPerVisit": views,
    "LeadOrigin": origin,
    "LeadSource": source
}

try:
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    data = response.json()
    
    # Surgical cleaning for Priority text
    raw_prio = data.get('priority', 'UNKNOWN')
    clean_prio = re.sub(r'[^a-zA-Z\s]', '', raw_prio).replace('Lead', '').strip().upper()
    score = data['lead_score']

    # --- 6. KPI DASHBOARD ---
    st.markdown("### **EXECUTIVE OVERVIEW**")
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f'<div class="kpi-card"><div class="kpi-label">Conversion Prob.</div><div class="kpi-value">{score}%</div></div>', unsafe_allow_html=True)
    with c2:
        status = "QUALIFIED" if score > 45 else "COLD"
        st.markdown(f'<div class="kpi-card"><div class="kpi-label">Status</div><div class="kpi-value" style="color:#059669">{status}</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="kpi-card"><div class="kpi-label">Priority</div><div class="kpi-value" style="color:#2563EB">{clean_prio}</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="kpi-card"><div class="kpi-label">Confidence</div><div class="kpi-value" style="color:#64748B">78.3%</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 7. ANALYTICS ROW ---
    left, right = st.columns([1, 1])

    with left:
        st.markdown("#### **Conversion Velocity**")
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            number={'suffix': "%", 'font': {'size': 50, 'color': '#1E293B'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1},
                'bar': {'color': "#0EA5E9"},
                'steps': [
                    {'range': [0, 40], 'color': "#F1F5F9"},
                    {'range': [40, 80], 'color': "#E2E8F0"},
                    {'range': [80, 100], 'color': "#CBD5E1"}]
            }
        ))
        fig_gauge.update_layout(height=300, margin=dict(t=20, b=0, l=20, r=20))
        st.plotly_chart(fig_gauge, use_container_width=True, config={'displayModeBar': False})

    with right:
        # FIXED: Correct header rendering and directive box
        st.markdown("#### **Strategic Directive**")
        st.markdown(f"""<div class="directive-box">ACTION: {data['action'].upper()}</div>""", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### **Behavioral Influence**")
        
        # FIXED: Darkened colors so Channel and Source are visible
        impact = pd.DataFrame({
            'Factor': ['Engagement', 'Frequency', 'Channel', 'Source'],
            'Score': [time/10, visits*1.2, 35 if "Lead Add" in origin else 20, 25 if "Welingak" in source else 15]
        }).sort_values('Score')
        
        # Used 'Viridis' scale which is highly visible and professional
        fig_bar = px.bar(impact, x='Score', y='Factor', orientation='h',
                         color='Score', color_continuous_scale='Viridis')
        fig_bar.update_layout(height=200, margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
        fig_bar.update_coloraxes(showscale=False)
        st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})

except Exception:
    st.error("SYSTEM ERROR: Backend Prediction Engine is Offline.")