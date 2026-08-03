import os
import sys

# To simulate Pathways proxy, maybe we need JAX_BACKEND=proxy?
# But wait, without actual pathways proxy, it won't connect.
# Let's just see if we can import pathwaysutils in their virtualenv
try:
    import pathwaysutils
    print("found pathwaysutils version:", pathwaysutils.__version__)
    print("has_is_pathways_backend_used:", hasattr(pathwaysutils, "is_pathways_backend_used"))
except Exception as e:
    print(f"Error: {e}")
