# Configuration

Using AWS for infrastructure and [Ansible](https://www.ansible.com)
for build automation.

## Installing Minikube

Currently the minikube file is downloaded locally then
copied onto the remote server. You will need to download 
it into the `files/` subfolder.

```{bash}
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

Reference: [Install Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
