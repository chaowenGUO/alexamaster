FROM openjdk:slim
ENV DEBUG pw:api
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD 1
RUN ["apt", "update"]
RUN ["apt", "install", "-y", "--no-install-recommends", "wget", "ca-certificates"]
RUN ["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"]
RUN ["apt", "install", "-y", "--no-install-recommends", "./google-chrome-stable_current_amd64.deb"]
COPY Surf.class *.jar /usr/local/src/
WORKDIR /usr/local/src
ENTRYPOINT ["java", "-cp", ".", "Surf"]
