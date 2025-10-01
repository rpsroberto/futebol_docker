# Usar uma imagem oficial do Python
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos
COPY app/ /app/

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta da aplicação
EXPOSE 5000

# Rodar a aplicação
CMD ["python", "app.py"]
