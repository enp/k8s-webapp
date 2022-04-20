# Example Kubernetes Web Application

Example web application for k8s with unlimited ingress and limited egress, so allowed only:

 + resolving via cluster dns resolver
 + http[s] requests to [Yandex Object Storage](https://cloud.yandex.ru/docs/storage/)

How to build:
```
docker build -t <image> app
docker push <image>
```
How to run:
```
cp values.example.yaml values.yaml
vi values.yaml
helm install --create-namespace --namespace webapp webapp chart
```
[Yandex Application Load Balancer Ingress controller](https://cloud.yandex.ru/docs/managed-kubernetes/tutorials/alb-ingress-controller) must be configured before running example