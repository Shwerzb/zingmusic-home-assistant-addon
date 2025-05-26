#!/usr/bin/env bash
echo "🔊 Starting Music Assistant with ZingMusic provider..."
export PYTHONPATH=/app
python3 -m music_assistant.server
