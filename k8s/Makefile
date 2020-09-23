CONTEXT ?= do
NAMESPACE ?= nameko
TAG ?= latest

deploy-namespace:
	kubectl --context=$(CONTEXT) apply -f namespace.yaml

# helm

deploy-dependencies:
	helm upgrade broker stable/rabbitmq --install \
	--namespace $(NAMESPACE) --kube-context=$(CONTEXT)

install-charts:
	$(MAKE) SERVICE_NAME=hello install-chart

test-charts:
	$(MAKE) SERVICE_NAME=hello test-chart

lint-charts:
	$(MAKE) SERVICE_NAME=hello lint-chart

test-chart:
	helm upgrade $(SERVICE_NAME) charts/$(SERVICE_NAME) --install \
	--namespace=$(NAMESPACE) --kube-context $(CONTEXT) \
	--dry-run --debug --set image.tag=$(TAG)

install-chart:
	helm upgrade $(SERVICE_NAME) charts/$(SERVICE_NAME) --install \
	--namespace=$(NAMESPACE) --kube-context=$(CONTEXT) \
	--set image.tag=$(TAG)

lint-chart:
	helm lint charts/$(SERVICE_NAME) --strict
