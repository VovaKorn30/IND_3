import click

@click.group()
def cli():
    """Група команд CLI"""
    pass


@cli.command()
@click.option("--name", prompt="Введіть ім'я", help="Ім'я користувача для виводу")
def say(name):
    """Команда для виводу імені, крім тих, що починаються на 'p'"""
    if name.lower().startswith('p'):
        click.echo("Ім’я не підходить")
    else:
        click.echo(f"Введене ім'я: {name}")


if __name__ == "__main__":
    cli()
