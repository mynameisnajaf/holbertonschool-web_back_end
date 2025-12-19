#!/usr/bin/env python3
"""A module that contains function"""


def list_all(mongo_collection):
    """function that lists all documents in a collection"""
    if mongo_collection.find() is None:
        return []
    return list(mongo_collection.find())
