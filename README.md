# dns-owl
This is a little Python script that updates your IP to the DynDNS servers of Strato

# Use
You can deploy this container on your server and update your public IP to the Strato DynDNS Servers. You can specify the update intervall in the environment variables using standard cron notation.

In the config.json you can enter the domains you want to update by a comma-separated list

# Careful
The script waits the specified interval before doing its first update. If you chose a long one (eg. 1 day) it takes as much time for the first update. During this, nothing is written to the log, so it can seems as the container is hung up, which is not the case.
I will try to make the logs more verbose in future versions.
