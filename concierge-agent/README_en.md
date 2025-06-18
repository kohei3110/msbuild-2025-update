# Concierge Agent - Smart Hotel Concierge

A smart hotel concierge system using Azure AI Agents and Semantic Kernel. An AI agent named "Lobby Boy" provides room booking, availability checking, and semantic search functionality.

## 🏨 Overview

This project demonstrates a smart hospitality system leveraging Azure AI Agents announced at Microsoft Build 2025. It implements an intelligent concierge agent that allows users to access various hotel services through natural language interaction.

## ✨ Key Features

### 🛏️ Room Management
- **Availability Check**: Check room availability for specified dates
- **Room Booking**: Real-time room booking and inventory management
- **Semantic Search**: Natural language room search (e.g., "romantic", "eco-friendly", "workspace")

### 🍽️ Dining Services
- Restaurant reservation management
- Menu information provision

### 🕐 Time-related Services
- Current time checking
- Date-related processing

## 📁 Project Structure

```
concierge-agent/
├── main.py                    # Main application
├── generate_evaluation.py     # Evaluation script
├── requirements.txt           # Python dependencies
├── .env.sample               # Environment variables template
├── skills/                   # Skill plugins
│   ├── __init__.py
│   ├── booking_skill.py      # Booking management skill
│   ├── dining_skill.py       # Dining skill
│   ├── semantic_search_plugin.py # Semantic search
│   └── time_skill.py         # Time-related skill
├── utils/                    # Utilities
│   ├── cosmosdb_client.py    # CosmosDB connection client
│   └── seed_cosmosdb.py      # Database initialization
├── README_ja.md              # Japanese version README
└── README_en.md              # This file (English version)
```

## 🚀 Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Azure OpenAI Service access
- Azure Cosmos DB account
- Azure AI Foundry project

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Copy `.env.sample` to `.env` and configure the following values:

```bash
# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT=https://<resource-name>.openai.azure.com/
AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME=gpt-4.1
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=text-embedding-3-small
AZURE_OPENAI_API_KEY=<api-key>
AZURE_OPENAI_API_VERSION=2025-03-01-preview

# Azure Cosmos DB Configuration
COSMOS_ENDPOINT=https://<resource-name>.documents.azure.com:443/
COSMOS_KEY=<cosmosdb-key>
COSMOS_DB_NAME=hotel
COSMOS_CONTAINER_NAME=rooms

# Azure AI Foundry Configuration
AZURE_SUBSCRIPTION_ID=<subscription-id>
RESOURCE_GROUP_NAME=<resource-group-name>
```

### 4. Initialize Database

```bash
python utils/seed_cosmosdb.py
```

### 5. Run the Application

```bash
python main.py
```

## 💬 Usage

### Basic Interaction Example

```
👤 User: Is there a suite room available tomorrow?

🛠️  Tool Execution → check_availability
   Arguments → {"room_type": "suite", "date": "2025-06-19"}
✅ Tool Result check_availability (execution time: 0.34s)
   → 2 suite rooms are available on 2025-06-19. Price: $500

# ConciergeAgent: Tomorrow (June 19, 2025), we have 2 suite rooms available.
The rate is $500 per night. Please let me know if you would like to make a reservation.
```

### Semantic Search Example

```
👤 User: I'm looking for a romantic atmosphere room

🛠️  Tool Execution → semantic_room_search
   Arguments → {"query": "romantic"}
✅ Tool Result semantic_room_search (execution time: 0.52s)
   → Honeymoon Suite - Luxurious suite with balcony, includes champagne service

# ConciergeAgent: For a romantic atmosphere, I recommend the "Honeymoon Suite".
It's a luxurious suite with a balcony and includes special champagne service.
Would you like me to check availability?
```

## 🔧 Skill Details

### BookingPlugin
- `check_availability()`: Check room availability
- `confirm_booking()`: Confirm booking

### DiningPlugin
- Restaurant-related services (extensible)

### SemanticRoomSearchPlugin
- `semantic_room_search()`: Natural language room search

### TimePlugin
- `get_current_time()`: Get current time

## 📊 Evaluation System

Use `generate_evaluation.py` to run agent performance evaluation:

```bash
python generate_evaluation.py
```

### Evaluation Metrics
- **Response Accuracy**: Correctness of answers to questions
- **Tool Usage Efficiency**: Appropriate skill selection and execution
- **Response Time**: Response speed measurement
- **User Experience**: Naturalness and usefulness of conversations

## 🛠️ Customization

### Adding New Skills

1. Create a new plugin file in the `skills/` directory
2. Define functions using the `@kernel_function` decorator
3. Add the plugin to the agent in `main.py`

Example:
```python
from semantic_kernel.functions import kernel_function

class NewPlugin:
    @kernel_function(description="Description of new feature")
    def new_function(self, param: str) -> str:
        return f"Processing result: {param}"
```

### Modifying Database Schema

Edit `utils/cosmosdb_client.py` and `utils/seed_cosmosdb.py` to customize data structure.

## 🔍 Troubleshooting

### Common Issues and Solutions

**Issue**: Azure OpenAI connection error
- **Solution**: Check configuration values in `.env` file
- **Solution**: Verify Azure OpenAI service is enabled

**Issue**: Cosmos DB connection error
- **Solution**: Check Cosmos DB account access permissions
- **Solution**: Verify network settings and firewall rules

**Issue**: Skills not executing
- **Solution**: Check agent `instructions`
- **Solution**: Verify function `description` is properly set

**Issue**: Low semantic search accuracy
- **Solution**: Check embedding model configuration
- **Solution**: Improve search queries

## 📚 Technology Stack

- **Azure AI Agents**: Agent framework
- **Semantic Kernel**: AI orchestration
- **Azure OpenAI Service**: Language model and embeddings
- **Azure Cosmos DB**: NoSQL database
- **Python**: Programming language
- **FastAPI**: Web API framework (optional)

## 🔗 Related Links

- [Azure AI Agents Documentation](https://docs.microsoft.com/azure/ai-services/agents/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [Azure OpenAI Service](https://azure.microsoft.com/products/ai-services/openai-service/)
- [Azure Cosmos DB](https://azure.microsoft.com/products/cosmos-db/)
- [Microsoft Build 2025](https://mybuild.microsoft.com/)

## 📄 License

This project is released under the MIT License.

## 🤝 Contributing

Pull requests and issue reports are welcome. Please review coding conventions and project guidelines before contributing.

## 📞 Support

If you have any questions or issues, please feel free to reach out through the GitHub Issues page.
