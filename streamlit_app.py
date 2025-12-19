    fig = px.line(
        df_season_drivers,
        x="round",
        y="points",
        color="driverRef",
        labels={"driverRef": "driver", "name": "Grand Prix"},
        category_orders={"driverRef": list_order_points},
    )
    st.plotly_chart(fig, use_container_width=True)

