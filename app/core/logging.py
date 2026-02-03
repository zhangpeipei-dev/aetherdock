
import structlog
import logging
import sys

def order_keys(logger, method_name, event_dict):
    """
    Reorder keys in the event dict to ensure consistent JSON output order.
    """
    # Define preferred key order
    key_order = [
        "timestamp",
        "env",
        "level",
        "filename",
        "func_name",
        "lineno",
        "event",
    ]
    
    ordered_dict = {}
    
    # Add keys in the preferred order
    for key in key_order:
        if key in event_dict:
            ordered_dict[key] = event_dict.pop(key)
            
    # Add any remaining keys (e.g. bound context variables)
    ordered_dict.update(event_dict)
    
    return ordered_dict

def setup_logging():
    structlog.configure(
        processors=[
            # Add timestamp in ISO format and +8 hours
            structlog.processors.TimeStamper(fmt="iso", utc=False),
            structlog.stdlib.add_log_level,
            structlog.processors.CallsiteParameterAdder(
                parameters=[
                    structlog.processors.CallsiteParameter.FILENAME,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                    structlog.processors.CallsiteParameter.LINENO,
                ]
            ),
            order_keys,  # Add the custom ordering processor before rendering
            structlog.processors.JSONRenderer(),
        ],
        logger_factory=structlog.PrintLoggerFactory(),
    )

logger = structlog.get_logger()
