import logging

def setup_logger():
    """Set up a logger for system diagnostics."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s]: %(message)s",
        handlers=[logging.StreamHandler()],
    )
    return logging.getLogger("metarobot")
