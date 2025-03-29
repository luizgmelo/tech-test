# Web Scraping ANS - Anexos

Script para automatizar o download dos Anexos I e II do Rol de Procedimentos da ANS.

## Pré-requisitos

- Python
- pip

## Configuração

1. Clone o repositório
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Execute o script principal:
```bash
python ans_scraper.py
```

O script irá:
1. Acessar o site da ANS
2. Baixar os Anexos I e II em PDF
3. Compactar em um arquivo ZIP chamado `anexos_ans.zip`

## Estrutura de Arquivos

- `ans_scraper.py` - Script principal
- `requirements.txt` - Dependências do projeto
- `README.md` - Esta documentação
