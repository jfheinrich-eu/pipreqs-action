FROM python:3.13.3-alpine3.21 AS builder

ADD ./src /app
RUN rm -rf /app/__pycache__ && \
    rm -rf /app/.pytest_cache && \
    pip3 install --target /app pipreqs && \
    chmod 755 /app/main.py

# Install project dependencies
RUN if [ -f /app/requirements.txt ]; then pip3 install --target /app -r /app/requirements.txt; fi

FROM python:3.13.3-alpine3.21 AS final
COPY --from=builder /app /app
ENV PYTHONPATH=/app

ENTRYPOINT ["/app/main.py"]
