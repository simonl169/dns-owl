python -c 'from owl.owl import *; starting_message()' # Run starting message and logo
python main.py # Run Update once directly at the start
echo "$CRONVARS2" "cd /app && python main.py" > mycron
crontab mycron
crond
python -m start_server
