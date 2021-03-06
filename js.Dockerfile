FROM node:slim
ENV DEBUG pw:api
RUN ["apt", "update"]
RUN ["apt", "install", "-y", "--no-install-recommends", "wget", "ca-certificates"]
RUN ["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"]
RUN ["apt", "install", "-y", "--no-install-recommends", "./google-chrome-stable_current_amd64.deb"]
COPY surf.js /usr/local/src/
WORKDIR /usr/local/src
RUN ["npm", "install", "playwright"]
ENTRYPOINT ["node", "--harmony", "surf.js"]
