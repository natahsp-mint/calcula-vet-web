# Plano de evolução — Calcula Vet

Documento de referência para **melhorias futuras** e **dívida técnica** identificada na análise do repositório (principalmente `main.py` e `README.md`). Prioridades são sugestões; ajustar conforme tempo e uso real.

---

## 1. Estado atual (resumo)

| Aspecto | Situação                                                                                         |
|---------|--------------------------------------------------------------------------------------------------|
|Interface| CLI única (`input` / `print`); mensagem de boas-vindas diz “Web”, mas não há aplicação web ainda.|
|  Dados  | Doses e textos embutidos no código; referência: Guia Terapêutico Veterinário 4ªed.               |
| Fármacos| 9 entradas lógicas (com sinônimos); fluxos por espécie/caso onde aplicável.                      |
|  README | Menciona “apresentações comerciais” e variáveis — ainda não refletido no código.                 9|

---

## 2. Correções e robustez (curto prazo)

- [DONE] **Entrada numérica:** Tratar `ValueError` quando peso ou mg/kg não forem números válidos; opcionalmente limitar tentativas ou mensagem clara.
- [DONE] **Nome reservado:** Evitar sombrear `input` do builtins (usar outro nome para a função que normaliza vírgula). 
- [DONE] **Prednisolona:** Corrigir string do prompt da espécie (parêntese/colon consistente) e revisar o fluxo do `while True` para que espécie/caso sejam coletados de forma clara quando a combinação for inválida (hoje parte da lógica pode confundir reentrada).
- [DONE] **Testes automatizados:** Testes unitários para fórmulas (peso × mg/kg) e, se possível, testes de integração com entrada simulada para cada fármaco.

---

## 3. Alinhamento com o README (médio prazo)

- **Apresentações comerciais:** Modelar concentrações (mg/ml, mg/comprimido) e calcular **volume ou fração de comprimido** além da dose em mg, com escolha de apresentação.
- **Mais variáveis:** Campos como espécies adicionais, idade, insuficiência renal/hepática — apenas com base em referências explícitas no guia e sempre com aviso de que é apoio, não substitui julgamento clínico.
- **Sincronizar nome do produto:** Ou renomear mensagens para “Calcula Vet” até existir web, ou planear entrega web e manter o branding coerente.
- Integração com bases de dados de bulário pago ou APIs terceiras — avaliar legalidade e termos de uso antes.

---

## 4. Interface “Web” (médio / longo prazo)

O nome **calcula-vet-web** e o texto de boas-vindas sugerem evolução para web.

- **Opções típicas:** SPA leve (HTML/JS) com lógica no cliente; ou framework Python (FastAPI/Flask) com templates; ou static site + WASM se a lógica for portada.
- **Requisitos:** Layout responsivo, acessibilidade básica, mesma base de dados de doses (idealmente extraída para JSON/YAML).
- **Implantação:** GitHub Pages, VPS ou container — definir mais tarde.

---

## 5. Arquitetura de dados e manutenção

- **Externalizar regras:** Mover doses, intervalos e textos para `data/` (JSON/YAML) carregado no arranque, com schema simples documentado.
- **Camada pura de cálculo:** Funções que recebem `(drug_id, weight, options)` e devolvem `(dose_mg, labels)` separadas de I/O, facilitando testes e eventual API.
- **Internacionalização:** Se houver versão em inglês ou outros idiomas, separar strings dos números.

---

## 6. Qualidade, empacotamento e colaboração

- **`requirements.txt` ou `pyproject.toml`:** Fixar versão mínima do Python e dependências (mesmo que zero por agora).
- **Lint/format:** `ruff` / `black` / `mypy` opcional para consistência.
- **Licença e aviso legal:** Texto curto de que o software é ferramenta de apoio e não substitui prescrição veterinária nem o guia oficial atualizado.
- **CI:** Pipeline simples (ex.: GitHub Actions) a correr testes em push.

---

## 7. Roadmap sugerido (fases)

| Fase | Foco                                                                       |
|------|----------------------------------------------------------------------------|
| **A**| Correções de robustez, refatoração de fluxo, testes nas fórmulas críticas. |
| **B**| Dados externos + funções de cálculo puras; CLI usando essa camada.         |
| **C**| Apresentações comerciais e variáveis adicionais alinhadas ao README.       |
| **D**| Interface web + deploy; aviso legal visível.                               |

---

*Última revisão do documento: alinhada ao código e README na data da criação do ficheiro; atualizar `Project.md` / `Memory.md` quando fases forem concluídas ou repriorizadas.*

CHECKLIST (By Natahsp-mint):
[] adcionar função "Restart" para user restartar código a qualquer momento.
