python=python3.7
cmd="$python main.py"
until $cmd; do
    echo "Slack bot crashed with exit code $?. Respawning.." >&2
    sleep 1
done
