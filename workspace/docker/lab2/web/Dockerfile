FROM python:3.11-alpine

RUN apk update -y
RUN apk add git
RUN git config --global user.name "humanda"
RUN git config --global user.email "humanda@example.com"

RUN apk add --no-cache gcc musl-dev python3-dev build-base

RUN pip install numpy pandas matplotlib openai flask

WORKDIR /work

RUN git clone https://github.com/shared-repo/human-da.git
RUN cp -r ./human-da/workspace/webapps/chatbotweb .

CMD ["flask", "--app chatbotweb", "--debug", "run"]

