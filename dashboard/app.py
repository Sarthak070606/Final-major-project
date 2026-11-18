from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from dashboard.views import (
    overview,
    map_page,
    station_explorer,
    historical_recent,
    quarterly,
    prediction,
    well_suitability,
    data_quality,
    model_performance,
    about,
    location_search,
)

from dashboard.utils.styles import inject_css
from dashboard.utils import config as cfg
from dashboard.utils.floating_chatbot import render_floating_chatbot




st.set_page_config(
    page_title=cfg.APP_TITLE,
    page_icon=cfg.PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)



inject_css()

st.markdown(
    """
    <style>

    /* Fix top heading clipping */
    [data-testid="stMainBlockContainer"] {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        overflow: visible !important;
    }

    /* Page title */
    .page-title {
        display: block !important;
        width: 100% !important;
        font-size: 30px !important;
        font-weight: 750 !important;
        line-height: 1.5 !important;
        color: #123b55 !important;
        padding: 8px 0 !important;
        margin: 0 0 8px 0 !important;
        overflow: visible !important;
        box-sizing: border-box !important;
    }

    /* Page subtitle */
    .page-subtitle {
        display: block !important;
        font-size: 16px !important;
        line-height: 1.6 !important;
        color: #526f83 !important;
        margin-bottom: 20px !important;
        overflow: visible !important;
    }

    /* Improve metric visibility */
    [data-testid="stMetricValue"] {
        font-size: clamp(20px, 2vw, 32px) !important;
        line-height: 1.4 !important;
        overflow-wrap: anywhere !important;
    }

    [data-testid="stMetricLabel"] {
        font-size: 14px !important;
        white-space: normal !important;
    }

    /* Sidebar text */
    [data-testid="stSidebar"] {
        overflow-y: auto !important;
    }

    [data-testid="stSidebar"] p {
        line-height: 1.5 !important;
    }

    /* Section separators */
    hr {
        border: none !important;
        height: 1px !important;
        background: #cbdde5 !important;
        margin: 25px 0 !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)




PAGES = {
    "🏠  Overview": overview,
    "🗺️  Groundwater Map": map_page,
    "📍  Location Search": location_search,
    "📡  Station Explorer": station_explorer,
    "📈  Historical vs Recent": historical_recent,
    "📅  Quarterly Analysis": quarterly,
    "🤖  AI Prediction": prediction,
    "💧  Well Suitability": well_suitability,
    "🛡️  Data Quality": data_quality,
    "🎯  Model Performance": model_performance,
    "ℹ️  About Project": about,
}


with st.sidebar:

    st.markdown(
        f"# {cfg.PAGE_ICON} MP Groundwater"
    )

    st.caption(
        "INTELLIGENCE & MONITORING PLATFORM"
    )

    st.markdown("---")

    choice = st.radio(
        "NAVIGATION",
        list(PAGES.keys()),
        label_visibility="visible",
    )

    st.markdown("---")

    st.caption("Data source: CGWB telemetry")

    st.caption(
        "Academic decision-support system"
    )

    st.caption(
        "Not a substitute for field investigation"
    )



PAGES[choice].render()



render_floating_chatbot()




st.markdown(
    """
    <div class="footer">
        MP Groundwater Intelligence · B.Tech Major Project ·
        CGWB telemetry · For research and decision support only
    </div>
    """,
    unsafe_allow_html=True,
)
