FROM node:slim
ENV DEBUG pw:api
RUN ["apt", "update"]
RUN ["apt", "install", "-y", "--no-install-recommends", "wget", "ca-certificates"]
RUN ["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"]
RUN ["apt", "install", "-y", "--no-install-recommends", "./google-chrome-stable_current_amd64.deb"]
COPY surf.js package.json /usr/local/src/
WORKDIR /usr/local/src
RUN ["npm", "install", "playwright"]

#FROM busybox
#WORKDIR /usr/local/src
#COPY --from=0 /usr/local/src/ .
#COPY --from=0 /opt/google /opt/google
#COPY --from=0 /usr/local/bin/node /usr/bin/
#COPY --from=0 /lib/x86_64-linux-gnu /lib/x86_64-linux-gnu/
#COPY --from=0 /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/
#COPY --from=0 /lib64 /lib64/
ENTRYPOINT ["node", "--harmony", "surf.js"]
