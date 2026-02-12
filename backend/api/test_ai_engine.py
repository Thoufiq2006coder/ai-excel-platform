from backend.ai_engine import analyze_data

dummy_data = [
    {"date": "2025-01-01", "sales": 1000, "profit": 200},
    {"date": "2025-01-02", "sales": 1200, "profit": 250},
    {"date": "2025-01-03", "sales": 900, "profit": 150}
]

result = analyze_data(dummy_data)

print(result)
