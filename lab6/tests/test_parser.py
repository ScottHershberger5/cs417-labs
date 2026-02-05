
from parser import parse_product_basic, parse_availability


def test_parse_product_basic_extracts_id(valid_product):
    parsed_product = parse_product_basic(valid_product)
    assert parsed_product["id"] == valid_product["id"]

def test_parse_product_basic_extracts_name(valid_product):
    parsed_product = parse_product_basic(valid_product)
    assert parsed_product["name"] == valid_product["name"]

def test_parse_product_basic_returns_only_id_and_name(valid_product):
    parsed_product = parse_product_basic(valid_product)

    assert set(parsed_product) == {"id", "name"}

# availability tests

def test_parse_availability_when_in_stock(valid_product):
    parsed_availabliity = parse_availability(valid_product)
    assert parsed_availabliity["in_stock"] == True

def test_parse_availability_when_out_of_stock(product_out_of_stock):
    parsed_availabliity = parse_availability(product_out_of_stock)
    assert parsed_availabliity["in_stock"] == False

def test_parse_availability_when_field_missing(minimal_product):
    parsed_availabliity = parse_availability(minimal_product)
    assert parsed_availabliity["in_stock"] == False