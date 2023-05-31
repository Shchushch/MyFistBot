FROM python:3.7-slim-stretch
ENV TOKEN='6152131089:AAFns80mTSJbaBVQR9lAR4QVPtYvXP8hKqE'
COPY . .
RUN pip install -r requirments.txt
CMD python bot.py