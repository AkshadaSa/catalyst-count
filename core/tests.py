import environ

env = environ.Env()
environ.Env.read_env()

print("DB_NAME:", env('DB_NAME', default='default_value'))
print("DB_USER:", env('DB_USER', default='default_value'))
print("DB_PASSWORD:", env('DB_PASSWORD', default='default_value'))
print("DB_HOST:", env('DB_HOST', default='default_value'))
print("DB_PORT:", env('DB_PORT', default='default_value'))
