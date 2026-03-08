from snowflake import SnowflakeGenerator

def internal_code_generator() -> str:
  code = SnowflakeGenerator(1)

  next_code = next(code)

  return str(next_code)
