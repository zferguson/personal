import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


def plot_forecast(actuals: pd.Series, forecast: np.ndarray, goal: float = None):
    months = forecast.shape[1]
    future_dates = pd.date_range(actuals.index[-1] + pd.DateOffset(months=1), periods=months, freq="M")

    median = np.percentile(forecast, 50, axis=0)
    lower = np.percentile(forecast, 25, axis=0)
    upper = np.percentile(forecast, 75, axis=0)

    # Build forecast traces
    fig = go.Figure()

    # Historical actuals
    fig.add_trace(go.Scatter(
        x=actuals.index, y=actuals.values,
        mode="lines", name="Historical Actuals", line=dict(color="black", width=2)
    ))

    # Forecast median
    fig.add_trace(go.Scatter(
        x=future_dates, y=median,
        mode="lines", name="Median Forecast", line=dict(color="blue")
    ))

    # Percentile range as shaded area
    fig.add_trace(go.Scatter(
        x=np.concatenate([future_dates, future_dates[::-1]]),
        y=np.concatenate([upper, lower[::-1]]),
        fill='toself',
        fillcolor='rgba(0, 0, 255, 0.1)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=True,
        name="25–75% Forecast Range"
    ))

    # Goal line
    if goal is not None:
        fig.add_trace(go.Scatter(
            x=[actuals.index[0], future_dates[-1]],
            y=[goal, goal],
            mode="lines",
            name="Goal",
            line=dict(color="orange", dash="dash")
        ))

    fig.update_layout(
        title="Monte Carlo Forecast",
        xaxis_title="Date",
        yaxis_title="Asset Value",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_final_histogram(forecast: np.ndarray, goal: float = None):
    final_values = forecast[:, -1]
    fig = px.histogram(
        final_values,
        nbins=50,
        title="Distribution of Final Forecast Values",
        labels={"value": "Final Value"},
        template="plotly_white"
    )

    # Add goal line
    if goal is not None:
        fig.add_vline(
            x=goal,
            line_dash="dash",
            line_color="orange",
            annotation_text="Goal",
            annotation_position="top right"
        )

    st.plotly_chart(fig, use_container_width=True)