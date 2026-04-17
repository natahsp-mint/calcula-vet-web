# Calcula Vet — memória de trabalho

Este arquivo guarda **preferências, decisões e histórico recente** das interações para orientar continuidade no Cursor. O estado “oficial” do código e do escopo está em `Project.md`.

## Como usar

- **Eu (assistente):** após mudanças relevantes no projeto ou pedidos explícitos, atualizo `Memory.md` e, quando couber, `Project.md`.
- **Você:** pode pedir “atualize o memory com X” ou corrigir qualquer ponto desatualizado.

---

## Preferências e convenções (da conversa)

- Documentação de contexto pedida em **português**: arquivos `Memory.md` e `Project.md` na raiz do repositório.
- Manter estes arquivos **sincronizados** com o repositório e com as interações, sem substituir o README salvo pedido explícito.
- Regra Cursor **sempre ativa**: `.cursor/rules/project-context.mdc` — orienta ler/atualizar `Project.md` e `Memory.md` conforme o trabalho.

---

## Histórico (linha do tempo)

| Data       | Nota |
|------------|------|
| 2026-04-16 | Criação de `Project.md` e `Memory.md` com base em `main.py` e `README.md`. Pedido: contexto persistente e atualização contínua conforme interações. |
| 2026-04-16 | Confirmação: adicionada regra `.cursor/rules/project-context.mdc` (`alwaysApply: true`). |
| 2026-04-16 | Criado `Plan.md` com análise do projeto, dívida técnica e roadmap por fases (A–D). |
| 2026-04-17 | Renomeado padrão de nomes para `Project.md` e `Memory.md`. |
| 2026-04-17 | Implementada validação de faixas mg/kg em `main.py` com `get_dosage_in_range` para amoxicilina, enrofloxacina (cão), omeprazol e prednisolona (casos com faixa). |
| 2026-04-17 | Refatorado fluxo de controle em `main.py` para cadeia única `if/elif/else` por fármaco, removendo blocos `if` soltos. |
| 2026-04-17 | Correção de nome reservado: removido sombreado de `input` em `main.py`; criada `normalized_input()` para números e uso explícito de `builtins.input` nos campos textuais/menus. |
| 2026-04-17 | Ajustado fluxo de `prednisolona`: prompts padronizados e recolha de espécie/caso movida para dentro do `while`, repetindo a seleção em combinações inválidas. |
| 2026-04-17 | Adicionados testes automatizados em `test_main.py`: 3 unitários (`calculate_dose_mg`) + 9 integrações com entrada simulada (um fluxo por fármaco). |

---

## Backlog / ideias (não implementadas)

- (vazio — preencher quando surgirem)

---

## Observações técnicas rápidas (para retomada)

- Entrada numérica aceita vírgula como separador decimal via `normalized_input()` em `main.py`.
- Fluxo principal está em cadeia `if/elif/else` dentro de `run_cli()`, com guarda `if __name__ == "__main__"` para permitir import em testes.
