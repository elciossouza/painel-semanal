# Painel semanal — marketing e vendas

Página estática que lê uma planilha pública do Google Sheets e desenha o painel
no navegador. Não há servidor: o `index.html` busca o CSV direto da planilha.

- **Fonte:** Google Sheets, compartilhado como "qualquer pessoa com o link pode ver"
- **Atualização:** automática a cada carregamento da página
- **Dependência:** Plotly 3.0.1 (CDN)

Para trocar a planilha, edite `PLANILHA` e `GID` no topo do `<script>`.
