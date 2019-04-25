# (generated with --quick)

import logging
from typing import Any, Optional, TypeVar

logger: logging.Logger
logging: module
os: module
re: module
redis: module
uuid: module

AnyStr = TypeVar('AnyStr', str, bytes)

class RedisLoader(object):
    _db: Any
    _main_q_key: bytes
    _session: str
    reference: int
    def __init__(self, name, **redis_kwargs) -> None: ...
    def _load_queue(self, data: list) -> None: ...
    def read_gcloud_repolist(self, bucket_id, prefix) -> None: ...
    def read_repolist(self, fpath) -> None: ...
    def sessionID(self) -> str: ...


def read_gcloud_blob(bucket_id: str, gpath: str, fpath: str) -> bool: ...
def repo_list_gcloud_bucket(bucket_id: str, prefix = ...) -> list: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
