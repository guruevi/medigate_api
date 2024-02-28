# coding: utf-8

"""
    Medigate API

    # Authentication To use this API, create an API user from Admin Settings > User Management, and generate an API token. Use the token as an [HTTP bearer token](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#authentication_schemes) to authenticate and authorize your API requests.  To use the token, add an `Authorization` header such as: ``` Authorization: Bearer <your token here> ```  # API Conventions  ## Pagination The endpoints in this API are paginated. To iteratively obtain all data, make repeated requests with increasing `offset` starting at 0, and constant `limit`. For example, `{\"offset\": 0, \"limit\": 100}`, followed by `{\"offset\": 100, \"limit\": 100}`, `{\"offset\": 200, \"limit\": 100}`, until less than `limit` results are returned.  ## Filters The endpoints in this API accept a `filter_by` argument to filter the results returned by the endpoint. Filters can be simple filters over a single field, or compound filters made up of other fields. For an example, look at the `filter_by` parameter of the endpoints below.  ### Simple Filters Filters a single field of the result set. The `operation` may be one of:  |`operation`s|Description|`value` Type| |---|---|---| |`in`, `not_in`|Checks for equality/inequality of any of the values|Array of values| |`contains`, `not_contains`|Checks if the string in `value` is contained in the field|string| |`in_subnet`, `not_in_subnet`|Checks if an IP field is in the subnet in `value`|string or list of strings specifying an IP subnet in CIDR notation, such as `\"192.168.1.0/24\"`| | `is_null`, `is_not_null`|Checks if the field has null value|_None_| |`greater`, `greater_or_equal`, `less`, `less_or_equal`|Compares with `value`|a number or timestamp (ISO format) to compare with| |`after_seconds_ago`, `before_seconds_ago`|Compares the field with a timestamp relative to the current date and time|number of seconds|  ### Compound Filters Simple filters can be combined with compound filters. The supported `operation`s are: * `not` - Takes a single filter in `operands`, and negates the filter's condition * `and`, `or` - Take multiple filters in `operands`, and combines them with the appropriate boolean operation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "medigate-api"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum"
]

setup(
    name=NAME,
    version=VERSION,
    description="Medigate API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Medigate API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    # Authentication To use this API, create an API user from Admin Settings &gt; User Management, and generate an API token. Use the token as an [HTTP bearer token](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#authentication_schemes) to authenticate and authorize your API requests.  To use the token, add an &#x60;Authorization&#x60; header such as: &#x60;&#x60;&#x60; Authorization: Bearer &lt;your token here&gt; &#x60;&#x60;&#x60;  # API Conventions  ## Pagination The endpoints in this API are paginated. To iteratively obtain all data, make repeated requests with increasing &#x60;offset&#x60; starting at 0, and constant &#x60;limit&#x60;. For example, &#x60;{\&quot;offset\&quot;: 0, \&quot;limit\&quot;: 100}&#x60;, followed by &#x60;{\&quot;offset\&quot;: 100, \&quot;limit\&quot;: 100}&#x60;, &#x60;{\&quot;offset\&quot;: 200, \&quot;limit\&quot;: 100}&#x60;, until less than &#x60;limit&#x60; results are returned.  ## Filters The endpoints in this API accept a &#x60;filter_by&#x60; argument to filter the results returned by the endpoint. Filters can be simple filters over a single field, or compound filters made up of other fields. For an example, look at the &#x60;filter_by&#x60; parameter of the endpoints below.  ### Simple Filters Filters a single field of the result set. The &#x60;operation&#x60; may be one of:  |&#x60;operation&#x60;s|Description|&#x60;value&#x60; Type| |---|---|---| |&#x60;in&#x60;, &#x60;not_in&#x60;|Checks for equality/inequality of any of the values|Array of values| |&#x60;contains&#x60;, &#x60;not_contains&#x60;|Checks if the string in &#x60;value&#x60; is contained in the field|string| |&#x60;in_subnet&#x60;, &#x60;not_in_subnet&#x60;|Checks if an IP field is in the subnet in &#x60;value&#x60;|string or list of strings specifying an IP subnet in CIDR notation, such as &#x60;\&quot;192.168.1.0/24\&quot;&#x60;| | &#x60;is_null&#x60;, &#x60;is_not_null&#x60;|Checks if the field has null value|_None_| |&#x60;greater&#x60;, &#x60;greater_or_equal&#x60;, &#x60;less&#x60;, &#x60;less_or_equal&#x60;|Compares with &#x60;value&#x60;|a number or timestamp (ISO format) to compare with| |&#x60;after_seconds_ago&#x60;, &#x60;before_seconds_ago&#x60;|Compares the field with a timestamp relative to the current date and time|number of seconds|  ### Compound Filters Simple filters can be combined with compound filters. The supported &#x60;operation&#x60;s are: * &#x60;not&#x60; - Takes a single filter in &#x60;operands&#x60;, and negates the filter&#39;s condition * &#x60;and&#x60;, &#x60;or&#x60; - Take multiple filters in &#x60;operands&#x60;, and combines them with the appropriate boolean operation
    """,  # noqa: E501
    package_data={"medigate_api": ["py.typed"]},
)