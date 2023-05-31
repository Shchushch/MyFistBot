FROM python:3.11-slim
ENV TOKEN='6152131089:AAFns80mTSJbaBVQR9lAR4QVPtYvXP8hKqE'
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]
