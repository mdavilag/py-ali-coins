# 🪙 py-ali-coins

Automação com Selenium para coletar moedas diárias no AliExpress usando um perfil do Chrome já logado. Envia notificações via Pushover e gera log em arquivo.

## ✅ Requisitos

- Python
- Google Chrome + ChromeDriver
- Conta no Pushover
- Perfil do Chrome já logado no AliExpress

## ⚙️ Instalação

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` com:

```
USER_TOKEN=seu_user_token (pushover)
APP_TOKEN=seu_app_token (pushover)
```

No `script.py`, configure o perfil do Chrome:

```python
chrome_options.add_argument("--user-data-dir=C:\\Users\\SeuUsuario\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("--profile-directory=Default")  # ou "Profile 1", etc.
```

## 🚀 Execução

```bash
python script.py
```

Ou, no Windows:

```bash
run.bat
```

## 🔔 Notificações

O status da execução é enviado via [Pushover](https://pushover.net).

## 📝 Logs

O log é salvo no arquivo `log.txt`.

## ⏰ Agendamento

- **Windows**: use o Agendador de Tarefas com o `run.bat`

