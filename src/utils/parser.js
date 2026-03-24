const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

class ConfigParser {
    constructor(configPath) {
        this.configPath = path.resolve(configPath);
        this.config = null;
    }

    load() {
        try {
            const fileContent = fs.readFileSync(this.configPath, 'utf8');
            this.config = yaml.load(fileContent);
        } catch (error) {
            throw new Error(`Failed to load config file: ${error.message}`);
        }
    }

    getRedisConfig() {
        if (!this.config || !this.config.redis) {
            throw new Error('Redis configuration is missing in the config file.');
        }
        return this.config.redis;
    }

    validateRedisConfig() {
        const redisConfig = this.getRedisConfig();
        const requiredFields = ['host', 'port', 'password'];
        for (const field of requiredFields) {
            if (!redisConfig[field]) {
                throw new Error(`Missing required Redis config field: ${field}`);
            }
        }
    }
}

module.exports = ConfigParser;