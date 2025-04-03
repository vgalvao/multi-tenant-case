eksctl create cluster \
  --name vgm-eks \
  --region us-east-1 \
  --version 1.27 \
  --nodegroup-name vgm-eks-nodegroup \
  --nodes 2 \
  --node-type t3.medium \
  --managed