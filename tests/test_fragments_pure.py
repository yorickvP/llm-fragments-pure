import os
from unittest.mock import patch
import llm
from llm.plugins import pm
from llm_fragments_pure import pure_loader


def test_pure_loader(httpx_mock):
    example_text = '# Example Title\n\nExample content.'
    httpx_mock.add_response(
        url="https://pure.md/https://example.com/",
        method="GET",
        text=example_text,
    )
    fragment = pure_loader("https://example.com/")
    assert str(fragment) == example_text
    assert fragment.source == "https://pure.md/https://example.com/"


def test_pure_loader_with_llm_key(httpx_mock):
    example_text = '# Example Title\n\nExample content.'
    httpx_mock.add_response(
        url="https://pure.md/https://example.com/",
        method="GET",
        text=example_text,
        match_headers={"x-puremd-api-token": "stored-api-key"}
    )
    
    # Mock load_keys to return stored key
    with patch('llm.load_keys', return_value={"puremd": "stored-api-key"}):
        fragment = pure_loader("https://example.com/")
        assert str(fragment) == example_text
        assert fragment.source == "https://pure.md/https://example.com/"


def test_pure_loader_with_env_fallback(httpx_mock):
    example_text = '# Example Title\n\nExample content.'
    httpx_mock.add_response(
        url="https://pure.md/https://example.com/",
        method="GET",
        text=example_text,
        match_headers={"x-puremd-api-token": "env-api-key"}
    )
    
    # Mock load_keys to return empty dict (no stored keys)
    with patch('llm.load_keys', return_value={}):
        # Mock environment variable
        with patch.dict(os.environ, {"PUREMD_API_KEY": "env-api-key"}):
            fragment = pure_loader("https://example.com/")
            assert str(fragment) == example_text
            assert fragment.source == "https://pure.md/https://example.com/"


def test_pure_loader_no_api_key(httpx_mock):
    example_text = '# Example Title\n\nExample content.'
    httpx_mock.add_response(
        url="https://pure.md/https://example.com/",
        method="GET",
        text=example_text,
    )
    
    # Mock load_keys to return empty dict and no env var
    with patch('llm.load_keys', return_value={}):
        with patch.dict(os.environ, {}, clear=True):
            fragment = pure_loader("https://example.com/")
            assert str(fragment) == example_text
            assert fragment.source == "https://pure.md/https://example.com/"


def test_pure_loader_error_response(httpx_mock):
    httpx_mock.add_response(
        url="https://pure.md/https://example.com/",
        method="GET",
        status_code=404,
    )
    
    try:
        pure_loader("https://example.com/")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Failed to load fragment" in str(e)
        assert "404" in str(e)