# coding: utf-8

"""
    Amun API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from amun.swagger_client.models.inspection_specification_build import InspectionSpecificationBuild  # noqa: F401,E501
from amun.swagger_client.models.inspection_specification_files import InspectionSpecificationFiles  # noqa: F401,E501
from amun.swagger_client.models.inspection_specification_python import InspectionSpecificationPython  # noqa: F401,E501
from amun.swagger_client.models.inspection_specification_run import InspectionSpecificationRun  # noqa: F401,E501


class InspectionSpecification(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'base': 'str',
        'packages': 'list[str]',
        'python_packages': 'list[str]',
        'python': 'InspectionSpecificationPython',
        'identifier': 'str',
        'build': 'InspectionSpecificationBuild',
        'run': 'InspectionSpecificationRun',
        'files': 'list[InspectionSpecificationFiles]',
        'script': 'str'
    }

    attribute_map = {
        'base': 'base',
        'packages': 'packages',
        'python_packages': 'python_packages',
        'python': 'python',
        'identifier': 'identifier',
        'build': 'build',
        'run': 'run',
        'files': 'files',
        'script': 'script'
    }

    def __init__(self, base=None, packages=None, python_packages=None, python=None, identifier=None, build=None, run=None, files=None, script=None):  # noqa: E501
        """InspectionSpecification - a model defined in Swagger"""  # noqa: E501

        self._base = None
        self._packages = None
        self._python_packages = None
        self._python = None
        self._identifier = None
        self._build = None
        self._run = None
        self._files = None
        self._script = None
        self.discriminator = None

        self.base = base
        if packages is not None:
            self.packages = packages
        if python_packages is not None:
            self.python_packages = python_packages
        if python is not None:
            self.python = python
        if identifier is not None:
            self.identifier = identifier
        if build is not None:
            self.build = build
        if run is not None:
            self.run = run
        if files is not None:
            self.files = files
        if script is not None:
            self.script = script

    @property
    def base(self):
        """Gets the base of this InspectionSpecification.  # noqa: E501

        Base image on which the runtime environment should be based on.  # noqa: E501

        :return: The base of this InspectionSpecification.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this InspectionSpecification.

        Base image on which the runtime environment should be based on.  # noqa: E501

        :param base: The base of this InspectionSpecification.  # noqa: E501
        :type: str
        """
        if base is None:
            raise ValueError("Invalid value for `base`, must not be `None`")  # noqa: E501
        if base is not None and len(base) < 1:
            raise ValueError("Invalid value for `base`, length must be greater than or equal to `1`")  # noqa: E501

        self._base = base

    @property
    def packages(self):
        """Gets the packages of this InspectionSpecification.  # noqa: E501

        A list of native packages that should be installed into the runtime environment.  # noqa: E501

        :return: The packages of this InspectionSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this InspectionSpecification.

        A list of native packages that should be installed into the runtime environment.  # noqa: E501

        :param packages: The packages of this InspectionSpecification.  # noqa: E501
        :type: list[str]
        """

        self._packages = packages

    @property
    def python_packages(self):
        """Gets the python_packages of this InspectionSpecification.  # noqa: E501

        A list of python packages that should be installed into the runtime environment.  # noqa: E501

        :return: The python_packages of this InspectionSpecification.  # noqa: E501
        :rtype: list[str]
        """
        return self._python_packages

    @python_packages.setter
    def python_packages(self, python_packages):
        """Sets the python_packages of this InspectionSpecification.

        A list of python packages that should be installed into the runtime environment.  # noqa: E501

        :param python_packages: The python_packages of this InspectionSpecification.  # noqa: E501
        :type: list[str]
        """

        self._python_packages = python_packages

    @property
    def python(self):
        """Gets the python of this InspectionSpecification.  # noqa: E501


        :return: The python of this InspectionSpecification.  # noqa: E501
        :rtype: InspectionSpecificationPython
        """
        return self._python

    @python.setter
    def python(self, python):
        """Sets the python of this InspectionSpecification.


        :param python: The python of this InspectionSpecification.  # noqa: E501
        :type: InspectionSpecificationPython
        """

        self._python = python

    @property
    def identifier(self):
        """Gets the identifier of this InspectionSpecification.  # noqa: E501

        A user-created string which will be inserted into the inspection id to distinguish different inspection runs.  # noqa: E501

        :return: The identifier of this InspectionSpecification.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this InspectionSpecification.

        A user-created string which will be inserted into the inspection id to distinguish different inspection runs.  # noqa: E501

        :param identifier: The identifier of this InspectionSpecification.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def build(self):
        """Gets the build of this InspectionSpecification.  # noqa: E501


        :return: The build of this InspectionSpecification.  # noqa: E501
        :rtype: InspectionSpecificationBuild
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this InspectionSpecification.


        :param build: The build of this InspectionSpecification.  # noqa: E501
        :type: InspectionSpecificationBuild
        """

        self._build = build

    @property
    def run(self):
        """Gets the run of this InspectionSpecification.  # noqa: E501


        :return: The run of this InspectionSpecification.  # noqa: E501
        :rtype: InspectionSpecificationRun
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this InspectionSpecification.


        :param run: The run of this InspectionSpecification.  # noqa: E501
        :type: InspectionSpecificationRun
        """

        self._run = run

    @property
    def files(self):
        """Gets the files of this InspectionSpecification.  # noqa: E501

        Files passed to the context.  # noqa: E501

        :return: The files of this InspectionSpecification.  # noqa: E501
        :rtype: list[InspectionSpecificationFiles]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this InspectionSpecification.

        Files passed to the context.  # noqa: E501

        :param files: The files of this InspectionSpecification.  # noqa: E501
        :type: list[InspectionSpecificationFiles]
        """

        self._files = files

    @property
    def script(self):
        """Gets the script of this InspectionSpecification.  # noqa: E501

        A script that should be executed in inspection run.  # noqa: E501

        :return: The script of this InspectionSpecification.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this InspectionSpecification.

        A script that should be executed in inspection run.  # noqa: E501

        :param script: The script of this InspectionSpecification.  # noqa: E501
        :type: str
        """

        self._script = script

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InspectionSpecification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InspectionSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
