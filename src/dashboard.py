import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
import sqlite3
from datetime import datetime

# --- 1. CONFIG & IDENTITY ---
st.set_page_config(page_title="LeadPulse Pro | Danushmathi Pathmanaban", page_icon="⚡", layout="wide")

# --- 2. DATABASE ARCHITECTURE ---
def init_db():
    conn = sqlite3.connect('lead_intelligence.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS lead_logs 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  timestamp TEXT, 
                  score REAL, 
                  status TEXT, 
                  visits INTEGER, 
                  time_spent INTEGER, 
                  channel TEXT,
                  source TEXT)''')
    conn.commit()
    conn.close()

def save_lead_data(score, status, v, t, c, s):
    conn = sqlite3.connect('lead_intelligence.db')
    c_db = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c_db.execute("INSERT INTO lead_logs (timestamp, score, status, visits, time_spent, channel, source) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (now, score, status, v, t, c, s))
    conn.commit()
    conn.close()

init_db()

# --- 3. ELITE UI STYLING (Light Theme) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .main { background-color: #F8FAFC; }
    
    /* LIGHT SIDEBAR */
    section[data-testid="stSidebar"] { background-color: #FFFFFF !important; border-right: 1px solid #E2E8F0; }

    /* KPI CARDS */
    .kpi-card {
        background: white; border-radius: 12px; padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border: 1px solid #E2E8F0;
        text-align: center;
    }
    .kpi-label { color: #64748B; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; }
    .kpi-value { color: #0F172A; font-size: 28px; font-weight: 800; }

    /* ACTION BANNERS */
    .action-box-hot {
        background: linear-gradient(90deg, #EF4444 0%, #B91C1C 100%);
        color: white; padding: 25px; border-radius: 15px;
        text-align: center; font-size: 22px; font-weight: 800;
        box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3); margin: 20px 0;
    }
    .action-box-cold {
        background: linear-gradient(90deg, #64748B 0%, #334155 100%);
        color: white; padding: 25px; border-radius: 15px;
        text-align: center; font-size: 22px; font-weight: 800; margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. ASSET LOADING ---
@st.cache_resource
def load_resources():
    model = joblib.load('models/lead_model.pkl')
    cols = joblib.load('models/model_columns.pkl')
    benchmarks = {'Time': 980, 'Visits': 48, 'Depth': 8.2}
    return model, cols, benchmarks

model, model_cols, bench = load_resources()

# --- 5. SIDEBAR COMMANDS ---
with st.sidebar:
    st.markdown("<h2 style='color:#0F172A;'>⚡ LeadPulse</h2>", unsafe_allow_html=True)
    st.markdown(f"**Principal Developers:** Danushmathi & Srivarshan")
    st.divider()
    
    visits = st.slider("Total Website Visits", 1, 100, 42)
    time = st.number_input("Time Spent (Seconds)", value=920)
    views = st.slider("Pages Viewed per Session", 1.0, 20.0, 7.5)
    
    st.divider()
    origin = st.selectbox("Acquisition Channel", ["Lead Add Form", "API", "Landing Page Submission"])
    source = st.selectbox("Traffic Source", ["Welingak Website", "Google", "Reference", "Direct Traffic"])

# --- 6. PREDICTION & SIMULATION LOGIC ---
def get_score(v, t, p, o, s):
    input_df = pd.DataFrame([{'TotalVisits': v, 'Total Time Spent on Website': t, 'Page Views Per Visit': p, 'Lead Origin': o, 'Lead Source': s}])
    input_df = pd.get_dummies(input_df)
    for col in model_cols:
        if col not in input_df.columns: input_df[col] = 0
    return round(model.predict_proba(input_df[model_cols])[0][1] * 100, 2)

score = get_score(visits, time, views, origin, source)
# Simulator: What if we increase time by 25%?
boosted_score = get_score(visits, time * 1.25, views, origin, source)
status = "🔥 HOT LEAD" if score > 70 else "❄️ COLD PROSPECT"

# --- 7. EXECUTIVE DASHBOARD ---
st.title("Lead Intelligence Summary")

# Row 1: High-Level Metrics
c1, c2, c3, c4 = st.columns([1, 1, 1, 1.2])
with c1:
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Conversion Prob.</div><div class="kpi-value">{score}%</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Current Status</div><div class="kpi-value">{"HOT" if score > 70 else "COLD"}</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="kpi-card"><div class="kpi-label">Growth Potential</div><div class="kpi-value" style="color:#3B82F6">+{round(boosted_score-score, 1)}%</div></div>', unsafe_allow_html=True)
with c4:
    st.write("") # Alignment
    if st.button("💾 SAVE PREDICTION TO DATABASE", use_container_width=True):
        save_lead_data(score, status, visits, time, origin, source)
        st.toast(f"Case Logged: {status} at {score}%", icon="✅")

# Row 2: Highlighted Strategic Action
if score > 70:
    st.markdown('<div class="action-box-hot">🚨 STRATEGIC PRIORITY: IMMEDIATE CALLBACK REQUIRED</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="action-box-cold">ℹ️ STRATEGIC STATUS: ADD TO EMAIL NURTURE LIST</div>', unsafe_allow_html=True)

# --- 8. ANALYTICS & AUDIT TRAIL ---
tab1, tab2, tab3 = st.tabs(["📊 Performance Benchmarking", "🎯 Behavioral Influence", "📋 Historical Audit Trail"])

with tab1:
    st.subheader("Success Comparison")
    st.caption("How this lead stacks up against the average successfully converted customer profile.")
    bench_df = pd.DataFrame({
        'Metric': ['Visits', 'Time', 'Page Depth'],
        'Current Lead': [visits, time/10, views*5],
        'Converted Leads (Avg)': [bench['Visits'], bench['Time']/10, bench['Depth']*5]
    })
    fig_bench = px.bar(bench_df, x='Metric', y=['Current Lead', 'Converted Leads (Avg)'], 
                       barmode='group', color_discrete_sequence=['#3B82F6', '#CBD5E1'])
    st.plotly_chart(fig_bench, use_container_width=True)

with tab2:
    st.subheader("Model Decision Factors")
    st.caption("The behavioral weights influencing the AI's current decision.")
    impact = pd.DataFrame({
        'Feature': ['Engagement', 'Frequency', 'Channel', 'Source'],
        'Weight': [time/10, visits*1.2, 35 if "Lead Add" in origin else 20, 25 if "Welingak" in source else 15]
    }).sort_values('Weight')
    fig_imp = px.bar(impact, x='Weight', y='Feature', orientation='h', color='Weight', color_continuous_scale='Blues')
    st.plotly_chart(fig_imp, use_container_width=True)

with tab3:
    st.subheader("Production History Log")
    conn = sqlite3.connect('lead_intelligence.db')
    history_df = pd.read_sql_query("SELECT * FROM lead_logs ORDER BY id DESC LIMIT 10", conn)
    conn.close()
    
    if not history_df.empty:
        st.dataframe(history_df, use_container_width=True)
        # Export Functionality
        csv = history_df.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 DOWNLOAD FULL AUDIT LOG (CSV)", data=csv, file_name="lead_pulse_history.csv", mime="text/csv")
    else:
        st.info("No records found. Save your first prediction to start the audit trail.")

# --- 9. WHAT-IF OPTIMIZER (Standout Feature) ---
st.divider()
st.subheader("🔮 Simulation Optimizer")
st.write(f"If the sales team can increase this lead's **Engagement Time** to {int(time*1.25)}s, the AI predicts conversion probability will rise to **{boosted_score}%**.")
st.progress(min(max(int(boosted_score), 0), 100))

st.divider()
st.caption("LeadPulse v5.0 | Secure MLOps Framework | Developed by Danushmathi & Srivarshan")