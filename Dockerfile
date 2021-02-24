FROM python:slim
RUN ["apt", "update"]
RUN ["apt", "install", "-y", "--no-install-recommends", "wget", "ca-certificates"]
RUN ["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"]
RUN ["apt", "install", "-y", "--no-install-recommends", "./google-chrome-stable_current_amd64.deb"]
COPY main.py /usr/local/src/
WORKDIR /usr/local/src
RUN ["pip", "install", "selenium", "chromedriver-binary-auto"]
RUN ["sed", "1s/^/import chromedriver_binary\n/" "main.py"]
ENTRYPOINT ["python", "main.py"]
