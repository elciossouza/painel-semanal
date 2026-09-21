import os, httpx, json
from app.google_ads import get_access_token
CID="3194533452"
tok=get_access_token(os.getenv("GOOGLE_ADS_REFRESH_TOKEN",""))
h={"Authorization":f"Bearer {tok}","developer-token":os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN",""),"Content-Type":"application/json"}
lg=os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID","").replace("-","")
if lg: h["login-customer-id"]=lg
r=httpx.post(f"https://googleads.googleapis.com/v24/customers/{CID}/googleAds:search",headers=h,
  json={"query":"""select segments.week, metrics.cost_micros, metrics.conversions,
                          metrics.cost_per_conversion, metrics.clicks, metrics.impressions,
                          metrics.average_cpc
                   from customer
                   where segments.date between '2026-05-25' and '2026-09-21'"""},timeout=90)
if r.status_code!=200:
    print("ERRO", r.status_code, r.text[:300]); raise SystemExit
linhas=[]
for x in r.json().get("results",[]):
    s=x["segments"]; m=x["metrics"]
    linhas.append({
      "semana": s.get("week"),
      "custo": round(int(m.get("costMicros",0))/1e6, 2),
      "conversoes": round(float(m.get("conversions",0)), 1),
      "cpa": round(int(m.get("costPerConversion",0))/1e6, 2),
      "cpc": round(int(m.get("averageCpc",0))/1e6, 2),
      "cliques": int(m.get("clicks",0)),
      "impressoes": int(m.get("impressions",0)),
    })
linhas.sort(key=lambda l: l["semana"])
saida={"conta": CID, "nome":"Cosmetica Farmácia de Manipulação",
       "moeda":"BRL", "semanas": linhas}
print("<<<JSON>>>")
print(json.dumps(saida, ensure_ascii=False, indent=1))
