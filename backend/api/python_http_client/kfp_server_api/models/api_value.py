# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kfp_server_api.configuration import Configuration


class ApiValue(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'int_value': 'str',
        'double_value': 'float',
        'string_value': 'str'
    }

    attribute_map = {
        'int_value': 'int_value',
        'double_value': 'double_value',
        'string_value': 'string_value'
    }

    def __init__(self, int_value=None, double_value=None, string_value=None, local_vars_configuration=None):  # noqa: E501
        """ApiValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._int_value = None
        self._double_value = None
        self._string_value = None
        self.discriminator = None

        if int_value is not None:
            self.int_value = int_value
        if double_value is not None:
            self.double_value = double_value
        if string_value is not None:
            self.string_value = string_value

    @property
    def int_value(self):
        """Gets the int_value of this ApiValue.  # noqa: E501


        :return: The int_value of this ApiValue.  # noqa: E501
        :rtype: str
        """
        return self._int_value

    @int_value.setter
    def int_value(self, int_value):
        """Sets the int_value of this ApiValue.


        :param int_value: The int_value of this ApiValue.  # noqa: E501
        :type int_value: str
        """

        self._int_value = int_value

    @property
    def double_value(self):
        """Gets the double_value of this ApiValue.  # noqa: E501


        :return: The double_value of this ApiValue.  # noqa: E501
        :rtype: float
        """
        return self._double_value

    @double_value.setter
    def double_value(self, double_value):
        """Sets the double_value of this ApiValue.


        :param double_value: The double_value of this ApiValue.  # noqa: E501
        :type double_value: float
        """

        self._double_value = double_value

    @property
    def string_value(self):
        """Gets the string_value of this ApiValue.  # noqa: E501


        :return: The string_value of this ApiValue.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this ApiValue.


        :param string_value: The string_value of this ApiValue.  # noqa: E501
        :type string_value: str
        """

        self._string_value = string_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiValue):
            return True

        return self.to_dict() != other.to_dict()