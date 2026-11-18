"""Consistent, accessible groundwater dashboard theme."""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

:root {
  --gw-navy: #102F46;
  --gw-navy-2: #17435D;
  --gw-teal: #087E8B;
  --gw-teal-dark: #066875;
  --gw-aqua: #EAF4F5;
  --gw-ink: #17324D;
  --gw-muted: #536B80;
  --gw-line: #D5E2E9;
  --gw-white: #FFFFFF;
  --gw-soft: #F5F9FA;
}

html, body, [class*="css"] {
  font-family: 'DM Sans', sans-serif;
}
.stApp {
  background: var(--gw-aqua);
  color: var(--gw-ink);
}
.block-container {
  padding-top: 1.6rem;
  padding-bottom: 3rem;
  max-width: 1500px;
}

/* Sidebar and navigation */
section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, var(--gw-navy) 0%, var(--gw-navy-2) 100%);
  border-right: 1px solid #28546A;
}
section[data-testid="stSidebar"] * {
  color: #F4FAFC !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label {
  padding: .52rem .68rem;
  border-radius: 9px;
  margin: .13rem 0;
  transition: background .15s ease;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
  background: rgba(255,255,255,.12);
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
  background: rgba(38, 190, 184, .22);
  outline: 1px solid rgba(145, 232, 222, .35);
}

/* Main-page typography */
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stMarkdownContainer"] li,
.stApp [data-testid="stCaptionContainer"] {
  color: var(--gw-muted);
}
h1, h2, h3, h4, h5, h6 {
  color: var(--gw-navy) !important;
  font-weight: 750 !important;
  letter-spacing: -.02em;
}
.page-title {
  font-size: 2rem;
  font-weight: 800;
  color: var(--gw-navy);
  margin: 0 0 .25rem;
  letter-spacing: -.04em;
}
.page-subtitle {
  color: var(--gw-muted);
  font-size: 1rem;
  margin-bottom: 1.45rem;
}
a, a:visited {
  color: var(--gw-teal);
}

/* Metric cards */
div[data-testid="stMetric"] {
  background: var(--gw-white);
  border: 1px solid var(--gw-line);
  border-radius: 15px;
  padding: 17px 18px;
  box-shadow: 0 5px 18px rgba(16,47,70,.06);
}
div[data-testid="stMetric"] label,
div[data-testid="stMetric"] label p {
  color: var(--gw-muted) !important;
  font-weight: 600;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
  color: var(--gw-teal) !important;
  font-weight: 800 !important;
}
div[data-testid="stMetricDelta"] {
  font-size: .8rem;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button,
div[data-testid="stFormSubmitButton"] button,
.stPopover > button {
  border-radius: 10px;
  border: 1px solid var(--gw-teal) !important;
  background: linear-gradient(105deg, var(--gw-teal), #159BA0) !important;
  color: #FFFFFF !important;
  font-weight: 700;
  padding: .55rem 1rem;
}
.stButton > button p,
.stDownloadButton > button p,
div[data-testid="stFormSubmitButton"] button p {
  color: #FFFFFF !important;
}
.stButton > button:hover,
.stDownloadButton > button:hover,
div[data-testid="stFormSubmitButton"] button:hover {
  background: var(--gw-teal-dark) !important;
  border-color: var(--gw-teal-dark) !important;
  color: #FFFFFF !important;
}

/* Inputs, selects and text areas */
.stApp input,
.stApp textarea,
.stApp [data-baseweb="select"] > div {
  color: var(--gw-ink) !important;
}
.stApp input,
.stApp textarea {
  background: #FFFFFF !important;
  border-color: #B8CBD6 !important;
}
.stApp input::placeholder,
.stApp textarea::placeholder {
  color: #718697 !important;
  opacity: 1;
}
.stApp label,
.stApp label p {
  color: var(--gw-ink);
}
div[data-testid="stAlert"] {
  border-radius: 12px;
}
div[data-testid="stExpander"] {
  background: #FFFFFF;
  border: 1px solid var(--gw-line);
  border-radius: 12px;
}
.stDataFrame {
  border: 1px solid var(--gw-line);
  border-radius: 12px;
  overflow: hidden;
}
div[data-testid="stTabs"] button {
  color: var(--gw-ink) !important;
  font-weight: 650;
}
hr {
  border-color: var(--gw-line);
}

/* Hero and section components */
.hero-panel {
  background: linear-gradient(115deg, var(--gw-navy) 0%, var(--gw-teal) 100%);
  color: #FFFFFF;
  border-radius: 20px;
  padding: 25px 28px;
  margin: .2rem 0 1.3rem;
  box-shadow: 0 12px 28px rgba(8,126,139,.16);
}
.hero-panel h2,
.hero-panel h3,
.hero-panel p {
  color: #FFFFFF !important;
}
.hero-panel p {
  margin: 0;
}
.section-kicker {
  color: var(--gw-teal);
  font-size: .76rem;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.footer {
  text-align: center;
  color: #647D8E;
  font-size: .8rem;
  padding: 1.4rem 0 .5rem;
  border-top: 1px solid var(--gw-line);
  margin-top: 2rem;
}
[data-testid="stPopover"] > button {
  border-radius: 999px !important;
}

/* Better contrast for the floating chatbot popover */
div[data-testid="stPopoverBody"] {
  width: min(410px, calc(100vw - 28px)) !important;
  max-height: 76vh !important;
  overflow-y: auto !important;
  background: #FFFFFF !important;
  color: var(--gw-ink) !important;
  border: 1px solid var(--gw-line) !important;
  border-radius: 17px !important;
  box-shadow: 0 16px 48px rgba(16,47,70,.24) !important;
}
div[data-testid="stPopoverBody"] * {
  color: var(--gw-ink);
}
div[data-testid="stPopoverBody"] h1,
div[data-testid="stPopoverBody"] h2,
div[data-testid="stPopoverBody"] h3,
div[data-testid="stPopoverBody"] p,
div[data-testid="stPopoverBody"] label {
  color: var(--gw-ink) !important;
}
div[data-testid="stPopoverBody"] [data-testid="stCaptionContainer"],
div[data-testid="stPopoverBody"] [data-testid="stCaptionContainer"] p {
  color: var(--gw-muted) !important;
}
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] {
  background: #F2F8F9 !important;
  color: var(--gw-ink) !important;
  border: 1px solid #D8E7EA !important;
  border-radius: 13px !important;
  padding: .7rem !important;
  margin: .45rem 0 !important;
}
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] p,
div[data-testid="stPopoverBody"] [data-testid="stChatMessage"] li {
  color: var(--gw-ink) !important;
}
div[data-testid="stPopoverBody"] .stTextInput input {
  background: #FFFFFF !important;
  color: var(--gw-ink) !important;
  border: 1px solid #B8CBD6 !important;
  border-radius: 9px !important;
}
div[data-testid="stPopoverBody"] .stTextInput input::placeholder {
  color: #718697 !important;
}
div[data-testid="stPopoverBody"] .stButton button,
div[data-testid="stPopoverBody"] [data-testid="stFormSubmitButton"] button {
  color: #FFFFFF !important;
}
div[data-testid="stPopoverBody"] .stButton button p,
div[data-testid="stPopoverBody"] [data-testid="stFormSubmitButton"] button p {
  color: #FFFFFF !important;
}

@media (max-width: 640px) {
  .block-container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
}
</style>
"""

def inject_css():
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
