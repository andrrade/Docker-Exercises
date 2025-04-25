FROM python:3.12.10-alpine3.21
  
RUN addgroup -S groupTeste && \
    adduser -S -G groupTeste -h /app userTeste && \
    mkdir -p /app && \
    chown userTeste:groupTeste /app

WORKDIR /app

COPY --chown=userTeste:groupTeste exe10.py .
RUN chmod 744 exe10.py

USER userTeste

CMD ["python", "exe10.py"]