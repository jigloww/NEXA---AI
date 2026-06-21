# NEXA AI Architecture

## High Level Architecture

Telegram User
      │
      ▼
 Telegram Bot
      │
      ▼
  Master Agent
      │
 ┌────┼──────────────┬─────────────┬─────────────┬─────────────┐
 ▼    ▼              ▼             ▼             ▼             ▼

Memory Academic Productivity Business Investment Knowledge
Agent   Agent      Agent        Agent     Agent     Base

      │
      ▼

   Database
(PostgreSQL)

      │
      ▼

 Memory Store
 (ChromaDB)

      │
      ▼

 External Tools
 ├── PDF Reader
 ├── Excel Reader
 ├── Scheduler
 ├── Market Analyzer
 ├── Business Analyzer
 └── Web Search
 