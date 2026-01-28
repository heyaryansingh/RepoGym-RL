from radon.complexity import cc_visit
from radon.metrics import mi_visit
import statistics

def get_complexity_score(content: str) -> float:
    """
    Calculates the average cyclomatic complexity of the provided code content.
    Returns a score where lower is better, but we normalize it so that:
    - 1.0 is very simple (complexity <= 5)
    - 0.0 is very complex (complexity >= 50)
    """
    try:
        results = cc_visit(content)
        if not results:
            return 1.0 # Empty or no functions
        
        avg_complexity = statistics.mean([r.complexity for r in results])
        # Linear normalization: 1.0 at 5, 0.0 at 50
        score = max(0.0, min(1.0, 1.0 - (avg_complexity - 5) / 45))
        return score
    except Exception:
        return 0.0 # Parse error or other failure

def get_maintainability_score(content: str) -> float:
    """
    Calculates the maintainability index of the provided code content.
    Radon MI scale is roughly 0-100.
    100-20: high maintainability
    19-10: medium maintainability
    9-0: low maintainability
    """
    try:
        score = mi_visit(content, multi=False)
        # Normalize to 0.0-1.0
        return max(0.0, min(1.0, score / 100.0))
    except Exception:
        return 0.0
