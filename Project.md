# Calcula Vet — contexto do projeto

## Nome e propósito

- **Repositório:** `Calcula_Vet` (nome relacionado ao pacote **calcula-vet-web** no README).
- **Objetivo:** calculadora de doses para uso veterinário, com base no **Guia Terapêutico Veterinário, 4ª edição** (referência citada na interface do programa).
- **Escopo atual:** script de linha de comando em Python que pergunta princípio ativo, peso e, quando aplicável, espécie ou tipo de caso, e imprime a dose e orientações de administração.

## Stack e ambiente

- **Linguagem:** Python 3.
- **Entrada:** `input()` no terminal; vírgulas em números são normalizadas para ponto.
- **Normalização de texto:** acentos removidos via `unicodedata` para comparar nomes de fármacos e todos caracteres convertidos em letras minúsculas.

## Estrutura do repositório

| Caminho                             | Função                                                                                    |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| `main.py`                           | Lógica principal: validação do fármaco, cálculos e mensagens ao usuário.                  |
| `test_main.py`                      | Testes automatizados (unitários de fórmula e integração com entrada simulada por fármaco).|
| `README.md`                         | Visão geral, objetivo, tecnologias e status.                                              |
| `Project.md`, `Memory.md`           | Contexto persistente para humanos e agente (ver regra em `.cursor/rules/`).               |
| `Plan.md`                           | Roadmap e melhorias futuras; dívida técnica e fases sugeridas.                            |
| `.cursor/rules/project-context.mdc` | Regra Cursor: manter `Project.md` / `Memory.md` alinhados ao trabalho.                    |

## Princípios ativos suportados (`main.py`)

Lista validada no código (sinônimos divididos por barra, onde existem):

- amoxicilina  
- dipirona  
- doxiciclina  
- enrofloxacina / enrofloxacino  
- maropitant / maropitante  
- meloxicam  
- metronidazol  
- omeprazol  
- prednisolona  

## Manutenção deste arquivo

- Atualizar conforme mudanças no `README.md`, na estrutura de pastas, na lista de fármacos ou referências oficiais.
- Detalhes de sessões e decisões pontuais ficam em `Memory.md`.
