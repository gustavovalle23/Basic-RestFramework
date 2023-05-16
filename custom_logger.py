import logging
from newrelic import context
from newrelic.agent import NewRelicHandler


class CustomLogger(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

        # Add a New Relic handler to send logs to New Relic
        handler = NewRelicHandler()
        handler.setLevel(logging.INFO)
        self.addHandler(handler)

    def _log(self, level, msg, args, kwargs):
        # Get the tenant ID from the New Relic context
        tenant_id = context.get("tenant_id", "unknown")

        # Add the tenant ID to the log record
        kwargs["extra"] = {"tenant_id": tenant_id}

        # Call the parent _log method to actually log the record
        super()._log(level, msg, args, kwargs)
