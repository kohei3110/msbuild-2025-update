# Notebook Collection - Azure AI Agents Practical Guide

This directory contains practical Jupyter notebooks about Azure AI Agents and multi-agent systems announced at Microsoft Build 2025.

## 📚 Notebook Overview

### 🔍 evaluate-azure-ai-agent-quality.ipynb
**Purpose**: Quality evaluation and performance measurement of Azure AI Agents

**Key Content**:
- Azure AI Foundry project client initialization
- Tourist Assistant agent creation and configuration
- Agent evaluation metrics implementation
- Quality scoring system

**Learning Points**:
- Best practices for agent evaluation
- Usage of Azure AI Evaluation library
- Real-world agent performance measurement techniques

### 🔗 multi-agent-connected-agents.ipynb
**Purpose**: Multi-agent collaboration system using Connected Agents

**Key Content**:
- Stock Price Agent (specialized in stock information) implementation
- Main Agent (integrated agent) construction
- Inter-agent communication via Connected Agent Tool
- Agent collaboration demonstration

**Learning Points**:
- Understanding Connected Agents architecture
- Separation of responsibilities design between agents
- Building modular AI systems

### 🧠 multi-agent-semantic-kernel.ipynb
**Purpose**: Multi-agent system using Semantic Kernel

**Key Content**:
- Researcher Agent (specialized in Bing search)
- Writer Agent (specialized in report creation)
- Coordinator Agent (task distribution)
- Collaborative workflow implementation

**Learning Points**:
- Utilizing Semantic Kernel framework
- Inter-agent collaboration mechanisms
- Decomposition and distributed processing of complex tasks

### 🛠️ user_functions.py
**Purpose**: Definition of custom functions used by agents

**Key Content**:
- Current time retrieval function
- Weather information retrieval function (mock)
- Other utility functions

## 📁 Directory Structure

```
notebook/
├── evaluate-azure-ai-agent-quality.ipynb  # Agent quality evaluation
├── multi-agent-connected-agents.ipynb     # Connected Agents demo
├── multi-agent-semantic-kernel.ipynb      # Semantic Kernel multi-agent
├── user_functions.py                      # Custom function definitions
├── venv/                                  # Python virtual environment
├── __pycache__/                           # Python cache
├── README_ja.md                           # Japanese version README
└── README_en.md                           # This file (English version)
```

## 🚀 Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or VS Code
- Azure AI Foundry project
- Azure OpenAI Service access

### 2. Create Virtual Environment

```bash
cd notebook
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Required Dependencies

Required packages are installed in the first cell of each notebook:

```python
# Basic packages
!pip install azure-ai-projects azure-identity azure-ai-evaluation
!pip install azure-ai-inference azure-ai-agents semantic-kernel
```

### 4. Environment Configuration

Set the following environment variables in `../concierge-agent/.env` file:

```bash
# Azure AI Foundry Configuration
PROJECT_CONNECTION_STRING=<project-connection-string>
AGENT_MODEL_DEPLOYMENT_NAME=<model-deployment-name>
PROJECT_NAME=<project-name>
RESOURCE_GROUP_NAME=<resource-group-name>

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=<openai-endpoint>
AZURE_OPENAI_API_KEY=<api-key>
AZURE_OPENAI_API_VERSION=<api-version>

# Azure Basic Configuration
AZURE_SUBSCRIPTION_ID=<subscription-id>

# Bing Search Configuration (for Semantic Kernel notebook)
BING_CONNECTION_NAME=<bing-connection-name>
```

## 💡 Usage

### Recommended Execution Order

1. **Beginner Level**: `evaluate-azure-ai-agent-quality.ipynb`
   - Learn basic concepts of single agents
   - Understand agent evaluation methods

2. **Intermediate Level**: `multi-agent-connected-agents.ipynb`
   - Implement inter-agent communication
   - Experience Connected Agents architecture

3. **Advanced Level**: `multi-agent-semantic-kernel.ipynb`
   - Complex multi-agent systems
   - Advanced utilization of Semantic Kernel

### Execution Methods

```bash
# Open with Jupyter Notebook
jupyter notebook

# Or open with VS Code
code .
```

## 🔧 Key Features

### Agent Evaluation Features
- **Quality Metrics**: Measurement of response accuracy, relevance, and completeness
- **Performance Analysis**: Monitoring execution time and resource usage
- **A/B Testing**: Comparison of multiple agent configurations

### Connected Agents Features
- **Agent Collaboration**: Collaborative operation between specialized agents
- **Tool Integration**: Using agents as tools for other agents
- **Dynamic Routing**: Appropriate agent selection based on query content

### Semantic Kernel Features
- **Plan Execution**: Automatic decomposition and execution of complex tasks
- **Plugin Management**: Reusable functional modules
- **Memory Management**: Persistence of conversation history and state

## 📊 Evaluation Metrics

### Quality Evaluation
- **Accuracy**: Fact-checking of provided information
- **Relevance**: Appropriateness of responses to queries
- **Completeness**: Coverage of necessary information
- **Consistency**: Coherence between multiple responses

### Performance Evaluation
- **Response Time**: Agent response speed
- **Throughput**: Processing volume per unit time
- **Resource Efficiency**: CPU/memory usage optimization
- **Error Rate**: Percentage of failed requests

## 🔍 Troubleshooting

### Common Issues and Solutions

**Issue**: Cannot connect to Azure AI Foundry project
- **Solution**: Check `PROJECT_CONNECTION_STRING` configuration
- **Solution**: Verify Azure CLI authentication status (`az login`)

**Issue**: Model deployment not found
- **Solution**: Check deployment name in Azure AI Foundry portal
- **Solution**: Verify that model is properly deployed

**Issue**: Package installation errors
- **Solution**: Verify that virtual environment is activated
- **Solution**: Check Python version compatibility

**Issue**: Connected Agents communication errors
- **Solution**: Check permission settings between agents
- **Solution**: Verify network connection and firewall settings

## 🎯 Learning Objectives

### Basic Level
- Understanding basic concepts of Azure AI Agents
- Creating and configuring single agents
- Basic tool integration

### Intermediate Level
- Implementing Connected Agents architecture
- Building agent evaluation systems
- Designing collaboration between multiple agents

### Advanced Level
- Advanced multi-agent systems using Semantic Kernel
- Custom plugin development
- Designing full-scale AI applications

## 🔗 Related Links

- [Azure AI Agents Documentation](https://docs.microsoft.com/azure/ai-services/agents/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [Azure AI Foundry](https://ai.azure.com/)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service/)
- [Microsoft Build 2025](https://mybuild.microsoft.com/)

## 📄 License

This project is released under the MIT License.

## 🤝 Contributing

We welcome pull requests for notebook improvements and new examples. Please review coding conventions before contributing.

## 📞 Support

If you have any questions or issues, please feel free to reach out through the GitHub Issues page.
