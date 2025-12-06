from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class APIv1Prefix(BaseModel):
    prefix: str
    user: str

class APIPrefix(BaseModel):
    prefix: str
    v1: APIv1Prefix

class AppRun(BaseModel):
    port: int
    host: str

class DBHelper(BaseModel):
    echo: bool
    echo_pool: bool
    pool_size: int
    max_overflow: int

class DataBase(BaseModel):
    user: str
    password: str
    host: str
    port: int
    name: str
    
    helper: DBHelper
    
    naming_convention: dict = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", '.env'),
        env_nested_delimiter='__',
        env_prefix='CONFIG__'
        )
    
    app_run: AppRun
    db: DataBase
    api: APIPrefix
    
    @property
    def DATABASE_URL_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.db.user}:{self.db.password}@{self.db.host}:{self.db.port}/{self.db.name}"
    
    @property
    def DATABASE_URL_psycopg(self) -> str:
        return f"postgresql+psycopg://{self.db.user}:{self.db.password}@{self.db.host}:{self.db.port}/{self.db.name}"

settings = Settings()