# tunr
API serving model tuning based on Bayesian optimization. For concurrent usage and easy deployment.


## Data validation
The `pydantic` data model system is strongly tied to `FastAPI`. In using that framework we achieve data validation at
the API endpoint-level.

## `.env`-file
The `docker-compose` builder depends on environment variables defined in `.env`-file. For security reasons, the actual
file used by each user should not be committed. Instead, a template `.env.template` is included with the repo to
indicate which parameters require setting.




## Resources
The following tutorials on building apps relying on `FastAPI`, a `postgres` application database and serving via `Docker` containers have been used as starting point
* Jeff Astor: Up and running with FastAPI ([part 1](https://www.jeffastor.com/blog/up-and-running-with-fastapi-and-docker), [part 2](https://www.jeffastor.com/blog/pairing-a-postgresql-db-with-your-dockerized-fastapi-app), [part 3](https://www.jeffastor.com/blog/hooking-fastapi-endpoints-up-to-a-postgres-database))
* Ahmed Nafies: FastAPI with SQLAlchemy, PostgreSQL and Alembic and of course Docker ([part 1](https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396), [part 2](https://ahmed-nafies.medium.com/tutorial-fastapi-sqlalchemy-postgresql-alembic-and-docker-part-2-asynchronous-version-8a339ce97e6d))