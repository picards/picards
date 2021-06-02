class Config:
    APP_NAME = 'studypi'

    DBNAME = 'studypi'
    USER = 'michael'
    PASSWORD = '3H$xlwl1riDrupan4p7#'
    SSLMODE = 'verify-full'
    SSLROOTCERT = 'app/ca.crt'
    PORT = 26257
    HOST = 'free-tier.gcp-us-central1.cockroachlabs.cloud'
    OPTIONS = '--cluster=pure-bull-2141'


class DevConfig(Config):
    DEBUG = True

    SAWO_API_KEY = 'cdf3f6a8-b776-43f7-85f3-4d898a7a0779'


class ProdConfig(Config):
    DEBUG = False

    SAWO_API_KEY = '34b10c22-1add-4f46-90fa-8b28dbe38d83'