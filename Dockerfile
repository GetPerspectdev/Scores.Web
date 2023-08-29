FROM python:3.10-bookworm

ENV CMAKE_ARGS="-DLLAMA_OPENBLAS=on"
ENV FORCE_CMAKE=1
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install llama-cpp-python
RUN pip install -r requirements.txt
COPY ./data ./data
COPY ./models ./models
COPY ./tokenizer ./tokenizer
COPY . .
EXPOSE 5050
RUN ls -al
CMD ["python", "main.py"]