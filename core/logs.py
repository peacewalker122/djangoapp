import json_log_formatter


class JSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message, extra, record):
        extra.update(
            {
                "source": "django",
                "level": record.levelname,
                "pathname": record.pathname,
                "lineno": record.lineno,
            }
        )

        for k, v in extra.items():
            extra[k] = str(v)

        return super().json_record(message, extra, record)
