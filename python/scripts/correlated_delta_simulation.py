import numpy as np
import pandas as pd

def run_correlated_delta_simulation(
    historical_assets: pd.DataFrame,
    n_months: int = 24,
    n_sims: int = 1000
):
    """
    Run correlated delta simulation on asset values by category.

    Returns:
    - results: dict with keys:
        - "actuals": original historical DataFrame
        - "future_dates": pd.DatetimeIndex
        - "simulations": {category: np.ndarray of shape (n_sims, n_months)}
        - "percentiles": {category: dict of median/25/75th (length n_months)}
        - "final_values": {category: np.ndarray of length n_sims}
    """
    categories = historical_assets.columns.tolist()
    deltas = historical_assets.diff().dropna()
    mu = deltas.mean().values
    cov = deltas.cov().values
    last_known = historical_assets.iloc[-1].values

    simulations = {cat: np.zeros((n_sims, n_months)) for cat in categories}

    # Run simulations
    for sim in range(n_sims):
        sim_deltas = np.random.multivariate_normal(mu, cov, size=n_months)
        sim_path = np.cumsum(sim_deltas, axis=0) + last_known
        for i, cat in enumerate(categories):
            simulations[cat][sim, :] = sim_path[:, i]

    # Calculate percentiles
    percentiles = {}
    final_values = {}
    for i, cat in enumerate(categories):
        cat_sims = simulations[cat]
        percentiles[cat] = {
            "median": np.median(cat_sims, axis=0),
            "p25": np.percentile(cat_sims, 25, axis=0),
            "p75": np.percentile(cat_sims, 75, axis=0),
        }
        final_values[cat] = cat_sims[:, -1]  # last month

    # Future date range
    last_date = historical_assets.index[-1]
    future_dates = pd.date_range(last_date + pd.DateOffset(months=1), periods=n_months, freq='M')

    return {
        "actuals": historical_assets,
        "future_dates": future_dates,
        "simulations": simulations,
        "percentiles": percentiles,
        "final_values": final_values
    }