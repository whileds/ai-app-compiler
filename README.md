# OneAtlas AI Generation Pipeline

AI-powered multi-stage application generation pipeline.

## Overview

This system converts natural language prompts into structured application specifications.

Pipeline stages:

1. Intent Extraction
2. Schema Generation
3. AppSpec Generation
4. Validation Layer
5. Repair Engine

The system generates:
- entities
- database schema
- pages
- API endpoints
- auth rules
- workflow stubs
- integration hooks

---

## Features

- Multi-stage pipeline architecture
- Validation engine
- Automatic repair engine
- Integration registry
- Workflow stub generation
- Cost tracking
- Latency tracking

---

## Supported Integrations

- Slack
- WhatsApp
- Gmail
- Stripe
- Jira

---

## API Endpoints


### Generate AppSpec

POST `/api/generate`

Example:

```json
{
  "prompt": "Build CRM with whatsapp notifications"
}
