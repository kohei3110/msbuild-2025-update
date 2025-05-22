# TypeScript Development Environment

This repository demonstrates a TypeScript development environment setup for GitHub Copilot Coding Agent.

## GitHub Actions Workflow

The repository includes a GitHub Actions workflow that automatically sets up a TypeScript development environment. The workflow:

1. Sets up Node.js
2. Installs TypeScript and development dependencies
3. Configures TypeScript settings
4. Sets up ESLint for linting
5. Creates and runs a sample TypeScript file to verify the setup

## Local Development

To set up the development environment locally:

```bash
# Install dependencies
npm install

# Build the TypeScript project
npm run build

# Run the application
npm start

# Run linting
npm run lint
```

## Project Structure

- `src/` - Source code directory
- `dist/` - Compiled JavaScript output
- `.github/workflows/` - GitHub Actions workflows