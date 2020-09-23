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
--git-url=git@github.com:${GHUSER}/nameko-example.git \
--git-path=k8s \
--namespace=flux | kubectl apply -f - 

kubectl -n flux rollout status deployment/flux
```

troubleshooting 
https://github.com/fluxcd/flux/issues/2517
```
- --registry-exclude-image=*
- --registry-include-image=docker.io/olivernadj/*
```

### add deploy keys

```
export FLUX_FORWARD_NAMESPACE="flux" 
fluxctl identity
```
https://github.com/olivernadj/nameko-example/settings/keys


### check current images
```bash
kubectl get pods --all-namespaces -o jsonpath="{..image}" | tr -s '[[:space:]]' '\n' | sort | uniq -c
```