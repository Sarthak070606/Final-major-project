
    # Create groundwater monitoring station map
    try:
        if hasattr(px, "scatter_map"):
            fig = px.scatter_map(
                df,
                lat="latitude",
                lon="longitude",
                color=color_col,
                hover_name="station" if "station" in df.columns else None,
                hover_data=hover_cols,
                color_continuous_scale="RdYlBu_r" if color_col else None,
                zoom=5.2,
                height=620,
                map_style="open-street-map",
                center={"lat": 23.5, "lon": 78.5},
                title="CGWB Groundwater Monitoring Stations – Madhya Pradesh"
            )

        elif hasattr(px, "scatter_mapbox"):
            fig = px.scatter_mapbox(
                df,
                lat="latitude",
                lon="longitude",
                color=color_col,
                hover_name="station" if "station" in df.columns else None,
                hover_data=hover_cols,
                color_continuous_scale="RdYlBu_r" if color_col else None,
                zoom=5.2,
                height=620,
                mapbox_style="open-street-map",
                center={"lat": 23.5, "lon": 78.5},
                title="CGWB Groundwater Monitoring Stations – Madhya Pradesh"
            )

        else:
            st.error(
                "Your Plotly installation does not support map charts. "
                "Please upgrade Plotly."
            )
            return

    except Exception as e:
        st.error(f"Unable to generate groundwater map: {e}")
        return

    fig.update_traces(
        marker={"size": 9, "opacity": 0.85}
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=45, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#183247",
        coloraxis_colorbar_title="Groundwater level (m)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "scrollZoom": True,
            "displayModeBar": True
        }
    )
