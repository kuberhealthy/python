# Python Kuberhealthy Client

This repository provides a small Python library for reporting check results back to [Kuberhealthy](https://github.com/kuberhealthy/kuberhealthy). It also includes a runnable example program and container configuration.

## Installing

Install the client into your own project:

```bash
pip install kuberhealthy-client
```

The library exposes two helpers:

```python
from kuberhealthy_client import report_ok, report_error

# Environment variables KH_REPORTING_URL and KH_RUN_UUID are read automatically.
report_ok()
report_error("something went wrong")
```

Both functions accept optional `url` and `run_uuid` keyword arguments if you prefer to supply values directly.

## Running the example

Set the `KH_REPORTING_URL` and `KH_RUN_UUID` environment variables, add your
check logic to `client.py`, and then run:

```bash
python3 client.py
```

Within the `main` function, uncomment either `report_ok()` or
`report_error("message")` after your logic depending on the result.

## Building and pushing the check

Use the provided `Makefile` and `Dockerfile` to build and publish the check
image.

```bash
make build IMG=myrepo/example-check:latest
make push IMG=myrepo/example-check:latest
```

## Using in your own checks

1. Add your check logic to `client.py` or your own script. Call `report_ok()`
   when the check succeeds or `report_error("message")` when it fails.
2. Build and push your image as shown above.
3. Create a `KuberhealthyCheck` resource pointing at your image and apply it to any
   cluster where Kuberhealthy runs:

```yaml
apiVersion: kuberhealthy.github.io/v2
kind: KuberhealthyCheck
metadata:
  name: example-python-check
spec:
  image: myrepo/example-check:latest
  runInterval: 1m
```
