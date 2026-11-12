"""practice_api.py: a small local API that behaves like real ones on a bad day.
Run: python practice_api.py (serves on http://127.0.0.1:5050)
"""
import logging

import time
from flask import Flask, request, jsonify

logging.getLogger("werkzeug").setLevel(logging.ERROR) # keep the request log quiet

practice = Flask("practice_api")

COURSES = [{"id": i, "title": t} for i, t in enumerate([
"Python Basics", "Git & GitHub", "SQL Foundations", "HTTP & APIs", "Flask", "Testing",
"Docker", "Cloud Basics", "LLM Fundamentals", "RAG", "Agents", "Client Delivery"], start=1)]

_flaky = {"calls": 0}
_hits = [] # request times, for the rate limiter

@practice.route("/hello")
def hello():
    return jsonify(message="Hello from the kitchen!", served_by="practice_api")


@practice.route("/echo", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def echo(): # tells you exactly what it received
    return jsonify(method=request.method, path=request.path, query=request.args.to_dict(),
content_type=request.headers.get("Content-Type"),
api_key=request.headers.get("X-API-KEY"), body=request.get_json(silent=True))

@practice.route("/status/<int:code>")
def status(code): # answers with whatever status you ask for
    return jsonify(you_asked_for=code), code

@practice.route("/slow")
def slow(): # /slow?seconds=2 waits before answering
    time.sleep(float(request.args.get("seconds", 2)))
    return jsonify(message="Sorry, the kitchen was busy")

@practice.route("/secure")
def secure(): # needs the header X-API-KEY: abc123def   
    if request.headers.get("X-API-KEY") != "abc123def":
        return jsonify(error="unauthorized", message="Missing or wrong X-API-KEY header"), 401
    return jsonify(secret="Only for key holders")


@practice.route("/flaky")
def flaky(): # fails twice with 503, then works
    _flaky["calls"] += 1
    if _flaky["calls"] < 3:
        return jsonify(error="unavailable", message="Try again shortly"), 503
    attempts, _flaky["calls"] = _flaky["calls"], 0
    return jsonify(message=f"Worked on attempt {attempts}")


@practice.route("/courses")
def courses(): # paginated list: ?page=1&limit=5
    page = request.args.get("page", 1, type=int)
    limit = request.args.get("limit", 5, type=int)
    if page < 1 or not 1 <= limit <= 10:
        return jsonify(error="bad_request", message="Need page >= 1 and 1 <= limit <= 10"), 400
    start = (page - 1) * limit
    has_more = start + limit < len(COURSES) 
    return jsonify(items=COURSES[start:start + limit], page=page, limit=limit, total=len(COURSES), next_page=page + 1 if has_more else None)


@practice.route("/limited")
def limited(): # at most 3 requests per second
    now = time.monotonic()
    _hits[:] = [t for t in _hits if now - t < 1.0]
    if len(_hits) >= 3:
        return (jsonify(error="rate_limited", message="Max 3 requests per second"), 429, {"Retry-After": "1"})
    _hits.append(now)
    return jsonify(ok=True, used_this_second=len(_hits), limit=3)



# Q6
def fetch_json(url, params=None, api_key=None, timeout=5):
    headers = {}

    if api_key:
        headers["X-API-KEY"] = api_key

    response = request.get(
        url,
        params,
        headers,
        timeout
    )

    response.raise_for_status()

    return response.json()


# Q7
def get_all(url, limit=20, max_pages=50):
    all_items = []
    page = 1
    visited_page = set()

    while page is not None and len(visited_page) < max_pages:

        if page in visited_page:
            break

        visited_page.add(page)

        response = request.get(
            url,
            params={
                "page":page,
                "limit":limit
            },
            timeout = 5
        )

        response.raise_for_status()
        data = response.json()

        all_items.extend(data.get("items", []))

        next_page = data.get("next_page")

        if next_page is None:
            break

        page = next_page

    return all_items




# Q8
def get_with_backoff(url, attempts=5):
    retry_status_codes = {429, 500, 502, 503, 504}

    for attempt in range(attempts):
        try:
            response = request.get(url, timeout=5)

            # Return immediately for non-retryable responses
            if response.status_code not in retry_status_codes:
                return response

            # Last attempt: don't wait again
            if attempt == attempts - 1:
                return response

            # Respect Retry-After if present
            retry_after = response.headers.get("Retry-After")

            if retry_after is not None:
                wait_time = float(retry_after)
            else:
                wait_time = 0.5 * (2 ** attempt)

        except (request.ConnectionError, request.Timeout):

            # Don't retry after the final attempt
            if attempt == attempts - 1:
                raise

            wait_time = 0.5 * (2 ** attempt)

        time.sleep(wait_time)


import json

# Step 1: Create a Python dictionary
learner = {
    "mentor": None,
    "active": True,
    "skills": ("Python", "SQL"),
    "name": "प्रि या "
}

# Step 2: Save dictionary to JSON file
with open("learner.json", "w", encoding="utf-8") as file:
    json.dump(learner, file, indent=2, ensure_ascii=False)

# Step 3: Read JSON file back
with open("learner.json", "r", encoding="utf-8") as file:
    learner_data = json.load(file)

# Step 4: Compare original and loaded data types
for key in learner:
    original_type = type(learner[key]).__name__
    loaded_type = type(learner_data[key]).__name__

    if original_type != loaded_type:
        print(f"{key}: {original_type} -> {loaded_type}")

print("\nLoaded data:")
print(learner_data)

# Only the tuple changes type into a list. JSON does not support Python tuples as a native data type. 


if __name__ == "__main__":
    practice.run(host="127.0.0.1", port=5050, threaded=True)



