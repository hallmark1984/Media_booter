FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Environment defaults for the loop
ENV SUBREDDIT="python"
ENV INTERVAL_MINS="10"

RUN echo '#!/bin/bash\n\
python manage.py migrate\n\
while true; do\n\
  python manage.py scrape reddit $SUBREDDIT $INTERVAL_MINS\n\
  python manage.py scrape bbc world $INTERVAL_MINS\n\
  echo "Sleeping $INTERVAL_MINS mins..."\n\
  sleep $(($INTERVAL_MINS * 60))\n\
done' > /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
