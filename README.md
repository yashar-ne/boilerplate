# boilerplate for FastAPI + SQLAlchemy + Alembic

To apply migrations to database run

```console
alembic upgrade head
```

To generate a new migration run

```console
alembic revision -m "Add a column"
```
