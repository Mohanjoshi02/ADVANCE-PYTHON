
import logging

logger = logging.getLogger("Experiment14Logger")
logger.setLevel(logging.DEBUG)  # Capture all levels starting from DEBUG

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app_experiment14.log", mode="w", encoding="utf-8")

console_handler.setLevel(logging.INFO)

file_handler.setLevel(logging.DEBUG)

console_format = logging.Formatter("{levelname} - {message}", style="{")
file_format = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

print("--- Starting Logging Demo ---")

logger.debug("This is a DEBUG message (Detailed info for developers).")
logger.info("This is an INFO message (General program status).")
logger.warning("This is a WARNING message (Something unexpected happened).")
logger.error("This is an ERROR message (A serious problem occurred).")
logger.critical("This is a CRITICAL message (System crash or severe failure).")

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("An exception occurred: Division by zero!")

print("--- Logging Complete. Check 'app_experiment14.log' file for output logs ---")

