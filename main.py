import click
import os
import termcolor


class Grep:
    @staticmethod
    def grep_from_str(text: str, target: str, is_colored_output: bool):
        lines: list[str] = text.splitlines()

        for line in lines:
            if target in line:
                # To print the line with colored target term, Split line by target term
                terms: list[str] = line.partition(target)

                if is_colored_output:
                    for term in terms:
                        if term is target:
                            termcolor.cprint(term, 'red', end='')
                        else:
                            print(term, end='')

                    print()

                else:
                    print(line)


class FileReader:
    @staticmethod
    def read_path(path: str) -> str:
        with open(path, "r") as f:
            return f.read();


@click.command()
@click.argument("path", type=str)
@click.argument("target", type=str)
@click.option("--colored-output", is_flag=True)
def main(path: str, target: str, colored_output: bool):
    context = FileReader.read_path(path)
    Grep.grep_from_str(context, target, color)


if __name__ == "__main__":
    main()
