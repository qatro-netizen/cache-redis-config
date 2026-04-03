interface RedisConfig {
  host: string;
  port: number;
  password?: string;
  db?: number;
  tls?: boolean;
}

interface CacheConfig {
  defaultTTL: number;
  maxKeys: number;
}

interface CacheRedisConfig {
  redis: RedisConfig;
  cache: CacheConfig;
}

export type { RedisConfig, CacheConfig, CacheRedisConfig };