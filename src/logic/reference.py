"""
Author: Niklas
See from types: wikipedia https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management
e.g. booklet, inbook, incollection, manual, mastersthesis/phdhesis, misc, proceedings, tech report, unpublished
"""
from attrs import define, validators, field
from typing import Optional
from datetime import datetime


def check_year(instance, attribute, given_year):
    """
    Checks that publishment year is in a reasonable range;
    e.g [500, current year + 5]
    """
    year_now = datetime.now().year
    if (given_year > year_now + 5) or (given_year < 500):
        raise ValueError(f"Given year is not in range [500, {year_now+5}]")


def check_name(instance, attribute, given_name):
    """
    Check that name is in proper format:
    - Firstname + ... + Surname
    - str made of [Aa-Zz]
    """
    split_name = given_name.split()
    len_n = len(split_name)
    if len_n < 2:
        raise ValueError("First name and surname is required")
    for name in split_name:
        if not name.isalpha():
            raise ValueError("Name has to consists only of alphabet letters")


def check_len(instance, attribute, given_str):
    """
    BibTeX has a 5000 character limit for each field?
    e.g. https://clemson.libguides.com/LaTeX
    """
    if given_str is not None and len(given_str) > 5000:
        raise ValueError("Str length exceeds BibTeX field character limit of 5000")


def check_str(instance, attribute, given_str):
    if given_str is not None and not isinstance(given_str, str):
        raise ValueError("Given value is not a string.")


@define
class Book:
    """
    @book{Martin09,
        author = {Martin, Robert},
        title = {Clean Code: A Handbook of Agile Software Craftsmanship},
        year = {2008},
        publisher = {Prentice Hall},
    }
    """

    author: str = field(validator=[validators.instance_of(str), check_name, check_len])
    title: str = field(validator=[validators.instance_of(str), check_len])
    year: int = field(converter=int, validator=[validators.instance_of(int), check_year])
    publisher: str = field(validator=[validators.instance_of(str), check_len])

    address: Optional[str] = field(default=None, validator=[check_str, check_len])
    edition: Optional[str] = field(default=None, validator=[check_str, check_len])
    editor: Optional[str] = field(default=None, validator=[check_str, check_len])
    month: Optional[str] = field(default=None, validator=[check_str, check_len])
    note: Optional[str] = field(default=None, validator=[check_str, check_len])
    number: Optional[str] = field(default=None, validator=[check_str, check_len])
    series: Optional[str] = field(default=None, validator=[check_str, check_len])
    volume: Optional[str] = field(default=None, validator=[check_str, check_len])


@define
class Article:
    """
    @article{CBH91,
        author = {Allan Collins and John Seely Brown and Ann Holum},
        title = {Cognitive apprenticeship: making thinking visible},
        journal = {American Educator},
        year = {1991},
        volume = {6},
        pages = {38--46}
    }
    """

    author: str = field(validator=[validators.instance_of(str), check_name, check_len])
    journal: str = field(validator=[validators.instance_of(str), check_len])
    title: str = field(validator=[validators.instance_of(str), check_len])
    year: int = field(converter=int, validator=[validators.instance_of(int), check_year])

    month: Optional[str] = field(default=None, validator=[check_str, check_len])
    note: Optional[str] = field(default=None, validator=[check_str, check_len])
    number: Optional[str] = field(default=None, validator=[check_str, check_len])
    pages: Optional[str] = field(default=None, validator=[check_str, check_len])
    volume: Optional[str] = field(default=None, validator=[check_str, check_len])


@define
class Inproceedings:
    """
    @inproceedings{VPL11,
        author = {Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti},
        title = {Extreme Apprenticeship Method in Teaching Programming for Beginners.},
        year = {2011},
        booktitle = {SIGCSE '11: Proceedings of the 42nd SIGCSE technical symposium on Computer science education},
    }
    """

    author: str = field(validator=[validators.instance_of(str), check_name, check_len])
    title: str = field(validator=[validators.instance_of(str), check_len])
    year: int = field(converter=int, validator=[validators.instance_of(int), check_year])
    booktitle: str = field(validator=[validators.instance_of(str), check_len])

    address: Optional[str] = field(default=None, validator=[check_str, check_len])
    editor: Optional[str] = field(default=None, validator=[check_str, check_len])
    month: Optional[str] = field(default=None, validator=[check_str, check_len])
    note: Optional[str] = field(default=None, validator=[check_str, check_len])
    number: Optional[str] = field(default=None, validator=[check_str, check_len])
    organization: Optional[str] = field(default=None, validator=[check_str, check_len])
    pages: Optional[str] = field(default=None, validator=[check_str, check_len])
    publisher: Optional[str] = field(default=None, validator=[check_str, check_len])
    series: Optional[str] = field(default=None, validator=[check_str, check_len])
    volume: Optional[str] = field(default=None, validator=[check_str, check_len])
