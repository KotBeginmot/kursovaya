import pytest
from src.main import tranzact_execute, five_operations, main

LINK = "operations.json"
def test_main():
    assert main([]) == "empty list"
    assert main(LINK) == "main complited"

def test_tranzact_execute():
    assert type(tranzact_execute(LINK)) == list

def test_five_operations():
    assert five_operations([]) == "operation list"




