# (generated with --quick)

import logging
from typing import Any

Blob: Any
NotFound: Any
logger: logging.Logger
logging: module
storage: module

def read_gcloud_blob(bucket_id: str, gpath: str, fpath: str) -> bool: ...
def repo_list_gcloud_bucket(bucket_id: str, prefix = ...) -> list: ...
def write_gcloud_blob(bucket_id: str, gpath: str, fpath: str) -> None: ...
