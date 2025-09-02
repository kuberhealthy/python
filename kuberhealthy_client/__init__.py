"""Lightweight client for reporting check results to Kuberhealthy."""

from __future__ import annotations

import json
import os
import urllib.request
from typing import Optional

KH_REPORTING_URL = "KH_REPORTING_URL"
KH_RUN_UUID = "KH_RUN_UUID"

def _get_env(name: str) -> str:
    """Return the value of the environment variable *name* or raise an error."""
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"{name} must be set")
    return value

def _post_status(payload: dict, *, url: Optional[str] = None, run_uuid: Optional[str] = None) -> None:
    """Send *payload* to the Kuberhealthy reporting URL."""
    url = url or _get_env(KH_REPORTING_URL)
    run_uuid = run_uuid or _get_env(KH_RUN_UUID)
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"content-type": "application/json", "kh-run-uuid": run_uuid},
    )
    with urllib.request.urlopen(request, timeout=10) as response:  # nosec B310
        response.read()

def report_ok(*, url: Optional[str] = None, run_uuid: Optional[str] = None) -> None:
    """Report a successful check to Kuberhealthy."""
    _post_status({"OK": True, "Errors": []}, url=url, run_uuid=run_uuid)

def report_error(message: str, *, url: Optional[str] = None, run_uuid: Optional[str] = None) -> None:
    """Report a failure to Kuberhealthy with *message* as the error."""
    _post_status({"OK": False, "Errors": [message]}, url=url, run_uuid=run_uuid)

__all__ = ["report_ok", "report_error", "KH_REPORTING_URL", "KH_RUN_UUID"]
