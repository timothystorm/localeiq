import typer

from data_store.impl.locale_repo_impl import LocaleRepoImpl

app = typer.Typer()


@app.command()
def list_locales():
    # start = time.time()
    repo = LocaleRepoImpl()
    for locale in repo.read_all():
        typer.echo(locale.__dict__)


# typer.echo(f"Took {time.time() - start} seconds")


if __name__ == "__main__":
    app()
