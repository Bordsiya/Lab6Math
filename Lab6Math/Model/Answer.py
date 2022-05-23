from dataclasses import dataclass


@dataclass
class Answer:
    table: any
    headers: any
    ok: bool
    message: str
