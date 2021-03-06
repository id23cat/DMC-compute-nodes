from typing import Callable, Optional
from logging import Logger
import logs.logs as logs

get_logger: Callable[[Optional[str]], Logger] = getattr(logs, logs.get_logger_name_func)
