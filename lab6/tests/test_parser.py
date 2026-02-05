import pytest
from src.parser import parse_product_basic, parse_availability


def test_parse_product_basic_extracts_id(valid_product):
    parsed_product = parse_product_basic(valid_product)
    assert parsed_product["id"] == valid_product["id"]

def test_parse_product_basic_extracts_name(valid_product):
    parsed_product = parse_product_basic(valid_product)
    assert parsed_product["name"] == valid_product["name"]

def test_parse_product_basic_returns_only_id_and_name(valid_product):
    parsed_product = parse_product_basic(valid_product)

    assert set(parsed_product) == {"id", "name"}
