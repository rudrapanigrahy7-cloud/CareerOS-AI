# CareerOS AI - MCP Architecture

## Overview

CareerOS AI uses Model Context Protocol (MCP) servers to connect agents with external tools and information sources.

The MCP layer provides a standardized interface between agents and tools.

---

# MCP Server 1: Filesystem / Document MCP

## Purpose

Allow agents to access and analyze uploaded documents.

## Used By

Research-to-Project Agent

Internship Agent

## Supported Files

* PDF
* TXT
* Markdown

## Example Use Cases

* Analyze research papers
* Read resumes
* Extract project information

---

# MCP Server 2: Search MCP

## Purpose

Provide access to web-based information.

## Used By

Hackathon Agent

Scholarship Agent

Career Strategist Agent

## Example Use Cases

* Discover hackathons
* Find scholarship opportunities
* Research learning resources

---

# MCP Server 3: GitHub MCP

## Purpose

Access public GitHub repositories.

## Used By

Research-to-Project Agent

Career Strategist Agent

## Example Use Cases

* Analyze repositories
* Suggest open-source projects
* Review project structures

---

# MCP Security Rules

Only approved MCP servers may be used.

Allowed MCP Servers:

* Filesystem MCP
* Search MCP
* GitHub MCP

All MCP requests must be logged.

---

# MCP Benefits

* Modular architecture
* Tool interoperability
* Easy future expansion
* Consistent agent-tool communication