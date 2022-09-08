# python discord bot w/ health check
An example implementation of discord bot using discord.py with an empty http server.

## Motivation
Container execution environment such as Cloud Run requires the container to listen some port and reply for the healthcheck probes.
By default, discord bot implemented by discord.py does not listen any port and fails to be deployed to such environments.
This implementation is a workaround to deploy discord bot where healthcheck is required.

## Run
set your discord bot token to environment variable `ENV_VAR_DISCORD_ID`

Local:
```
python src/main.py
```
Docker:
```
docker build --tag discordbot .
docker run --rm --env ENV_VAR_DISCORD_ID -p 8080:8080 -i discordbot
```