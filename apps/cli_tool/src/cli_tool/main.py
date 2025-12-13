import typer

from data_store.country.country_dao import read_countries

app = typer.Typer()


@app.command()
def hello():
    countries = read_countries()
    # print(countries)
    # data = {"data": countries}
    typer.echo(countries)


if __name__ == "__main__":
    app()
