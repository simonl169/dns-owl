# dns-owl
This is a little Python script that updates your IP to the DynDNS servers of Cloudflare

# Use
You can deploy this container on your server and update your public IP to the Cloudflare DynDNS Servers. You can specify the update intervall in the environment variables using standard cron notation.

In the config.json you can enter the domains you want to update by a comma-separated list.
New for Cloudflare: you have to add your Zone ID, Record IDs and API Key, as well as the Mail to access the Cloudflare API and Update your records.

~~~
{
  "PUBLIC_IP_CHECK": "CLOUDFLARE",
  "ENABLE_WEBSERVER": true,
  "WEBSERVER_PORT": 8000,
  "NOTIFY_SERVER": "https://<YOUR_NTFY_SERVER>/<TOPIC>",
  "ENABLE_NOTIFICATIONS": false,
  "ZONE_ID": "your_zone_id",
  "USER_EMAIL": "name.lastname@mail.com",
  "API_KEY": "your_CF_API_key",
  "domains": [
     {
       "RECORD_ID": "record_key_1",
       "RECORD_NAME": "sub1.domain.com"
     },
     {
       "RECORD_ID": "record_key_2",
       "RECORD_NAME": "sub2.domain.com"
     }
  ]

}

~~~

# Record ID and Zone ID, API Key
You can get your Zone ID and API Key form your Cloudflare Profile. If you are unsure, refer to the Cloudflare docs.
With Zone ID, Key and Mail, you can run
~~~
curl --request GET \
  --url https://api.cloudflare.com/client/v4/zones/{YOUR_ZONE_ID}/dns_records \
  --header 'Content-Type: application/json' \
  --header 'X-Auth-Email: name.lastname@domain.com' \
  --header 'X-Auth-Key: {YOUR_API_KEY}'
~~~
The result contains a list of your subdomains for this record and their corresponding RECORD_ID.

# Careful
The script waits the specified interval before doing its first update. If you chose a long one (eg. 1 day) it takes as much time for the first update. During this, nothing is written to the log, so it can seems as the container is hung up, which is not the case.
I try to remove this and have it run an update right at the start of the container.
I will try to make the logs more verbose in future versions.

# Strato
Support for Strato is deprecated, since I no longer host my domains there and cannot test any changes.
With the next update I will tr to make the script supporting both.
