# Calcula Vet — contexto do projeto

## Nome e propósito

- **Repositório:** `Calcula_Vet` (nome relacionado ao pacote **calcula-vet-web** no README).
- **Objetivo:** calculadora de doses para uso veterinário, com base no **Guia Terapêutico Veterinário, 4ª edição** (referência citada na interface do programa).
- **Escopo atual:** script de linha de comando em Python que pergunta princípio ativo, peso e, quando aplicável, espécie ou tipo de caso, e imprime a dose e orientações de administração.

## Stack e ambiente

- **Linguagem:** Python 3.
- **Entrada:** `input()` no terminal; vírgulas em números são normalizadas para ponto.
- **Normalização de texto:** acentos removidos via `unicodedata` para comparar nomes de fármacos.

## Estrutura do repositório

| Caminho    | Função |
|-----------|--------|
| `main.py` | Lógica principal: validação do fármaco, cálculos e mensagens ao usuário. |
| `test_main.py` | Testes automatizados (unitários de fórmula e integração com entrada simulada por fármaco). |
| `README.md` | Visão geral, objetivo, tecnologias e status. |
| `Project.md`, `Memory.md` | Contexto persistente para humanos e agente (ver regra em `.cursor/rules/`). |
| `Plan.md` | Roadmap e melhorias futuras; dívida técnica e fases sugeridas. |
| `.cursor/rules/project-context.mdc` | Regra Cursor: manter `Project.md` / `Memory.md` alinhados ao trabalho. |

## Princípios ativos suportados (`main.py`)

Lista validada no código (sinônimos entre parênteses onde existem):

- amoxicilina  
- dipirona  
- doxiciclina  
- enrofloxacina / enrofloxacino  
- maropitant / maropitante  
- meloxicam  
- metronidazol  
- omeprazol  
- prednisolona  

## Comportamento resumido por fármaco

- **Amoxicilina:** dosagem em mg/kg (faixa 10–20) informada pelo usuário.  
- **Dipirona, doxiciclina:** dose fixa por peso (fórmulas no código).  
- **Enrofloxacina:** ramificação cão (5–10 mg/kg) vs gato (dose fixa).  
- **Maropitant:** dose ligada ao peso; mensagem SC/VO SID.  
- **Meloxicam:** cão vs gato com esquemas de ataque e manutenção.  
- **Metronidazol:** giardíase vs anaeróbicos.  
- **Omeprazol:** mg/kg (0,5–1).  
- **Prednisolona:** espécie (cão/gato) e caso (alergia, imunossupressão, uso prolongado), com faixas no código.

## Status (README)

- Projeto em **desenvolvimento**; README menciona intenção futura de considerar apresentações comerciais e mais variáveis.

## Manutenção deste arquivo

- Atualizar quando mudar objetivo do produto, estrutura de pastas, lista de fármacos ou referências oficiais.
- Detalhes de sessões e decisões pontuais ficam em `Memory.md`.
