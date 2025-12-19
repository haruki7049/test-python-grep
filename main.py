import click
import os


class Grep:
    @staticmethod
    def grep_from_str(text: str, target: str):
        lines = text.splitlines()
        for line in lines:
            if target in line:
                print(line)


class FileReader:
    @staticmethod
    def read_path(path: str) -> str:
        with open(path, "r") as f:
            return f.read();


@click.command()
@click.argument("path", type=str)
@click.argument("target", type=str)
def main(path: str, target: str):
    context = FileReader.read_path(path)
    Grep.grep_from_str(context, target)


if __name__ == "__main__":
    main()
