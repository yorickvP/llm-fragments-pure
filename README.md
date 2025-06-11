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

You can provide your pure.md API token in two ways:

### Option 1: Using LLM keys (recommended)

```bash
llm keys set puremd
# Enter your API key when prompted
llm -f 'pure:https://example.com' "Summarize this page"
```

### Option 2: Environment variable

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