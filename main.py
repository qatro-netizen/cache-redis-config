import os
from typing import Dict, List
from pydantic import BaseModel
from redis import Redis

class Config(BaseModel):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

class CacheConfig:
    def __init__(self, config: Config):
        self.redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB)

    def get(self, key: str) -> str:
        return self.redis.get(key).decode('utf-8')

    def set(self, key: str, value: str) -> None:
        self.redis.set(key, value)

    def delete(self, key: str) -> None:
        self.redis.delete(key)

def load_config() -> Config:
    config_file = os.getenv('CACHE_CONFIG_FILE', 'config.yaml')
    return Config.parse_file(config_file)

def main() -> None:
    config = load_config()
    cache_config = CacheConfig(config)
    print(cache_config.get('test_key'))

if __name__ == '__main__':
    main()