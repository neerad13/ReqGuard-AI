from dataclasses import dataclass, field


@dataclass
class Requirement:

    req_id: str

    text: str

    req_type: str = "Unknown"

    ambiguity: list = field(default_factory=list)

    quality_score: int = 100

    rewritten_text: str = ""

    priority: str = "Unknown"