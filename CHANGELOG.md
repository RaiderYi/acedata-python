# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-03

### Added
- Core client (`AceDataClient`) with chat / image / music / video / embeddings support
- OpenAI SDK compatibility mode (`openai_base_url` property)
- Streaming chat support (`chat_stream`)
- Auto-retry with exponential backoff (configurable `max_retries`)
- Authentication & rate-limit error handling
- Balance query and model listing utilities
- 5 example scripts (chat, image, music, video, OpenAI compatible)
- Full test suite (13 tests, 100% pass rate)
- GitHub Actions CI (Python 3.9–3.12)
- Bilingual README (Chinese + English)
- MIT License
