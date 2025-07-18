import numpy as np
import pandas as pd

def run_correlated_delta_simulation(
    historical_assets: pd.DataFrame,
    n_months: int = 24,
    n_sims: int = 1000,
    subtotal_categories: list = None,
):
    """
    Run correlated delta simulation on asset values by category.

    Returns:
    - results: dict with keys:
        - "actuals": historical asset values (DataFrame)
        - "future_dates": pd.DatetimeIndex
        - "simulations": {category: (n_sims, n_months)}
        - "percentiles": {category: {median, p25, p75} arrays}
        - "final_values": {category: (n_sims,) array}
        - "total": dict with median, p25, p75, final_values
        - "total_actuals": Series of summed actuals across all categories
        - "subtotal": same structure for subtotal group (if provided)
        - "subtotal_actuals": Series of summed actuals for subset (if provided)
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

    # Per-category stats
    percentiles = {}
    final_values = {}
    for cat in categories:
        sims = simulations[cat]
        percentiles[cat] = {
            "median": np.median(sims, axis=0),
            "p25": np.percentile(sims, 25, axis=0),
            "p75": np.percentile(sims, 75, axis=0),
        }
        final_values[cat] = sims[:, -1]

    # Aggregate helpers
    def compute_aggregate(cats):
        combined = sum(simulations[cat] for cat in cats)
        return {
            "median": np.median(combined, axis=0),
            "p25": np.percentile(combined, 25, axis=0),
            "p75": np.percentile(combined, 75, axis=0),
            "final_values": combined[:, -1]
        }

    # Total across all categories
    total = compute_aggregate(categories)
    total_actuals = historical_assets.sum(axis=1)

    # Optional subtotal
    subtotal = None
    subtotal_actuals = None
    if subtotal_categories:
        missing = [cat for cat in subtotal_categories if cat not in categories]
        if missing:
            raise ValueError(f"Subtotal categories not found: {missing}")
        subtotal = compute_aggregate(subtotal_categories)
        subtotal_actuals = historical_assets[subtotal_categories].sum(axis=1)

    future_dates = pd.date_range(
        historical_assets.index[-1] + pd.DateOffset(months=1),
        periods=n_months,
        freq="M"
    )

    return {
        "actuals": historical_assets,
        "future_dates": future_dates,
        "simulations": simulations,
        "percentiles": percentiles,
        "final_values": final_values,
        "total": total,
        "total_actuals": total_actuals,
        "subtotal": subtotal,
        "subtotal_actuals": subtotal_actuals,
    }