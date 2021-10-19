# tunr
API serving model tuning based on Bayesian optimization. For concurrent usage and easy deployment.


## `.env`-file
The `docker-compose` builder depends on environment variables defined in `.env`-file. For security reasons, the actual
file used by each user should not be committed. Instead, a template `.env.template` is included with the repo to
indicate which parameters require setting.