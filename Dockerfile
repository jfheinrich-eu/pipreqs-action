FROM jfheinrich/pipreqs-action:latest AS builder

ENV PATH="/opt/git/bin:${PATH}"
ENV LD_LIBRARY_PATH="/opt/git/lib"
ENV PYTHONPATH=/app
ENTRYPOINT ["/app/app.py"]
