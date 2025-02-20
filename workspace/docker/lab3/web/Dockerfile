FROM python:3.11-bookworm

RUN apt update \
&& git config --global user.name "humanda" \
&& git config --global user.email "humanda@example.com" \
&& pip install numpy pandas matplotlib \
&& pip install pymysql cryptography \
&& pip install openai flask flask-wtf \
&& pip install tensorflow \
# && pip install torch torchvision torchaudio \
&& pip install chromadb

EXPOSE 5000

WORKDIR /work

RUN git clone https://github.com/shared-repo/human-da.git \
&& cp -r ./human-da/workspace/webapps/demoweb2 .



CMD ["flask", "--app", "demoweb2", "--debug", "run", "--host=0.0.0.0"]

