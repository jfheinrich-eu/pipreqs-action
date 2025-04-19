FROM python:3.13.3-alpine3.21
ADD . /app
WORKDIR /app

# Install development dependencies
RUN apk add --no-cache python3 py3-pip

# Install pipreqs
RUN pip3 install pipreqs

# Copy requirements file if it exists
COPY requirements.txt* ./

# Install project dependencies
RUN if [ -f requirements.txt ]; then pip3 install --user --target /app -r requirements.txt; fi

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3-debian10
COPY --from=builder /app /app
WORKDIR /app
ENV PYTHONPATH=/app
CMD ["/app/main.py"]
