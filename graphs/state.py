from typing import TypedDict, Dict, List


class ChurnState(TypedDict):
    customer_data: Dict

    prediction: str
    confidence: float

    explanation: List[str]

    priority: str

    strategy: List[str]