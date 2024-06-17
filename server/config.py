application = {
    "type": "desktop",
    "framework": {
        "custom": ["Tkinter", "EntanglementManager.py"]
    }
}

environment_variables = {
    "database_url": "sqlite:///database_prod.sqlite",
    "api_key": "your_api_key",
    "smtp_server": "smtp.example.com",
    "smtp_username": "your_username",
    "smtp_password": "your_password",
    "log_level": "INFO"
}

database = {
    "development": {
        "type": "SQLite",
        "path": "database_dev.sqlite"
    },
    "testing": {
        "type": "SQLite",
        "path": "database_test.sqlite"
    },
    "production": {
        "type": "SQLite",
        "path": "database_prod.sqlite"
    }
}

settings = {
    "debug_mode": True,
    "testing_mode": False,
    "log_level": "INFO"
}

logging = {
    "development": {
        "level": "DEBUG",
        "file": "logs/dev.log"
    },
    "testing": {
        "level": "INFO",
        "file": "logs/test.log"
    },
    "production": {
        "level": "WARNING",
        "file": "logs/prod.log"
    }
}

error_reporting = {
    "email": {
        "smtp_server": "smtp.example.com",
        "username": "your_username",
        "password": "your_password",
        "from_address": "errors@example.com",
        "to_address": "admin@example.com"
    }
}

security = {
    "secret_key": "your_secret_key",
    "https_enabled": True,
    "cors_settings": {
        "allowed_origins": ["http://localhost", "https://yourdomain.com"]
    }
}

performance = {
    "connection_pooling": True,
    "cache_settings": {
        "enabled": True,
        "type": "memory",
        "timeout": 300
    }
}

third_party_services = {
    "email_service": {
        "smtp_server": "smtp.example.com",
        "username": "your_username",
        "password": "your_password"
    },
    "cloud_storage": {
        "provider": "aws_s3",
        "access_key": "your_access_key",
        "secret_key": "your_secret_key",
        "bucket_name": "your_bucket_name"
    }
}