# (generated with --quick)

import logging
import okra.error_handling
from typing import List, Optional, Type, TypeVar

DirectoryNotCreatedError: Type[okra.error_handling.DirectoryNotCreatedError]
MissingEnvironmentVariableError: Type[okra.error_handling.MissingEnvironmentVariableError]
NetworkError: Type[okra.error_handling.NetworkError]
csv: module
logger: logging.Logger
logging: module
os: module

AnyStr = TypeVar('AnyStr', str, bytes)

def create_parent_dir(repo_name: str, dirpath: str) -> bool: ...
def gcloud_clone_or_fetch_repo(repo_name: str) -> bool: ...
def local_persistance(repo_name: str, parent_dir: str, buffer_size = ...) -> None: ...
def okay_benice(qpath: str) -> None: ...
def parse_bigquery_csv(fpath: str) -> List[str]: ...
def populate_db(dburl: str, cache: str, repo_name: str, buffer_size = ...) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
