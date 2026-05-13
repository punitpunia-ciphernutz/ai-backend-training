import time
import logging
from functools import wraps

# setup logging once
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

logger = logging.getLogger(__name__)


def timer_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        try:
            result = func(*args, **kwargs)

            execution_time = round(time.time() - start, 4)

            logger.info({
                "function": func.__name__,
                "execution_time": execution_time,
                "status": "success"
            })

            return result

        except Exception as e:
            execution_time = round(time.time() - start, 4)

            logger.error({
                "function": func.__name__,
                "execution_time": execution_time,
                "status": "failed",
                "error": str(e)
            })

            raise

    return wrapper