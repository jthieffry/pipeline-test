# How to initialize a CDK project with uv:
```
mkdir project
cd project
cdk init app --language python
rm -Rf .venv
uv init -p 3.12
uv add -r requirements.txt
uv add --dev -r -requirements-dev.txt
rm requirements.txt requirements-dev.txt
```
Then, modify cdk.json, and change:
```
app: uv run ./app.py
```

