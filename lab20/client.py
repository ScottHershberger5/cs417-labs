"""Lab 20: Build the Other Side — Client

Client functions that talk to your FastAPI server. Each task adds
a new function that handles a more realistic scenario.
"""

import requests
import time


def submit(student: str, lab: int, base_url: str = "http://localhost:8000") -> dict:
    """Task 1: Submit a grading request and return the result.

    POST to {base_url}/grade with {"student": student, "lab": lab}.
    Raise RuntimeError if the status code is not 200.
    Return the response as a dictionary.
    """
    # TODO: Implement
    payload = {"student": student, "lab": lab}
    url = f"{base_url}/grade"
    response = requests.post(url, json = payload)

    if response.status_code != 200:
        raise RuntimeError(f"Request failed with status code {response.status_code}")

    return response.json()
    


def submit_with_retry(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    timeout: float = 2,
    max_retries: int = 3,
) -> dict:
    """Task 2: Submit with timeout and retry logic.

    POST to /grade with {"student": student, "lab": lab, "slow": True}.
    Use the timeout parameter in requests.post().
    On requests.exceptions.Timeout, retry up to max_retries times.
    Raise RuntimeError("all retries failed") if every attempt times out.
    Return the response dictionary on success.
    """
    # TODO: Implement
    url = f"{base_url}/grade"
    payload = {"student": student, "lab": lab, "slow": True}

    for _ in range(max_retries):
        try:
            response = requests.post(url, json=payload, timeout=timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            continue

    raise RuntimeError("all retries failed")
    


def submit_idempotent(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    timeout: float = 2,
    max_retries: int = 3,
) -> dict:
    """Task 3: Submit with an idempotency key.

    Same as submit_with_retry, but include a stable submission_id
    in the request body: f"{student}-lab{lab}"
    """
    # TODO: Implement
    
    url = f"{base_url}/grade"
    submission_id = f"{student}-lab{lab}"
    payload = {
        "student": student,
        "lab": lab,
        "slow": True,
        "submission_id": submission_id
    }

    for _ in range(max_retries):
        try:
            response = requests.post(url, json=payload, timeout=timeout)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            continue

    raise RuntimeError("all retries failed")


def submit_async(
    student: str,
    lab: int,
    base_url: str = "http://localhost:8000",
    poll_interval: float = 0.5,
    max_polls: int = 20,
) -> dict:
    """Task 4: Async submission with polling.

    POST to /grade-async with student, lab, and a stable submission_id.
    Expect a 202 response with a job_id.
    Poll GET /grade-jobs/{job_id} every poll_interval seconds.
    When status is "complete", return the result dictionary.
    Raise RuntimeError("polling timed out") if max_polls is exceeded.
    """
    # TODO: Implement
    submission_id = f"{student}-lab{lab}"

    url = f"{base_url}/grade-async"
    payload = {
        "student": student,
        "lab": lab,
        "submission_id": submission_id
    }

    response = requests.post(url, json=payload)

    if response.status_code != 202:
        raise RuntimeError("expected 202 Accepted")

    job_id = response.json()["job_id"]

    poll_url = f"{base_url}/grade-jobs/{job_id}"

    for _ in range(max_polls):
        time.sleep(poll_interval)

        r = requests.get(poll_url)

        if r.status_code == 404:
            raise RuntimeError("job not found")

        data = r.json()

        if data["status"] == "complete":
            return data["result"]

    raise RuntimeError("polling timed out")


# ---------------------------------------------------------------------------
# Bonus Task 5: The Smart Client
# ---------------------------------------------------------------------------


class SmartClient:
    """A client that tries sync first, then falls back to async."""

    def __init__(self, base_url: str = "http://localhost:8000", timeout: float = 2):
        self.base_url = base_url
        self.timeout = timeout

    def submit(self, student: str, lab: int) -> dict:
        submission_id = f"{student}-lab{lab}"

        # -------------------------
        # 1. Try synchronous path
        # -------------------------
        sync_url = f"{self.base_url}/grade"
        payload = {
            "student": student,
            "lab": lab,
            "submission_id": submission_id
        }

        try:
            response = requests.post(sync_url, json=payload, timeout=self.timeout)

            if response.status_code == 200:
                return response.json()

        except requests.exceptions.Timeout:
            # fall through to async
            pass

        # -------------------------
        # 2. Fallback to async
        # -------------------------
        async_url = f"{self.base_url}/grade-async"

        response = requests.post(async_url, json=payload)

        if response.status_code != 202:
            raise RuntimeError("async request failed")

        job_id = response.json()["job_id"]

        poll_url = f"{self.base_url}/grade-jobs/{job_id}"

        # -------------------------
        # 3. Poll until complete
        # -------------------------
        for _ in range(20):
            time.sleep(0.5)

            r = requests.get(poll_url)

            if r.status_code == 404:
                raise RuntimeError("job not found")

            data = r.json()

            if data["status"] == "complete":
                return data["result"]

        raise RuntimeError("polling timed out")
