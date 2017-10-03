from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os
from collections import OrderedDict


def get_real_file_path(file_path):
    """This function gets a file path, can be either relative or absolute, 
    parse it and return the absolute real file path.

    If the file path contains tilde, it will be expanded to the user's home
    directory if set.
    If the file path is relative, it will be expanded in respect to the
    current working directory.

    :param file_path: A path to a file.
    :return: The absolute real path for the file.
    """
    file_path = os.path.expanduser(file_path)
    file_path = os.path.abspath(file_path)
    return file_path


def generate_json_output(file_path, future_location, version, s3_path):
    """This function generates a JSON output response for placing in the
    project's dependencies configuration file.

    :param file_path: The file path provided by the user.
    :param future_location: The location in which the file should be placed
    in the user's project.
    :param version: The version generated by the tool for this file.
    :param s3_path: path to the file location in S3

    :return: The JSON response with the fields ordered by the creation order.
    """
    json_response = OrderedDict()
    json_response['name'] = os.path.basename(file_path)
    json_response['version'] = version
    json_response['location'] = future_location
    json_response['s3path'] = s3_path

    return json_response


def print_output_message(json_response):
    """This function prints the JSON response along with some more information
    on what to do with the response.

    :param json_response: The JSON response to print. Should be a dict-like
    object.

    :return: Nothing, just prints to stdout. 
    """
    msg = 'The file {0} has been successfully uploaded!\nAdd this json to ' \
          'your microservice dependencies.json ' \
          'configuration file, as another item in the "dependencies" ' \
          'list:\n\n{1}\n'.format(json_response['name'],
                                  json.dumps(json_response, indent=2))
    print(msg)
