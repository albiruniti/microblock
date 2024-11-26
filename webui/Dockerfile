FROM debian:12-slim

SHELL ["/bin/bash", "-c"]

RUN apt update && apt upgrade && apt install -y \
	python3 python3-pip

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ["entrypoint.sh"]