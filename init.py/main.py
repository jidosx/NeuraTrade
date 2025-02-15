from neuratrade.data.loaders import load_data
from neuratrade.utils.helpers import get_current_time
from neuratrade.utils.logger import log_info

if __name__ == "__main__":
    data = load_data("path/to/your/data.csv")
    log_info(f"Data loaded at {get_current_time()}")
    # TO DO: Implement main logic
