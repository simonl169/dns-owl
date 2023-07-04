echo "$CRONVARS2" "cd /app && python main.py" >> mycron
crontab mycron
crond -f