from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    blob_storage_connection_string: str
    blob_storage_container: str = "backups"
    psql_connection_string: PostgresDsn
    psql_database_name: Optional[str]
    retry_count: int = 3
    retry_delay: int = 5
    blob_storage_path_prefix: Optional[str]
    leader_election_enabled: bool = False
    redis_url: Optional[str]


settings = Settings()
