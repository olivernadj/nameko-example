# nameko-example

## todos
 - [x] nameko hello world
 - [x] put it into docker image
 - [x] deploy them to kubernetes via unpacked helm
 - [ ] ~~upgrade them with fluxcd~~ i could not make automated policy works with unpacked helm chats.
   - [x] double check.
   - [x] check what happen if I add fluxcd.io via kubectl edit instead of having the in the manifest in git repo. **Nothing!**
 - [x] use HelmRelease Custom Resource instead unpacked charts.
 


## Observations

### fluxcd.io annotations
Workload policy loose automation, when I commented out fluxcd.io manifestation. It was expected.
```
#  annotations:
#    fluxcd.io/automated: "true"
#    fluxcd.io/tag.hello-app: semver:*
```
![workloads with no automation](https://raw.githubusercontent.com/olivernadj/nameko-example/master/lost-automation.png "Workload with and without annotation")

Although editing `kubectl edit deployment hello-depl` and add back fluxcd.io annotations has no effect. 
That was unexpected. It means flux is threats git repo as a source of truth and does not scan actual deployment instances. 

### POLICY automated
As I expected flux indeed replace the image with a newest tag and also push back the new tag into git repo.


### Unpacked helm charts
Unpacked helm charts are pretty much ignored, by fluxcd.

Therefore we need the HelmRelease Custom Resource. What is come with following prerequisites:
 - HelmRelease Kubernetes custom resource definition
 - Flux Helm Operator with Helm v3 support


## Guide
 
### fluxctl install 
 
```bash
export GHUSER="olivernadj"
fluxctl install \
--git-user=${GHUSER} \
--git-email=${GHUSER}@users.noreply.github.com \
--git-url=git@github.com:${GHUSER}/nameko-example.git \
--git-path=release \
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


### Install the HelmRelease Kubernetes custom resource definition and the operator:
```bash
kubectl apply -f https://raw.githubusercontent.com/fluxcd/helm-operator/master/deploy/crds.yaml

helm upgrade -i helm-operator fluxcd/helm-operator --wait \
--namespace flux \
--set git.ssh.secretName=flux-git-deploy \
--set helm.versions=v3
```


## Conclusion
Finally I managed to set up a working **Managing Helm releases the GitOps way** from an initial
`docker-compose` state.
This experiment gradually thought me how to
 - made automated re-deploy of a vanilla manifests based on github repo changes
 - how to trigger re-deploy of a vanilla manifests based on a docker hub push
 - how to trigger re-deploy of an unpacked charts with helm-operator on git or docker changes

![workloads with automation](https://raw.githubusercontent.com/olivernadj/nameko-example/master/devops-automated.png "Workload with  helm operator")


## Resources
 - https://www.youtube.com/watch?v=OFgziggbCOg
 - https://github.com/fluxcd/helm-operator-get-started
