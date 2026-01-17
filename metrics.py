import time
import logging
from contextlib import contextmanager

logger = logging.getLogger("metrics")

@contextmanager
def timer(name):
    """Context manager to log the duration of a block of code."""
    start_time = time.perf_counter()
    try:
        yield
    finally:
        end_time = time.perf_counter()
        duration = end_time - start_time
        logger.info(f"Metric: {name} took {duration:.4f}s")
