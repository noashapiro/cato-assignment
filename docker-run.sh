#!/bin/bash

echo "Building Docker image..."
docker build -t cato-tests .

echo "Running tests in Docker container..."
docker run --rm cato-tests

