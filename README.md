# dns-owl
This is a little Python script that updates your IP to the DynDNS servers of Cloudflare

# Use
You can deploy this container on your server and update your public IP to the Cloudflare DynDNS Servers. You can specify the update intervall in the environment variables using standard cron notation.

In the config.json you can enter the domains you want to update by a comma-separated list.
New for Cloudflare: you have to add your Zone ID, Record IDs and API Key, as well as the Mail to access the Cloudflare API and Update your records.


# Careful
The script waits the specified interval before doing its first update. If you chose a long one (eg. 1 day) it takes as much time for the first update. During this, nothing is written to the log, so it can seems as the container is hung up, which is not the case.
I try to remove this and have it run an update right at the start of the container.
I will try to make the logs more verbose in future versions.

# Strato
Support for Strato is deprecated, since I no longer host my domains there and cannot test any changes.
With the next update I will tr to make the script supporting both.
