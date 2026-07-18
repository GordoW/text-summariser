from dotenv import load_dotenv
import os


load_dotenv()


APP_NAME = os.getenv(
    "APP_NAME",
    "Default API Name"
)

APP_DESC = os.getenv(
    "APP_DESC",
    "Default API description"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "0.0.1"
)

DEBUG = os.getenv(
    "DEBUG",
    "False"
) == "True"