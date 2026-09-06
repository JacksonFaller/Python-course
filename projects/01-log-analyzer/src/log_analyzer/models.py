from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class LogEntry:
    timestamp: datetime
    method: str
    path: str
    status: int
    duration_ms: int
