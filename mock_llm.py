# src/mock_llm.py
"""
A tiny mock LLM to show the pipeline without real API keys.
It creates:
- initial answer + short assumptions
- evaluates assumptions against snippets (rudimentary)
- synthesizes a final verdict
This is for learning/testing only.
"""

def initial_and_assumptions(claim: str):
    claim = claim.strip()
    assumptions = []
    answer = "Uncertain"

    # Very simple heuristics:
    if " is " in claim.lower() or " are " in claim.lower():
        # split on first ' is ' or ' are '
        if " is " in claim.lower():
            subject, predicate = claim.split(" is ", 1)
        else:
            subject, predicate = claim.split(" are ", 1)
        subject = subject.strip().strip(".")
        predicate = predicate.strip().strip(".")
        assumptions.append(f"{subject} exists")
        assumptions.append(f"{subject} has the property '{predicate}'")
        # extra heuristic for capitals
        if "capital" in predicate.lower() or "capital of" in predicate.lower():
            answer = "True"  # guess for common pattern
        else:
            answer = "Uncertain"
    else:
        # fallback: treat whole claim as single assumption
        assumptions = [claim]
        answer = "Uncertain"

    return {"answer": answer, "assumptions": assumptions}


def evaluate_assumption(assumption: str, snippets: list):
    """
    Check if any snippet contains words from the assumption.
    Returns a simple verdict and confidence.
    """
    a_words = [w.lower().strip(".,'\"") for w in assumption.split() if len(w) > 2]
    found = 0
    for s in snippets:
        s_low = s.lower()
        if any(w in s_low for w in a_words):
            found += 1

    if found >= 2:
        return {"verdict": "supports", "confidence": 80}
    elif found == 1:
        return {"verdict": "supports", "confidence": 55}
    else:
        return {"verdict": "uncertain", "confidence": 30}


def final_synthesis(initial_answer: str, assumption_results: list):
    """
    Combine assumption results into a final label.
    Very simple scoring: supports +1, contradicts -1, uncertain 0.
    """
    score = 0
    for r in assumption_results:
        v = r.get("eval", {}).get("verdict", "uncertain")
        if v == "supports":
            score += 1
        elif v == "contradicts":
            score -= 1

    if score > 0:
        label = "Likely True"
    elif score < 0:
        label = "Likely False"
    else:
        label = "Unverifiable"

    # Make a simple confidence number
    confidence = 50 + (10 * score)
    confidence = max(10, min(95, confidence))

    explanation = f"Based on {len(assumption_results)} checks the result is '{label}'."
    return {"label": label, "confidence": confidence, "explanation": explanation}
