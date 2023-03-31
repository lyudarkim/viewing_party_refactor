import pytest
from viewing_party.movie import Movie

def test_returns_valid_attributes():
    # Arrange/ Act
    movie = Movie("Ada Lovelace", "documentary", 5)
    
    # Assert
    assert movie.title == "Ada Lovelace"
    assert movie.genre == "documentary"
    assert movie.rating == 5