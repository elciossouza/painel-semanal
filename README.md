# Painel semanal — marketing e vendas

Página estática que lê uma planilha pública do Google Sheets e desenha o painel
no navegador. Não há servidor: o `index.html` busca o CSV direto da planilha.

- **Fonte:** Google Sheets, compartilhado como "qualquer pessoa com o link pode ver"
- **Atualização:** automática a cada carregamento da página
- **Dependência:** Plotly 3.0.1 (CDN)

Para trocar a planilha, edite `PLANILHA` e `GID` no topo do `<script>`.

## Google Ads

`ads.json` traz investimento, conversões e custo por conversão direto da API da
conta, por semana. A página é estática e não pode chamar a API (exigiria o
refresh token e o developer token num repositório público), então o arquivo é
gerado por `scripts/atualizar_ads.py` — que roda onde as credenciais existem —
e versionado junto.

Para atualizar: rode o script e faça commit do `ads.json`.
