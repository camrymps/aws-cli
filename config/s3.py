from botocore.config import Config

"""
Boto3 S3 client configuration object.

Learn more here config_.

.. _config: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
"""
def config(**kwargs) -> Config:
    return Config(
        # Default configuration options go here.
        #
        # Ex: 
        # region_name="us-east-1",
        # client_cert="/tls/cert.crt",
        # use_fips_endpoint=True,
        # ...

        # '**kwargs' must be LAST
        **kwargs
    )