## Adding new dependencies

LocaleIQ uses Poetry to manage its dependencies. To add a new dependency, follow these steps:

For example, adding a new package to the `apps/date_time` project:

```bash
   poetry --directory apps/core install <package-name>
```

> Don't forget the `--directory` flag to specify the correct project path.
> If the packages get added to the root `pyproject.toml`, you might have missed this flag.
> You can always remove the unwanted packages from the root `pyproject.toml` and `poetry.lock` files manually.