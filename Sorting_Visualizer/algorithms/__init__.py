import os
import importlib

algorithms = []

folder = os.path.dirname(__file__)

for file in os.listdir(folder):
    if file.endswith(".py") and file != "__init__.py":
        module_name = file[:-3]
        module = importlib.import_module(f"algorithms.{module_name}")

        if hasattr(module, "sort"):
            algorithms.append((module_name, module.sort))
