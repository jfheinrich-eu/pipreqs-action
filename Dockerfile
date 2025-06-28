FROM jfheinrich/pipreqs-action:latest AS builder

ADD . /project
WORKDIR /project

RUN mkdir /app && \
    cp -a src/ /app && \
    python -m pip install --no-cache-dir --target /app . && \
    chmod 755 /app/app.py

FROM jfheinrich/pipreqs-action:latest AS final
COPY --from=builder /app /app
ENV PYTHONPATH=/app
ENTRYPOINT ["/app/app.py"]
