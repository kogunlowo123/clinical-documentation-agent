#!/bin/bash
set -euo pipefail
echo "Setting up Clinical Documentation Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
