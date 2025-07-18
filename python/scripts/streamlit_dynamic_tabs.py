import streamlit as st
from modules.data_loader import load_data
from modules.simulation import run_monte_carlo
from modules.visualization import plot_forecast
from modules.metrics import summarize_forecast

data_dict = load_data()
st.sidebar.button("Run Simulation", on_click=lambda: st.session_state.update(run=True))

tabs = st.tabs(data_dict.keys())
for i, (category, actuals) in enumerate(data_dict.items()):
    with tabs[i]:
        # Inputs
        goal = st.number_input(f"{category} Goal", value=actuals.iloc[-1] * 1.5)
        mean_return = st.number_input(f"{category} Mean Monthly Return (%)", value=0.5)
        std_dev = st.number_input(f"{category} Volatility (%)", value=2.0)
        horizon = st.slider("Forecast Months", 6, 60, 24)

        # Run Sim + Show Output
        if st.session_state.get("run", False):
            forecast = run_monte_carlo(actuals.iloc[-1], mean_return, std_dev, horizon)
            plot_forecast(actuals, forecast, goal)
            stats = summarize_forecast(forecast, goal)
            for k, v in stats.items():
                st.metric(label=k, value=v)