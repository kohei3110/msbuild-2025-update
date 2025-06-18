# GitHub Actions Workflows

This directory contains GitHub Actions workflows for the Microsoft Build 2025 Update sample project.

## 📁 Directory Structure

```
.github/
├── workflows/
│   ├── copilot-setup-steps.yml      # GitHub Copilot setup workflow
│   ├── eval-single-agent-fail.yml   # Agent evaluation (failure case)
│   ├── eval-single-agent-success.yml # Agent evaluation (success case)
│   └── evals/                       # Evaluation scripts
├── README_ja.md                     # Japanese version README
└── README_en.md                     # This file (English version)
```

## 🔧 Workflow Descriptions

### 1. Copilot Setup Steps (`copilot-setup-steps.yml`)

**Purpose**: Automate GitHub Copilot environment setup

**Trigger**: Manual execution (`workflow_dispatch`)

**Key Features**:
- Setup procedures execution on Ubuntu environment
- Repository checkout
- Required permissions setup (`contents: read`)

**Usage**:
1. Navigate to the "Actions" tab in your GitHub repository
2. Select the "Copilot Setup Steps" workflow
3. Click the "Run workflow" button

### 2. Agent Evaluation - Fail Case (`eval-single-agent-fail.yml`)

**Purpose**: Evaluation testing of AI agents in failure scenarios

**Trigger**: Manual execution (`workflow_dispatch`)

**Key Features**:
- Python 3.11 environment setup
- Azure AI evaluation library installation
- Agent performance evaluation in failure cases

**Required Environment Variables**:
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_API_VERSION`
- `AZURE_SUBSCRIPTION_ID`

### 3. Agent Evaluation - Success Case (`eval-single-agent-success.yml`)

**Purpose**: Evaluation testing of AI agents in success scenarios

**Trigger**: Manual execution (`workflow_dispatch`)

**Key Features**:
- Python 3.11 environment setup
- Azure AI evaluation library installation
- Agent performance evaluation in success cases

**Required Environment Variables**: Same as failure case

## 🚀 Setup Instructions

### 1. Prerequisites

- Azure OpenAI Service access
- Azure subscription
- Required secrets configuration

### 2. Secrets Configuration

Add the following secrets in your GitHub repository settings:

```
AZURE_OPENAI_ENDPOINT=<your-azure-openai-endpoint>
AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME=<deployment-name>
AZURE_OPENAI_API_KEY=<api-key>
AZURE_OPENAI_API_VERSION=<api-version>
AZURE_SUBSCRIPTION_ID=<subscription-id>
```

### 3. Running Workflows

1. Access your GitHub repository
2. Select the "Actions" tab
3. Choose the workflow you want to run
4. Click "Run workflow"

## 📊 Viewing Evaluation Results

After running agent evaluation workflows, you can check results through:

1. **GitHub Actions Logs**: Detailed execution logs
2. **Evaluation Metrics**: Performance indicators from Azure AI Evaluation
3. **Success/Failure Reports**: Results for each test case

## 🔍 Troubleshooting

### Common Issues and Solutions

**Issue**: Workflow fails to execute
- **Solution**: Verify that secrets are correctly configured
- **Solution**: Ensure Azure OpenAI Service is enabled

**Issue**: Evaluation scripts not found
- **Solution**: Verify that the `evals/` directory exists
- **Solution**: Check that working directory is correctly set

**Issue**: Python dependency installation errors
- **Solution**: Check dependencies in `requirements.txt`
- **Solution**: Verify Python version compatibility

## 📝 Customization

### Adding New Workflows

1. Create a new YAML file in `.github/workflows/` directory
2. Define appropriate triggers and jobs
3. Add necessary secrets if required

### Modifying Existing Workflows

1. Edit the target YAML file
2. Test with test execution
3. Verify operation in production environment

## 🔗 Related Links

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Azure AI Services](https://azure.microsoft.com/en-us/products/ai-services/)
- [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)
- [Microsoft Build 2025](https://mybuild.microsoft.com/)

## 📞 Support

If you have any questions or issues, please feel free to reach out through the GitHub Issues page.
