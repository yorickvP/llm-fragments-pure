# llm-fragments-pure

Run URLs through the [pure.md](https://pure.md/) API to convert web pages to clean Markdown.

## Installation

```bash
llm install llm-fragments-pure
```

## Usage

```bash
llm -f 'pure:https://example.com' "Summarize this page"
```

## API Key

Set the `PUREMD_API_KEY` environment variable to use your pure.md API token:

```bash
export PUREMD_API_KEY=your_api_key_here
llm -f 'pure:https://example.com' "Summarize this page"
```

## Development

```bash
cd llm-fragments-pure
python -m venv venv
source venv/bin/activate
python -m pip install -e '.[test]'
```