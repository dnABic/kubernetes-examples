Test if redis answers:

(printf "PING\r\n"; sleep 1) | nc $(minikube ip) 30379
