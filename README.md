# nameko-example

## todos
 - [x] nameko hello world
 - [x] put it into docker image
 - [x] deploy them to kubernetes via helm
 - [ ] upgrade them with fluxcd
 
 
 
 
 
### fluxctl install 
 
```bash
export GHUSER="olivernadj"
fluxctl install \
--git-user=${GHUSER} \
--git-email=${GHUSER}@users.noreply.github.com \
--git-url=git@github.com:${GHUSER}/nameko-example/ \
--git-path=k8s \
--namespace=flux | kubectl apply -f - 
```
