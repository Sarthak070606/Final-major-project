
from __future__ import annotations

import streamlit as st
import pandas as pd
import plotly.express as px

from dashboard.utils import data_loader as dl


def render():

    # -------------------------------------------------
    # PAGE HEADER
    # -------------------------------------------------

    st.markdown(
        '<div class="page-title">Madhya Pradesh Groundwater Map</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Interactive CGWB monitoring station locations'
        '</div>',
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # LOAD DATA
    # -------------------------------------------------

    try:
        latest = dl.load_latest_readings()
        stations = dl.load_stations_master()

    except Exception as e:
        st.error(f"Error loading groundwater data: {e}")
        return

    df = None

    if (
        latest is not None
        and not latest.empty
        and {"latitude", "longitude"}.issubset(latest.columns)
    ):
        df = latest.copy()

    elif (
        stations is not None
        and not stations.empty
        and {"latitude", "longitude"}.issubset(stations.columns)
    ):
        df = stations.copy()

    if df is None or df.empty:
        st.warning("Station coordinate data is unavailable.")
        return

    # -------------------------------------------------
    # CLEAN COORDINATES
    # -------------------------------------------------

    df["latitude"] = pd.to_numeric(
        df["latitude"], errors="coerce"
    )

    df["longitude"] = pd.to_numeric(
        df["longitude"], errors="coerce"
    )

    df = df.dropna(
        subset=["latitude", "longitude"]
    )

    # Madhya Pradesh geographical boundary filter
    df = df[
        df["latitude"].between(21.0, 27.0)
        & df["longitude"].between(74.0, 83.0)
    ].copy()

    if df.empty:
        st.warning(
            "No valid Madhya Pradesh station coordinates found."
        )
        return

    # -------------------------------------------------
    # DISTRICT FILTER
    # -------------------------------------------------

    if "district" in df.columns:

        districts = sorted(
            df["district"].dropna().astype(str).unique().tolist()
        )

        selected = st.multiselect(
            "Filter by district",
            districts,
            default=districts
        )

        if selected:
            df = df[
                df["district"].astype(str).isin(selected)
            ].copy()

        else:
            st.info(
                "Select at least one district to display stations."
            )
            return

    # -------------------------------------------------
    # GROUNDWATER LEVEL COLOR
    # -------------------------------------------------

    color_col = None

    if "wl_raw" in df.columns:

        df["wl_raw"] = pd.to_numeric(
            df["wl_raw"], errors="coerce"
        )

        if df["wl_raw"].notna().any():
            color_col = "wl_raw"

    # -------------------------------------------------
    # HOVER INFORMATION
    # -------------------------------------------------

    hover_cols = [
        col for col in [
            "station",
            "district",
            "wl_raw",
            "datetime"
        ]
        if col in df.columns
    ]

    # -------------------------------------------------
    # MAP CREATION
    # -------------------------------------------------

    try:

        map_data = df.dropna(
            subset=["latitude", "longitude"]
        ).copy()

        if hasattr(px, "scatter_map"):

            fig = px.scatter_map(
                map_data,
                lat="latitude",
                lon="longitude",
                color=color_col,
                hover_name=(
                    "station"
                    if "station" in map_data.columns
                    else None
                ),
                hover_data=hover_cols,
                color_continuous_scale=(
                    "RdYlBu_r" if color_col else None
                ),
                zoom=5.2,
                height=620,
                map_style="open-street-map",
                center={
                    "lat": 23.5,
                    "lon": 78.5
                },
                title=(
                    "CGWB Groundwater Monitoring Stations "
                    "– Madhya Pradesh"
                )
            )

        elif hasattr(px, "scatter_mapbox"):

            fig = px.scatter_mapbox(
                map_data,
                lat="latitude",
                lon="longitude",
                color=color_col,
                hover_name=(
                    "station"
                    if "station" in map_data.columns
                    else None
                ),
                hover_data=hover_cols,
                color_continuous_scale=(
                    "RdYlBu_r" if color_col else None
                ),
                zoom=5.2,
                height=620,
                mapbox_style="open-street-map",
                center={
                    "lat": 23.5,
                    "lon": 78.5
                },
                title=(
                    "CGWB Groundwater Monitoring Stations "
                    "– Madhya Pradesh"
                )
            )

        else:
            st.error(
                "Your Plotly version does not support map charts. "
                "Please upgrade Plotly."
            )
            return

    except Exception as e:

        st.error(
            f"Unable to generate groundwater map: {e}"
        )
        return

    # -------------------------------------------------
    # MAP MARKER STYLING
    # -------------------------------------------------

    fig.update_traces(
        marker={
            "size": 9,
            "opacity": 0.85
        }
    )

    # -------------------------------------------------
    # MAP LAYOUT
    # -------------------------------------------------

    fig.update_layout(
        margin={
            "l": 0,
            "r": 0,
            "t": 45,
            "b": 0
        },
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#183247",
        coloraxis_colorbar_title="Groundwater level (m)"
    )

    # -------------------------------------------------
    # DISPLAY MAP
    # -------------------------------------------------

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "scrollZoom": True,
            "displayModeBar": True
        }
    )

    # -------------------------------------------------
    # STATION STATISTICS
    # -------------------------------------------------

    st.caption(
        f"Displaying {len(df):,} stations with valid coordinates. "
        "Map background: OpenStreetMap."
    )

    # -------------------------------------------------
    # STATION RECORDS
    # -------------------------------------------------

    with st.expander("View station records"):

        show_cols = [
            col for col in [
                "station",
                "district",
                "latitude",
                "longitude",
                "wl_raw",
                "datetime"
            ]
            if col in df.columns
        ]

        st.dataframe(
            df[show_cols].reset_index(drop=True),
            use_container_width=True
        )
