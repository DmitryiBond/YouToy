class RedisKeys:
    BALANCE_SUFFIX = "_balance"
    LOCAL_BALANCE_SUFFIX = "_balance_local"
    FACTOR_SUFFIX = "_factor"
    
    # Manual Control keys
    MANUAL_CMD_TYPE = "manual_cmd_type"
    MANUAL_CMD_DURATION = "manual_cmd_duration"
    MANUAL_CMD_SOURCE = "manual_cmd_source"
    
    # Trading keys
    TRADING_ENABLED = "trading_enabled"
    TRADING_INTERVAL = "trading_interval"
    TRADING_MODE = "trading_mode" # "crypto" or "polymarket"
    POLYMARKET_SLUG = "polymarket_slug"

    # Legacy Keys? (Used in main.py but seemingly specific)
    SOLANA_BALANCE = "solana_balance"
    TON_BALANCE = "ton_balance"

class CommandTypes:
    STROKE = "stroke"
    TWIST = "twist"
