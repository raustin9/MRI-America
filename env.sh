case "${HOSTNAME:-unset}" in (accona|sinai|kavir|gobi|thar|sahara)
docker_start+=(
    # --mount="type=bind,src=/mnt/seenas2/data,dst=/home/raustin9/src/Sunrise-Demo/data,readonly=false"
    --mount="type=bind,src=/mnt/seenas2/data,dst=/mnt/seenas2/data,readonly=false"
    # --mount="type=bind,src=/mnt/data,dst=/mnt/data,readonly=false"
    # --publish=127.202.208.70:33267:33267
    --net=host
)

docker_service_start+=(
    --mount="type=bind,src=/mnt/seenas2/data,dst=/mnt/seenas2/data,readonly=true"
)

;; esac

GLOBE_PROD_PORT=33267
GLOBE_PROD_IP=127.202.208.70


#if [ "${USER:-}" = "raustin9" ]; then
#    # echo "User: ${USER:-}"
#    server_bind=127.242.160.24  # $(,address sunrise +%B)
#    server_port=57872  # $(,address sunrise +%P)
#fi
#if [ "${USER:-}" = "raustin9" ]; then
#    # echo "User: ${USER:-}"
#    server_bind=${GLOBE_PROD_IP}
#    server_port=${GLOBE_PROD_PORT}
#    # server_bind=127.242.160.24  # $(,address sunrise +%B)
#    # server_port=57872  # $(,address sunrise +%P)
#fi
case "${USER:?}@${HOSTNAME:?}" in
("thobson2@sahara")
    docker_tag=th--${docker_tag:?}
    docker_name=th--${docker_name:?}
    
    server_bind=0.0.0.0  # 127.233.183.68  # $(,address th/sunrise/server/city +%B)
    server_port=47361  # $(,address th/sunrise/server/city +%P)
    server_host=http://sahara.eecs.utk.edu:${server_port:?}/

    client_bind=0.0.0.0  # 127.148.193.76  # $(,address th/sunrise/client +%B)
    client_port=54742  # $(,address th/sunrise/client +%P)
    client_host=http://sahara.eecs.utk.edu:${client_port:?}/
    ;;

("raustin9@sahara")
    docker_tag=aa--${docker_tag:?}
    docker_name=aa--${docker_name:?}

    server_bind=0.0.0.0  # 127.35.215.166  # $(,address aa/sunrise/server/city +%B)
    server_port=4002  # $(,address aa/sunrise/server/city +%P)
    server_host=http://sahara.eecs.utk.edu:${server_port:?}/

    client_bind=0.0.0.0  # 127.109.99.176  # $(,address aa/sunrise/client +%B)
    client_port=4001  # $(,address aa/sunrise/client +%P)
    client_host=http://sahara.eecs.utk.edu:${client_port:?}/
    ;;
esac
