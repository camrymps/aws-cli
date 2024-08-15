import boto3
import click
from param_types.dict_param_type import DICT
from config.s3 import config
from lib.utils import remove_empty_args, recurse_directory


@click.group()
def s3():
    pass

@s3.command()
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--recursive",
    default=False,
    help="Command is performed on all files or objects under the specified directory or prefix.",
)
@click.option("--no-paginate", default=False, help="Disable automatic pagination.")
def ls():
    click.echo("ls")


@s3.command()
@click.argument("source", type=click.Path(exists=False))  # CopySource
@click.argument("destination", type=click.Path(exists=False))  # Key
@click.option(
    "--acl",
    type=click.Choice(
        [
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ]
    ),
)  # ACL
@click.option(
    "--sse", type=click.Choice(["AES256", "aws:kms", "aws:kms:dsse"])
)  # ServerSideEncryption
@click.option("--sse-c", type=click.STRING)  # SSECustomerAlgorithm
@click.option("--sse-c-key", type=click.STRING)  # SSECustomerKey
@click.option("--sse-kms-key-id", type=click.STRING)  # SSEKMSKeyId
@click.option(
    "--sse-c-copy-source", type=click.STRING
)  # CopySourceSSECustomerAlgorithm
@click.option("--sse-c-copy-source-key", type=click.STRING)  # CopySourceSSECustomerKey
@click.option(
    "--storage-class",
    type=click.Choice(
        [
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
            "OUTPOSTS",
            "GLACIER_IR",
            "SNOW",
            "EXPRESS_ONEZONE",
        ]
    ),
)  # SSEStorageClass
@click.option("--website-redirect", type=click.STRING)  # WebsiteRedirectionLocation
@click.option("--content-type", type=click.STRING)  # ContentType
@click.option("--cache-control", type=click.STRING)  # CacheControl
@click.option("--content-disposition", type=click.STRING)  # ContentDisposition
@click.option("--content-encoding", type=click.STRING)  # ContentEncoding
@click.option("--content-language", type=click.STRING)  # ContentLanguage
@click.option("--expires", type=click.DateTime())  # Expires
@click.option("--request-payer", type=click.STRING)  # RequestPayer
@click.option("--metadata", type=DICT())  # Metadata
@click.option(
    "--metadata-directive", type=click.Choice(["COPY", "REPLACE"])
)  # MetadataDirective
@click.option("--recursive", type=click.BOOL)

# Global options
@click.option("--no-paginate", type=click.BOOL)
@click.option("--output", type=click.Choice(["json", "text"]))
@click.option("--ca-bundle", type=click.STRING)
@click.option("--cli-read-timeout", type=click.INT)
@click.option("--cli-connect-timeout", type=click.INT)
def cp(**kwargs):
    """
    Description:

    Copies a local file or S3 object to another location locally or in S3.

    cp <LocalPath> <S3Uri> or <S3Uri> <LocalPath> or <S3Uri> <S3Uri>
    """

    source = kwargs.get("source")
    destination = kwargs.get("destination")
    bucket = None

    # Get the bucket
    if "s3://" in destination:
        bucket = destination[destination.index("s3://") + 5 :].split("/")[0]
    elif "s3://" in source:
        bucket = source[source.index("s3://") + 5 :].split("/")[0]
    elif "s3://" in source and "s3://" in destination:
        bucket = destination[destination.index("s3://") + 5 :].split("/")[0]

    # Assemble the arguments for the S3 client's 'copy_object' method
    args = remove_empty_args(
        {
            "Bucket": bucket,
            "CopySource": kwargs.get("source"),
            "Key": kwargs.get("key"),
            "ServerSideEncryption": kwargs.get("sse"),
            "SSECustomerAlgorithm": kwargs.get("sse_c"),
            "SSECustomerKey": kwargs.get("sse_c_key"),
            "SSEKMSKeyId": kwargs.get("sse_kms_key_id"),
            "CustomerSourceSSECustomerAlgorithm": kwargs.get("sse_c_copy_source"),
            "CustomerSourceSSECustomerKey": kwargs.get("sse_c_copy_source_key"),
            "StorageClass": kwargs.get("storage_class"),
            "WebsiteRedirectionLocation": kwargs.get("website_redirect"),
            "ContentType": kwargs.get("content_type"),
            "CacheControl": kwargs.get("cache_control"),
            "ContentDisposition": kwargs.get("content_disposition"),
            "ContentEncoding": kwargs.get("content_encoding"),
            "ContentLanguage": kwargs.get("content_language"),
            "Expires": kwargs.get("expires"),
            "RequestPayer": kwargs.get("request_payer"),
            "Metadata": kwargs.get("metadata"),
            "MetadataDirective": kwargs.get("metadata_directive"),
        }
    )

    print(args)

    s3_client = boto3.client(
        "s3",
        config=config(
            proxies_config={
                "proxy_ca_bundle": kwargs.get("ca_bundle")
            },
            connect_timeout=kwargs.get("connect_timeout"),
            read_timeout=kwargs.get("read-timeout"),
        ),
    )

    print(recurse_directory("C:\\Users\\Michael Scott\\OneDrive\\Documents\\Projects\\galactica-aws-cli"))

    #s3_client.copy_object(**args)
