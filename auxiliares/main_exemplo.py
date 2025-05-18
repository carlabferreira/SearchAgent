'''
Aluna: Carla Beatriz Ferreira
Disciplina: Introdução a Inteligência Artificial
Data: 20-04-2025
Descrição: xxx

'''

from smolagents import CodeAgent, LiteLLMModel, Tool, InferenceClientModel, FinalAnswerTool

class FindRoutTool(Tool):
    name = "find_route"
    description = """
    This tool must be used when you want to find the route or path between two places, locations or points
    """
    inputs = {
        "source": {
            "type": "string",
            "description": "The source location. It can be an address, a place, a street name, etc.",
        },
        "target": {
            "type": "string",
            "description": "The target location. It can be an address, a place, a street name, etc.",
        },
    }
    output_type = "string"

    def forward(self, source, target):
        return f"The sortest route from {source} to {target} is ..." #chamar a função de rota aqui
    
model = LiteLLMModel(
    model_id="ollama_chat/qwen3:8b",  # alterado
    api_base="http://localhost:11434",  # Default Ollama local server
    num_ctx=8192,
)

agent = CodeAgent(tools=[FindRoutTool()], model=model, add_base_tools=False)
agent.run("How can I go from Margô Drinkeria to Berilo Cozinha & Drinks?") #prompt a ser alterado para exemplos

'''
alterações possíveis:
- Mudar para aceitar apenas endereços
- Exibir o caminho informado a partir dos nomes das ruas
- exibir a distância entre os pontos
- colocar uma ferramenta para verificar erros de digitação antes de rodar o código
- colocar uma ferramenta para verificar se o ponto existe
'''