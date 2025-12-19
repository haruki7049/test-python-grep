import click
import os
import termcolor


class Grep:
    @staticmethod
    def grep_from_str(text: str, target: str):
        lines: list[str] = text.splitlines()

        for line in lines:
            if target in line:
                # To print the line with colored target term, Split line by target term
                terms: list[str] = line.partition(target)

                for term in terms:
                    if term is target:
                        termcolor.cprint(term, 'red', end='')
                    else:
                        print(term, end='')

                print()


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
