import h5py
from pydantic import FilePath
from typing import TypedDict, List
from numpy import ndarray


class ResultDict(TypedDict):
    label: str
    array: ndarray


class H5pyStruct(TypedDict):
    name: str
    result: List[ResultDict]


def write_result(result: ResultDict, result_file: FilePath):
    """
    Export a
    :param result:
    :param result_file:
    :return:
    """
    with h5py.File(result_file, "w") as f:
        for keys in result:
            f[keys] = result[keys]
