FROM python:latest
COPY bot.py .
RUN pip3 install python-telegram-bot --upgrade
ENTRYPOINT [ "python3" ]
CMD ["bot.py"] 
