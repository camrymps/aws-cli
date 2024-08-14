import click
from services.s3 import s3

@click.group()
def aws():
    pass

aws.add_command(s3)

if __name__ == '__main__':
    aws()