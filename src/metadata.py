# Function that adds meta data
from datetime import datetime
import subprocess
def get_metadata(seed=None, model=None):
    """
    dict with metadata for plots and dataframes
    """
    if seed is None:
        seed = 42
    date = datetime.now().isoformat(timespec="seconds")

    try:
        git_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).decode().strip()
    except Exception:
        git_commit = "unknown"

    return {
        "seed": seed,
        "date": date,
        "git_commit": git_commit,
        "model": model,
    }