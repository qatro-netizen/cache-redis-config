import argparse
import logging
import yaml

from cache_redis_config.config import RedisConfig
from cache_redis_config.utils import get_logger

# Set up logging
logger = get_logger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description='Cache Redis Config')
    parser.add_argument('--config', help='Config file path')
    return parser.parse_args()

def main():
    args = parse_args()
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    redis_config = RedisConfig(**config)
    logger.info(f'Loaded Redis config: {redis_config.to_dict()}')

if __name__ == '__main__':
    main()