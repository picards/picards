class Config:
    APP_NAME = 'studypi'


class DevConfig(Config):
    DEBUG = True

    SAWO_API_KEY = 'cdf3f6a8-b776-43f7-85f3-4d898a7a0779'


class ProdConfig(Config):
    DEBUG = False

    SAWO_API_KEY = '34b10c22-1add-4f46-90fa-8b28dbe38d83'


COCKROACH_CONN = {
    'dbname': 'studypi',
    'user': 'michael',
    'password': 'xlwl1riDrupan4p7#',
    'sslmode': 'verify-full',
    'sslrootcert': 'app/ca.crt',
    'port': 26257,
    'host': 'free-tier.gcp-us-central1.cockroachlabs.cloud',
    'options': '--cluster=pure-bull-2141'
}