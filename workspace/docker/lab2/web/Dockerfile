FROM python:3.11-alpine

RUN apk update \
&& apk add git \
&& git config --global user.name "humanda" \
&& git config --global user.email "humanda@example.com" \
# && apk add --no-cache gcc musl-dev python3-dev build-base \
&& pip install numpy pandas matplotlib openai flask

WORKDIR /work

RUN git clone https://github.com/shared-repo/human-da.git \
&& cp -r ./human-da/workspace/webapps/chatbotweb2 .

EXPOSE 5000



CMD ["flask", "--app", "chatbotweb2", "--debug", "run", "--host=0.0.0.0"]

